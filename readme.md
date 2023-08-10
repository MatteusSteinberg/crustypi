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
And start the processes up 
* `pm2 start index.py --name crustypi` <br />
* `pm2 start dataposer.py --name crustypi-poster` <br />
Now we can restart our processes whenever we want with the new updates <br />
#### *Automate start process by*
`sudo env PATH=$PATH:/usr/bin /usr/lib/node_modules/pm2/bin/pm2 startup systemd -u crustypi --hp /home/crustypi` <br />
Following command is provided by doing: `pm2 startup`

### Process Database
A "small" database on the raspberry containing recent data <br />
The thought is to wipe the data on each post of data from the pi, on occasions that the raspberry pi is not connected to the internet it will store the data without wiping it until it's connected to the internet again. <br />

The databse is a "Tinydb" which is installed simply by doing `pip install tinydb`, the code takes care of the rest.

## API