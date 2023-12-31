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
* `pm2 start dataposter.py --name crustypi-poster` <br />
Now we can restart our processes whenever we want with the new updates <br />
#### *Automate start process by*
`sudo env PATH=$PATH:/usr/bin /usr/lib/node_modules/pm2/bin/pm2 startup systemd -u crustypi --hp /home/crustypi` <br />
Following command is provided by doing: `pm2 startup`

### Process Database
A "small" database on the raspberry containing recent data <br />
The thought is to wipe the data on each post of data from the pi, on occasions that the raspberry pi is not connected to the internet it will store the data without wiping it until it's connected to the internet again. <br />

The databse is a sqlite dabtase which is default installed in python.

### Arduino (Analog sensors)
A raspberry pi can only read digital signals. In order to read analog signals from analog sensors, we have to do a bit of extra work. <br />
This is where the arduino comes in, which is able to read analog signals.

By installing the Firmata example called "StandardFirmata" on the arduino, and installing analog sensors in the correct pins, we can get the signals from an arduino board into our Python code using Firmata. <br />
Python's version for Firmata: `pip install pyfirmata` <br />

After this you need to have hardware permission to use Serial on your raspberry pi, this can be done with following command:
`sudo adduser $USER dialout` <br />
Afterwards, restart your system.

Guide can be found here: https://roboticsbackend.com/control-arduino-with-python-and-pyfirmata-from-raspberry-pi/#Step_1_Run_StandardFirmata_on_your_Arduino_board


### MQTT Broker

`pip install paho-mqtt`

HiveMQ Broker credentials: <br />
*``crustypi``* <br />
*``Crustyburger@123``*
With: <br />
Port: `8883`
URL: `a91938236da5469ca7780ce25a489b8f.s2.eu.hivemq.cloud`

*Subscriber* <br />
*``crustypi-ui``* <br />
*``Crustyburger@123``*

## API & Client

If yarn is not installed run:
* `npm install yarn --global` <br />
  Install nextjs and dependencies:
* `yarn` <br />
  Run Nextjs:
* `yarn dev` <br />

## Creating a MongoDB URI and ALLOW_KEY for Post Requests

To create a MongoDB URI, follow these steps:

1. Sign up for a free MongoDB Atlas account at https://www.mongodb.com/cloud/atlas/register.
2. Create a new project and cluster.
3. Click on "Connect" and select "Connect your application".
4. Choose your driver and version, then copy the connection string.
5. Replace `<password>` with your MongoDB Atlas password and `<dbname>` with the name of your database.
6. Paste the string in your environment variables before processing the request.

To create an ALLOW_KEY for post requests, follow these steps:

1. Generate a random string of characters to use as your ALLOW_KEY.
2. Add the ALLOW_KEY to your environment variables.
3. In your code, check that the ALLOW_KEY in the request headers matches the ALLOW_KEY in your environment variables before processing the request.

Diagram of infrastructure:
![alt text](https://github.com/MatteusSteinberg/crustypi/blob/master/images/diagram.png?raw=true)