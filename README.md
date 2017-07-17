# MLInAction
## Pre-Install
1. How to install the latest python on CentOS
Refer to https://www.python.org/downloads/

```bash
wget https://www.python.org/ftp/python/3.6.1/Python-3.6.1.tar.xz
tar Jxvf Python-3.6.1.tar.xz
cd Python-3.6.1/
./configure --prefix=/usr/local/python3
sudo make && sudo make install

sudo rm /usr/bin/python
sudo ln -s /usr/local/python3/bin/python3.6 /usr/bin/python
```



2. Install numpy and matplotlib on CentOS

```bash
sudo yum install numpy -y
sudo yum install python-matplotlib -y
```

tutorial
http://cs231n.github.io/python-numpy-tutorial/

3. How to enable auto-complete in python command-line

4. python vim related plugin
http://vimawesome.com/plugin/python-mode
https://github.com/python-mode/python-mode


# TODO
- [ ] Investigation on Virtualenv
https://virtualenv.pypa.io/en/latest/index.html`

Reference codes:
https://github.com/pbharrin/machinelearninginaction

What does if name main do
https://stackoverflow.com/questions/419163/what-does-if-name-main-do
