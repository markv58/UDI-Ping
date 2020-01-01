#!/usr/bin/env python3
"""
This is a NodeServer was created using template for Polyglot v2 written in Python2/3
by Einstein.42 (James Milne) milne.james@gmail.com
"""
import polyinterface
import sys
import time
import os
import struct
import array
import fcntl
import subprocess

LOGGER = polyinterface.LOGGER

class Controller(polyinterface.Controller):

    def __init__(self, polyglot):
        super(Controller, self).__init__(polyglot)
        self.name = 'Ping'
        self.firstCycle = True
        
    def start(self):
        LOGGER.info('Started Ping')
        self.discover()
        self.check_params()
        
    def shortPoll(self):
        for node in self.nodes:
            self.nodes[node].update()
        if self.firstCycle:
             self.query()
             self.firstCycle = False

    def longPoll(self):
        pass

    def query(self):
        self.reportDrivers()
        for node in self.nodes:
            self.nodes[node].reportDrivers()

    def discover(self, *args, **kwargs):
        #Discover nodes and add them
        for key,val in self.polyConfig['customParams'].items():
            netip = val.replace('.','')
            self.addNode(hostnode(self, self.address, netip, val, key))
            
    def update(self):
        pass

    def delete(self):
        LOGGER.info('Deleting Ping NodeServer.')

    def stop(self):
        LOGGER.debug('NodeServer stopped.')

    def check_params(self):
        pass

    def remove_notices_all(self,command):
        LOGGER.info('remove_notices_all:')
        # Remove all existing notices
        self.removeNoticesAll()

    def update_profile(self,command):
        LOGGER.info('update_profile:')
        st = self.poly.installprofile()
        return st

    id = 'controller'
    commands = {
        'DISCOVER': discover,
        'UPDATE_PROFILE': update_profile,
        'REMOVE_NOTICES_ALL': remove_notices_all
    }
    drivers = [{'driver': 'ST', 'value': 1, 'uom': 2}]

class Ping(object):

    def __init__(self, ip, timeout):
        self.ip = ip
        self.timeout = timeout

    def ping(self):
        response = 0
        try:
            response,result = subprocess.getstatusoutput("ping -c1 -w2 " + self.ip)
            #LOGGER.debug('first try')
            #LOGGER.debug(response)
            if response == 0:
                return response
        except:
            return None
        if response == 127:
            try:
                response = subprocess.call(['/sbin/ping','-c1','-W2', self.ip], shell=False)
                #LOGGER.debug('second try')
                #LOGGER.debug(response)
                if response == 0:
                    return response
            except:
                return None
        else:
            return None

class hostnode(polyinterface.Node):
    def __init__(self, controller, primary, address, ipaddress, name):
        super(hostnode, self).__init__(controller, primary, address, name)
        self.ip = ipaddress
        self.scan = 1
        self.missed = 0
        
    def start(self):
        self.setOn('DON')
        self.reportDrivers()
        
    def update(self):
        if (self.scan):
            netstat = Ping(ip=self.ip,timeout=self.parent.polyConfig['shortPoll'])
            result = netstat.ping()
            
            if (result != None):
                self.missed = 0
                self.setOnNetwork(0)
                #LOGGER.debug(self.ip + ': On Network')
            elif (self.missed >= 5):
                self.setOffNetwork()
                #LOGGER.debug(self.ip + ': Off Network')           
            elif self.missed >= 0 and self.missed < 5:
                self.missed += 1
                self.setInFault(self.missed)
                #LOGGER.debug(self.ip + ': In Fault')
 
            
    def setOnNetwork(self,missed):
        self.setDriver('ST', 0)
        self.setDriver('GV0', self.missed)
    
    def setInFault(self, missed):
        self.setDriver('ST', 1)
        self.setDriver('GV0', self.missed)
        
    def setOffNetwork(self):
        self.setDriver('ST', 2)
        self.setDriver('GV0', self.missed)
    
    def setOn(self, command):
        self.missed = 0
        self.setOffNetwork()
        self.setDriver('GV0', 0)
        self.setDriver('GV1', 1)
        self.scan = 1

    def setOff(self, command):
        self.missed = 0
        self.setOffNetwork()
        self.setDriver('GV0', 0)
        self.setDriver('GV1', 0)
        self.scan = 0

    def query(self):
        self.reportDrivers()


    drivers = [
        {'driver': 'ST', 'value': 0, 'uom': 25},
        {'driver': 'GV0', 'value': 0, 'uom': 56},
        {'driver': 'GV1', 'value': 1, 'uom': 2}
    ]

    id = 'hostnode'

    commands = {
                    'DON': setOn, 'DOF': setOff, 'QUERY': query
                }
if __name__ == "__main__":
    try:
        polyglot = polyinterface.Interface('PingNodeServer')
        polyglot.start()
        control = Controller(polyglot)
        control.runForever()
    except (KeyboardInterrupt, SystemExit):
        sys.exit(0)

