# Ping Node Server

#### Updating

Answer Yes to upload profile. Restart the nodeserver, click the Update Profile button then close and restart the AC.

#### Installation

#### Please backup your Isy and Polyglot before installing the node server.

Install from the NodeServer store or manually.

    cd .polyglot/nodeservers
    git clone https://github.com/markv58/UDI-Ping.git
    cd UDI-Ping
    chmod +x install.sh
    ./install.sh

Note: If you do a manual install, you will need to do a 'git reset --hard' in the .polyglot/nodeservers/UDI-Ping folder before you can update from the NodeServer store or do a 'git pull'.

#### Requirements

A local Polyglot Nodeserver running on a Raspberry Pi.

#### What does this do?

This will ping devices on your lan or a .com. If a device does not respond it will be reported as In Fault until it hits 5 faults and then it's reported as Off Network. You can keep tabs on your devices, router, modem, internet connection, etc. and program an ISY controlled switch to cycle Off then On to reset the device or send yourself a notification.

1.0.2 minor bug fix

1.0.3 fixed crash when external ip is unreachable or modem is down

1.0.5 works on Polisy now, use ip instead of the domain name. Ex. 8.8.8.8 for Google

1.0.8 Standardize url input for RPi and Polisy, <www.url.com>

1.0.9 Set all as On Network on restart.

1.0.10 Increased missed pings to 1440 max instead of 5, Off network count still 5 missed pings.

1.0.11 Better error handling.
