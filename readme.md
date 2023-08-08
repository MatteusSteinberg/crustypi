# Crustypi raspberry pi
The directory can be found under /home/{user}/application/crustypi <br />
The credentials are the following: <br />
*``crustypi``* <br />
*``crustyburger``*

## Pipeline
### The following files will not be updated via git and is found under the following paths on the raspberry pi

* gitpull.service = /etc/systemd/system/gitpull.service
* service.timer = /etc/systemd/system/service.timer
* service.sh = /usr/bin/service.sh

gitpull.service and service.timer is enabled on the pi using `systemctl start 'file'` and the status can be checked using `systemctl status 'file'`

## Process manager

Install pman: https://pypi.org/project/pman/
* `pip install pman`
* `sudo apt install virtualenv virtualenvwrapper` <br />
Add the following lines to .bashrc
* `export WORKON_HOME=~/python-envs`
* `source /usr/share/virtualenvwrapper/virtualenvwrapper.sh` <br />
And create the virtual python environment
* `mkvirtualenv --python=python3 python_env`