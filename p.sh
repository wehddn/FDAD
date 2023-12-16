sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt update
sudo apt install python3.9

sudo update-alternatives --install /usr/bin/python python /usr/bin/python3.9 1
sudo update-alternatives --install /usr/bin/python python /home/gitpod/.pyenv/shims/python3.12 2
sudo update-alternatives --config python
. ~/.bashrc
alias python='/usr/bin/python3.9'