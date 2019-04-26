# Ping Node Server

#### Installation

Install from the NodeServer store or manually.

    cd .polyglot/nodeservers
    git clone https://github.com/markv58/Ping.git
    cd Ping
    chmod +x install.sh
    ./install.sh

#### Requirements

A local Polyglot Nodeserver running on a Raspberry Pi.

#### What does this do?

This will ping devices on your lan or a .com. If a device does not respond it will be reported as In Fault until it hits 5 faults and then it's reported as Off Network. You can keep tabs on your devices, router, modem, internet connection, etc. and program an ISY controlled switch to cycle Off then On to reset the device or send yourself a notification.
