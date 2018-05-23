sudo dpkg-reconfigure tzdata
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt-get update
sudo apt-get install python3.6 --assume-yes
sudo ln -s /usr/bin/python3.6 /usr/bin/python
sudo rm /usr/bin/python3
sudo ln -s /usr/bin/python3.6 /usr/bin/python3
sudo apt-get upgrade --assume-yes
sudo apt-get install build-essential unzip --assume-yes
sudo apt-get install python3-setuptools python3-dev --assume-yes
sudo apt-get install git-core --assume-yes
sudo su
curl https://raw.githubusercontent.com/aurora/rmate/master/rmate > rmate
sudo mv rmate /usr/local/bin
sudo chmod +x /usr/local/bin/rmate
rmate ~/.bashrc
source ~/.bashrc
rmate ~/.bashrc
source ~/.bashrc
mkdir /home/ubuntu/mpcs
cd /home/ubuntu/mpcs
mkvirtualenv mpcs
pip install --upgrade boto3
pip install --upgrade jmespath-terminal
pip install --upgrade awscli
pip install --upgrade PyMySQL
pip install --upgrade psycopg2-binary
pip install --upgrade sqlalchemy
pip install --upgrade stripe
pip install --upgrade flask
pip install --upgrade flask-sqlalchemy
pip install --upgrade gunicorn
pip install --upgrade globus_sdk
workon mpcs
deactivate
workon mpcs
python
cd
deactivate
ll
ll .ssh
sudo adduser --disabled-password --gecos ‘mpcsroot' mpcsroot
sudo adduser --disabled-password --gecos 'mpcsroot' mpcsroot
sudo bash -c '/bin/echo campusadmin ALL=\(ALL:ALL\) NOPASSWD:ALL >> /etc/sudoers'
sudo mkdir /home/mpcsroot/.ssh
sudo nano /home/mpcsroot/.ssh/authorized_keys
sudo chmod 600 /home/mpcsroot/.ssh/authorized_keys
sudo chown -R mpcsroot:mpcsroot /home/mpcsroot/.ssh
ll
chmod 755 .ssh
ll
ll .ssh
workon mpcs
ls
git clone https://github.com/mpcs-cc/anntools
ls
cd anntools
nano config.txt
ls .
echo "" > hw6_run.py
rmate hw6_run.py
cd .
cd ..
ls
echo "" > hw6_annotator.py
rmate hw6_annotator.py
python hw6_annotator.py
ls
workon mpcs
python hw6_annotator.py
rmate hw6_annotator.py
python hw6_annotator.py
tmux
ls
tmux attach -t 1
tmux list-sessions
tmux attach -t 0
workon mpcs
ls
rmate annotator.py
python annotator.py
rmate anntools/run.py
python annotator.py
rmate annotator.py
python annotator.py
python
os.environ.get('AWS_SNS_JOB_COMPLETE_TOPIC')
python
python annotator.py
ls
cd anntools
ls
rmate annotate.py
ls
cd ..
python annotate.py
python annotator.py
