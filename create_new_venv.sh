#/usr/bin/bash

sudo pip install setuptools
sudo pip install --upgrade setuptools
sudo pip install virtualenv
sudo pip install --upgrade virtualenv
virtualenv --system-site-packages -p python3 ${1}
