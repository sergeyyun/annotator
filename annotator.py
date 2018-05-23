#Reference:
#https://docs.python.org/3/library/uuid.html
#https://docs.python.org/3/library/json.html
#https://docs.aws.amazon.com/AmazonS3/latest/API/sigv4-HTTPPOSTConstructPolicy.html
#https://docs.aws.amazon.com/AmazonS3/latest/API/sigv4-post-example.html
#https://stackoverflow.com/questions/34348639/amazon-aws-s3-browser-based-upload-using-post
#http://boto3.readthedocs.io/en/latest/guide/s3.html
#http://boto3.readthedocs.io/en/latest/guide/migrations3.html
#http://boto3.readthedocs.io/en/latest/reference/services/s3.html#S3.Bucket.download_file
#https://docs.python.org/3/library/re.html
#https://docs.python.org/2/library/subprocess.html
#http://boto3.readthedocs.io/en/latest/guide/sqs-example-long-polling.html

import uuid
import subprocess
import boto3
import botocore
import os
import re
import shlex
from pathlib import Path
from ast import literal_eval

AWS_SNS_JOB_REQUEST_QUEUE = 'syun0_job_requests'
AWS_DYNAMODB_ANNOTATIONS_TABLE = "syun0_annotations"

if __name__ == '__main__':
    #connect to SQS and get the message queue
    sqs = boto3.resource('sqs', region_name='us-east-1')
    queue = sqs.get_queue_by_name(QueueName=AWS_SNS_JOB_REQUEST_QUEUE)

    while True:
        messages = queue.receive_messages(WaitTimeSeconds=20)
        if(messages):
            for message in messages:
                #read message body and extract the parameters for the annotator
                body = literal_eval(message.body)
                data = literal_eval(body.get('Message'))
                input_file_name = data.get('input_file_name')
                job_id = data.get('job_id')
                s3_key_input_file = data.get('s3_key_input_file')
                user_id = data.get('user_id')
                user_email = data.get('user_email')
                bucket = data.get('s3_inputs_bucket')
                submit_time = data.get('submit_time')
                job_status = data.get('job_status')

                #download file from S3 and save it to the anntools/data/job_id folder
                s3 = boto3.resource('s3')
                save_dir = Path('anntools/data/' + job_id + '/')
                if not os.path.exists(save_dir):
                    os.makedirs(save_dir)
                file_path_str = 'anntools/data/' + job_id + '/' + input_file_name

                try:
                    s3.Bucket(bucket).download_file(s3_key_input_file, file_path_str)
                except botocore.exceptions.ClientError:
                    print('Error: could not download the requested file')

                #check if file exists in data folder, spawn a subprocess, run annotator
                file_path = Path(file_path_str)
                if (file_path.is_file()):
                    #pass user id and job id as command line arguments to the annotator
                    command = 'python run.py data/' + job_id + '/' + input_file_name + ' ' + user_id + ' ' + job_id + ' ' + user_email
                    args = shlex.split(command)
                    subprocess.Popen(args, cwd="anntools/")
                    #update job status to running
                    try:
                        dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
                        ann_table = dynamodb.Table(AWS_DYNAMODB_ANNOTATIONS_TABLE)
                    except Exception:
                        print("Error: failed to connect to the database")

                    try:
                        response = ann_table.update_item(
                            Key = {'job_id': job_id},
                            UpdateExpression = 'SET job_status = :val1',
                            ConditionExpression = 'job_status = :val2',
                            ExpressionAttributeValues={
                                ':val1': "RUNNING",
                                ':val2': "PENDING"
                            }
                        )
                    except Exception as e:
                        print("Error: failed to update database record")

                else:
                    print("Error: file " + input_file_name + " not found")

                #delete the message
                message.delete()

        else:
            print("No new jobs found")
