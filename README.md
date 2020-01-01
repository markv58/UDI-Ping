# Ping Node Server

#### Installation

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
