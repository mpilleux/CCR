#!/usr/bin/env python
# encoding: utf8
#
# Copyright © Burak Arslan <burak at arskom dot com dot tr>,
#             Arskom Ltd. http://www.arskom.com.tr
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
#    1. Redistributions of source code must retain the above copyright notice,
#       this list of conditions and the following disclaimer.
#    2. Redistributions in binary form must reproduce the above copyright
#       notice, this list of conditions and the following disclaimer in the
#       documentation and/or other materials provided with the distribution.
#    3. Neither the name of the owner nor the names of its contributors may be
#       used to endorse or promote products derived from this software without
#       specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER BE LIABLE FOR ANY DIRECT,
# INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY
# OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
# NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE,
# EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#

import logging

from spyne.decorator import srpc
from spyne.service import ServiceBase
from spyne.model.complex import Iterable
from spyne.model.primitive import Integer
from spyne.model.primitive import String
from spyne.model.primitive import Unicode

from spyne.util.simple import wsgi_soap_application

try:
    from wsgiref.simple_server import make_server
except ImportError:
    print("Error: example server code requires Python >= 2.5")
    raise

'''
'''

class STEDeploymentInfo(ServiceBase):
    @srpc(Unicode, Unicode, Unicode, Unicode, Unicode, Unicode, _returns=String)
    def setChannelAddress(steName, configurationName, startupName, device, antenna, value):
        if configurationName.__contains__("SUCCESS"):
            return "1"
        else:
            return "0"
    @srpc(Unicode, Unicode, Unicode, Unicode, _returns=String)
    def getPduName(steName, configurationName, startupName, hostname):
        if configurationName.__contains__("SUCCESS"):
            return "1"
        else:
            return "0"
    @srpc(Unicode, Unicode, Unicode, Unicode, Unicode, _returns=String)
    def getPduPort(steName, configurationName, startupName, hostname):
        if configurationName.__contains__("SUCCESS"):
            return "1"
        else:
            return "0"
    @srpc(Unicode, Unicode, Unicode, Unicode, _returns=String)
    def getAllPduPort(steName, configurationName, startupName, hostname):
        if configurationName.__contains__("SUCCESS"):
            return "1"
        else:
            return "0"
    @srpc(Unicode, Unicode, Unicode, _returns=String)
    def getHosts(steName, configurationName, startupName):
        if configurationName.__contains__("SUCCESS"):
            return "1"
        else:
            return "0"
    @srpc(Unicode, Unicode, Unicode, Unicode, _returns=String)
    def getHostbyType(steName, configurationName, startupName, hostType):
        if configurationName.__contains__("SUCCESS"):
            return "1"
        else:
            return "0"
    @srpc(Unicode, Unicode, Unicode, Unicode, _returns=String)
    def getKernelVersion(steName, configurationName, startupName, hostname):
        if configurationName.__contains__("SUCCESS"):
            return "1"
        else:
            return "0"
    @srpc(Unicode, Unicode, Unicode, Unicode, _returns=String)
    def getAcsDaemons(steName, configurationName, startupName, hostname):
        if configurationName.__contains__("SUCCESS"):
            return "1"
        else:
            return "0"
    @srpc(Unicode, Unicode, Unicode, Unicode, Unicode, _returns=String)
    def getCmdLine(steName, configurationName, startupName, hostname, mandate):
        if configurationName.__contains__("SUCCESS"):
            return "1"
        else:
            return "0"
    @srpc(Unicode, Unicode, Unicode, Unicode, _returns=String)
    def getLkmFile(steName, configurationName, startupName, hostname):
        if configurationName.__contains__("SUCCESS"):
            return "1"
        else:
            return "0"
    @srpc(Unicode, Unicode, Unicode, Unicode, Unicode, _returns=String)
    def getModules(steName, configurationName, startupName, hostname, mandate):
        if configurationName.__contains__("SUCCESS"):
            return "1"
        else:
            return "0"
    @srpc(Unicode, Unicode, Unicode, _returns=String)
    def getTypes(steName, configurationName, startupName):
        if configurationName.__contains__("SUCCESS"):
            return "1"
        else:
            return "0"
    @srpc(Unicode, Unicode, Unicode, Unicode, _returns=String)
    def getHostType(steName, configurationName, startupName, hostname):
        if configurationName.__contains__("SUCCESS"):
            return "1"
        else:
            return "0"
    @srpc(Unicode, Unicode, Unicode, Unicode, Unicode, _returns=String)
    def getChannelAddress(steName, configurationName, startupName, device, antenna):
        if configurationName.__contains__("SUCCESS"):
            return "1"
        else:
            return "0"
    @srpc(Unicode, Unicode, Unicode, Unicode, Unicode, _returns=String)
    def getNodeAddress(steName, configurationName, startupName, device, antenna):
        if configurationName.__contains__("SUCCESS"):
            return "1"
        else:
            return "0"
    @srpc(Unicode, Unicode, Unicode, Unicode, Unicode, _returns=String)
    def isSimulated(steName, configurationName,startupName, device, antenna):
        if configurationName.__contains__("SUCCESS"):
            return "1"
        else:
            return "0"
    @srpc(Unicode, Unicode, Unicode, Unicode, Unicode, _returns=String)
    def isEnableDeviceAtStartup(steName, configurationName, startupName, device, antenna):
        if configurationName.__contains__("SUCCESS"):
            return "1"
        else:
            return "0"
    @srpc(Unicode, Unicode, Unicode, Unicode, _returns=String)
    def isAntennaInCurrentStartup(steName, configurationName, startupName, antenna):
        if configurationName.__contains__("SUCCESS"):
            return "1"
        else:
            return "0"
    @srpc(Unicode, Unicode, Unicode, Unicode, _returns=String)
    def isPadConfigured(steName, configurationName, startupName, padname):
        if configurationName.__contains__("SUCCESS"):
            return "1"
        else:
            return "0"
    @srpc(Unicode, Unicode, Unicode, Unicode, _returns=String)
    def isPadAssigned(steName, configurationName, startupName, padname):
        if configurationName.__contains__("SUCCESS"):
            return "1"
        else:
            return "0"
    @srpc(Unicode, Unicode, Unicode, Unicode, _returns=String)
    def getAntennaNameAssignedToPad(steName, configurationName, startupName, padname):
        if configurationName.__contains__("SUCCESS"):
            return "1"
        else:
            return "0"
    @srpc(Unicode, Unicode, Unicode, _returns=String)
    def getConfiguredAntennas(steName, configurationName, startupName):
        if configurationName.__contains__("SUCCESS"):
            return "1"
        else:
            return "0"
    @srpc(Unicode, Unicode, Unicode, Unicode, _returns=String)
    def isComputerDeployed(steName, configurationName, startupName, computername):
        if configurationName.__contains__("SUCCESS"):
            return "1"
        else:
            return "0"

if __name__=='__main__':
    logging.basicConfig(level=logging.DEBUG)
    logging.getLogger('spyne.protocol.xml').setLevel(logging.DEBUG)

    logging.info("listening to http://127.0.0.1:7790")
    logging.info("wsdl is at: http://localhost:7790/?wsdl")

    wsgi_app = wsgi_soap_application([STEDeploymentInfo], 'cl.alma.adc.webservice.soap')
    server = make_server('127.0.0.1', 7790, wsgi_app)
    server.serve_forever()
