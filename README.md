# MLInAction
## Pre-Install
1. How to install the latest python on CentOS
Refer to https://www.python.org/downloads/
``bash
wget https://www.python.org/ftp/python/3.6.1/Python-3.6.1.tar.xz
tar Jxvf Python-3.6.1.tar.xz
cd Python-3.6.1/
./configure --prefix=/usr/local/python3
sudo make && sudo make install

sudo rm /usr/bin/python
sudo ln -s /usr/local/python3/bin/python3.6 /usr/bin/python
``



2. Install numpy on CentOS
``bash
sudo yum install numpy -y
``

3. How to enable auto-complete in python command-line


# TODO
- [ ] Investigation on Virtualenv
https://virtualenv.pypa.io/en/latest/index.html`
