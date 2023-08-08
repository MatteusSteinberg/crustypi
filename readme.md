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

Install 
* `sudo apt install nodejs` <br />
Install node version manager - includes node package manager
* `curl -o- https://raw.githubusercontent.com/creationix/nvm/v0.33.0/install.sh | bash` <br />
Install pm2 globally
* `sudo npm install pm2 --global` <br />
And start the process up 
* `pm2 start index.py --name crustypi` <br />
Now we can restart our process whenever we want with the new updates