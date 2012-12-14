#!/usr/bin/env python
import ConfigParser
from suds.client import Client

config = ConfigParser.ConfigParser()
config.read('../../config/conf.cfg')
get_url  = config.get('getTMCDB', 'url')
get_port = config.get('getTMCDB', 'port')
set_url  = config.get('setTMCDB', 'url')
set_port = config.get('setTMCDB', 'port')

c = Client(('http://%s:%s/?wsdl'%(set_url,set_port)))
c.set_options(cache=None)

g = Client(('http://%s:%s/?wsdl'%(get_url,get_port)))
g.set_options(cache=None)

steName ="TEST"
configurationName = "SUCCESS"
startupName = "TEST"
device = "TEST"
antennaName = "TEST"
value = "TEST"
computer = "TEST"
container = "TEST"
padname = "TEST"
cai = "TEST"
disklessName = "TEST"
antenna = "TEST"
computername = "TEST"
pduName = "TEST"
pduPort = "TEST"
abmType = "TEST"
lkmFile = "TEST"

print c.service.setChannelAddress(steName, configurationName, startupName, device, antenna, value)
print c.service.setNodeAddress(steName, configurationName,	startupName, device, antenna, value)
print c.service.setEnableDeviceSimulation(steName, configurationName, startupName, device, antenna)
print c.service.setDisableDeviceSimulation(steName, configurationName, startupName, device, antenna)
print c.service.setEnableDeviceAtStartup(steName, configurationName, startupName, device, antenna)
print c.service.setDisableDeviceAtStartup(steName, configurationName, startupName, device, antenna)
print c.service.addAntennaToStartup(steName, configurationName, startupName, antenna)
print c.service.removeAntennaFromStartup(steName, configurationName, startupName, antenna)
print c.service.deployContainer(steName, configurationName, startupName, computer, container)
print c.service.undeployContainer(steName, configurationName, startupName, container)
print c.service.deployComponent(steName, configurationName, startupName, container, antenna, device)
print c.service.undeployComponent(steName, configurationName, startupName, container, antenna, device)
print c.service.assignAntennaToPad(steName, configurationName, startupName, padname, antenna)
print c.service.unassingPad(steName, configurationName, startupName, padname)
print c.service.addComputer(steName, configurationName, startupName, computername)
print c.service.switchMoveAntennaToPad(steName, configurationName, startupName, antenna, padname)
print c.service.addAntennaToCAI(steName, configurationName, startupName, cai, antenna)
print c.service.removeAntennaFromCAI(steName, configurationName, startupName, cai, antenna)
print c.service.addAntennaToACACAI(steName, configurationName, startupName, cai, antenna)
print c.service.removeAntennaFromACACAI(steName, configurationName, startupName, cai, antenna)
print c.service.addDisklessToSiteXml(steName, configurationName, startupName, disklessName, pduName, pduPort, abmType)
print c.service.removeDisklessFromSiteXml(steName, configurationName, startupName, disklessName)
print c.service.setLkmLoaderInXml(steName, configurationName, startupName,antennaName, lkmFile)
print c.service.setIPInXml(steName, configurationName, startupName,antennaName)


#GETTER
hostname = "TEST"
hostType = "TEST"
mandate = "TEST"

print g.service.getPduName(steName, configurationName, startupName, hostname)
print g.service.getPduPort(steName, configurationName, startupName, hostname)
print g.service.getAllPduPort(steName, configurationName, startupName, hostname)
print g.service.getHosts(steName, configurationName, startupName)
print g.service.getHostbyType(steName, configurationName, startupName, hostType)
print g.service.getKernelVersion(steName, configurationName, startupName, hostname)
print g.service.getAcsDaemons(steName, configurationName, startupName, hostname)
print g.service.getCmdLine(steName, configurationName, startupName, hostname, mandate)
print g.service.getLkmFile(steName, configurationName, startupName, hostname)
print g.service.getModules(steName, configurationName, startupName, hostname, mandate)
print g.service.getTypes(steName, configurationName, startupName)
print g.service.getHostType(steName, configurationName, startupName, hostname)
print g.service.getChannelAddress(steName, configurationName, startupName, device, antenna)
print g.service.getNodeAddress(steName, configurationName, startupName, device, antenna)
print g.service.isSimulated(steName, configurationName,startupName, device, antenna)
print g.service.isEnableDeviceAtStartup(steName, configurationName, startupName, device, antenna)
print g.service.isAntennaInCurrentStartup(steName, configurationName, startupName, antenna)
print g.service.isPadConfigured(steName, configurationName, startupName, padname)
print g.service.isPadAssigned(steName, configurationName, startupName, padname)
print g.service.getAntennaNameAssignedToPad(steName, configurationName, startupName, padname)
print g.service.getConfiguredAntennas(steName, configurationName, startupName)
print g.service.isComputerDeployed(steName, configurationName, startupName, computername)

