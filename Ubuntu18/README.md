
## Nvidia Drivers on Ubuntu 18.04
$ sudo apt-get purge nvidia*

$ ubuntu-drivers devices

$ sudo  ubuntu-drivers autoinstall

$ sudo apt-get update
$ sudo apt-get upgrade


## Python 3.9 on Ubuntu 18.04

```
Deadsnake Repo for Python: https://launchpad.net/~deadsnakes/+archive/ubuntu/ppa
```
$ sudo add-apt-repository ppa:deadsnakes/ppa
$ sudo apt update
$ sudo apt install python3.9
$ python -V
