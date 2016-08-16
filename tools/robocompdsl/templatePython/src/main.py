#!/usr/bin/env python
# -*- coding: utf-8 -*-
[[[cog

import sys
sys.path.append('/opt/robocomp/python')

import cog
def A():
	cog.out('<@@<')
def Z():
	cog.out('>@@>')
def TAB():
	cog.out('<TABHERE>')

from parseCDSL import *
component = CDSLParsing.fromFile(theCDSL)


REQUIRE_STR = """
<TABHERE><TABHERE># Remote object connection for <NORMAL>
<TABHERE><TABHERE>try:
<TABHERE><TABHERE><TABHERE>proxyString = ic.getProperties().getProperty('<NORMAL>Proxy')
<TABHERE><TABHERE><TABHERE>try:
<TABHERE><TABHERE><TABHERE><TABHERE>basePrx = ic.stringToProxy(proxyString)
<TABHERE><TABHERE><TABHERE><TABHERE><LOWER>_proxy = RoboComp<NORMAL>.<NORMAL>Prx.checkedCast(basePrx)
<TABHERE><TABHERE><TABHERE><TABHERE>mprx["<NORMAL>Proxy"] = <LOWER>_proxy
<TABHERE><TABHERE><TABHERE>except Ice.Exception:
<TABHERE><TABHERE><TABHERE><TABHERE>print 'Cannot connect to the remote object (<NORMAL>)', proxyString
<TABHERE><TABHERE><TABHERE><TABHERE>#traceback.print_exc()
<TABHERE><TABHERE><TABHERE><TABHERE>status = 1
<TABHERE><TABHERE>except Ice.Exception, e:
<TABHERE><TABHERE><TABHERE>print e
<TABHERE><TABHERE><TABHERE>print 'Cannot get <NORMAL>Proxy property.'
<TABHERE><TABHERE><TABHERE>status = 1
"""

<TABHERE><TABHERE># Remote object connection for <NORMALx>
<TABHERE><TABHERE>proxyData["<NORMALx>"] = {"comp":"COMP NAME HERE","caster":RoboComp<NORMAL>.<NORMAL>Prx.checkedCast,"name":"<NORMAL>"}
<TABHERE><TABHERE>try:
<TABHERE><TABHERE><TABHERE>while True:
<TABHERE><TABHERE><TABHERE><TABHERE>try:
<TABHERE><TABHERE><TABHERE><TABHERE><TABHERE>port = rcmaster_proxy.getComPort(proxyData["<NORMALx>"]["comp"],"localhost");
<TABHERE><TABHERE><TABHERE><TABHERE><TABHERE>basePrx = ic.stringToProxy(proxyData["<NORMALx>"]["name"]+":tcp -h localhost -p "+str(port))
<TABHERE><TABHERE><TABHERE><TABHERE><TABHERE><NORMAL>_proxy = proxyData["<NORMALx>"]["caster"](basePrx)
<TABHERE><TABHERE><TABHERE><TABHERE><TABHERE>proxyData["<NORMALx>"]["proxy"] = <NORMAL>_proxy
<TABHERE><TABHERE><TABHERE><TABHERE>except RoboCompRCMaster.ComponentNotFound:
<TABHERE><TABHERE><TABHERE><TABHERE><TABHERE>print 'waiting for <NORMALx> interface'
<TABHERE><TABHERE><TABHERE><TABHERE><TABHERE>time.sleep(3)
<TABHERE><TABHERE><TABHERE><TABHERE>except Ice.Exception:
<TABHERE><TABHERE><TABHERE><TABHERE><TABHERE>print 'Cannot connect to the remote object (<NORMAL>)'
<TABHERE><TABHERE><TABHERE><TABHERE><TABHERE>traceback.print_exc()
<TABHERE><TABHERE><TABHERE><TABHERE><TABHERE>status = 1
<TABHERE><TABHERE><TABHERE><TABHERE>else:
<TABHERE><TABHERE><TABHERE><TABHERE><TABHERE>break
<TABHERE><TABHERE>except Ice.Exception, e:
<TABHERE><TABHERE><TABHERE>print e
<TABHERE><TABHERE><TABHERE>print 'Cannot get <NORMAL>Proxy property.'
<TABHERE><TABHERE><TABHERE>status = 1



REQUIRE_STR_RCMASTER="""
<TABHERE><TABHERE># Remote object connection for rcmaster
<TABHERE><TABHERE>proxyData["rcmaster"] = {"comp":"rcmaster","caster":RoboCompRCMaster.rcmasterPrx.checkedCast,"name":"rcmaster"}
<TABHERE><TABHERE>try:
<TABHERE><TABHERE><TABHERE>with open(os.path.join(os.path.expanduser('~'), ".config/RoboComp/rcmaster.config"), 'r') as f:
<TABHERE><TABHERE><TABHERE><TABHERE>rcmaster_uri = f.readline().strip().split(":")
<TABHERE><TABHERE><TABHERE>basePrx = ic.stringToProxy("rcmaster:tcp -h "+rcmaster_uri[0]+" -p "+rcmaster_uri[1])
<TABHERE><TABHERE><TABHERE>try:
<TABHERE><TABHERE><TABHERE><TABHERE>print "Connecting to rcmaster " ,rcmaster_uri
<TABHERE><TABHERE><TABHERE><TABHERE>rcmaster_proxy = RoboCompRCMaster.rcmasterPrx.checkedCast(basePrx)
<TABHERE><TABHERE><TABHERE>except Ice.SocketException:
<TABHERE><TABHERE><TABHERE><TABHERE>raise Exception("RCMaster is not running")
<TABHERE><TABHERE><TABHERE>proxyData["rcmaster"]["proxy"] = rcmaster_proxy
<TABHERE><TABHERE>except Ice.Exception:
<TABHERE><TABHERE><TABHERE>print 'Cannot connect to the remote object (rcmaster)'
<TABHERE><TABHERE><TABHERE>traceback.print_exc()
<TABHERE><TABHERE><TABHERE>status = 1

"""

SUBSCRIBESTO_STR = """
<TABHERE><TABHERE><NORMAL>_adapter = ic.createObjectAdapter("<NORMAL>Topic")
<TABHERE><TABHERE><LOWER>I_ = <NORMAL>I(worker)
<TABHERE><TABHERE><LOWER>_proxy = <NORMAL>_adapter.addWithUUID(<LOWER>I_).ice_oneway()

<TABHERE><TABHERE>subscribeDone = False
<TABHERE><TABHERE>while not subscribeDone:
<TABHERE><TABHERE><TABHERE>try:
<TABHERE><TABHERE><TABHERE><TABHERE><LOWER>_topic = topicManager.retrieve("<NORMAL>")
<TABHERE><TABHERE><TABHERE><TABHERE>subscribeDone = True
<TABHERE><TABHERE><TABHERE>except Ice.Exception, e:
<TABHERE><TABHERE><TABHERE><TABHERE>print "Error. Topic does not exist (yet)"
<TABHERE><TABHERE><TABHERE><TABHERE>status = 0
<TABHERE><TABHERE><TABHERE><TABHERE>time.sleep(1)
<TABHERE><TABHERE>qos = {}
<TABHERE><TABHERE><LOWER>_topic.subscribeAndGetPublisher(qos, <LOWER>_proxy)
<TABHERE><TABHERE><NORMAL>_adapter.activate()
"""

PUBLISHES_STR = """
<TABHERE><TABHERE># Create a proxy to publish a <NORMAL> topic
<TABHERE><TABHERE>topic = False
<TABHERE><TABHERE>try:
<TABHERE><TABHERE><TABHERE>topic = topicManager.retrieve("<NORMAL>")
<TABHERE><TABHERE>except:
<TABHERE><TABHERE><TABHERE>pass
<TABHERE><TABHERE>while not topic:
<TABHERE><TABHERE><TABHERE>try:
<TABHERE><TABHERE><TABHERE><TABHERE>topic = topicManager.retrieve("<NORMAL>")
<TABHERE><TABHERE><TABHERE>except IceStorm.NoSuchTopic:
<TABHERE><TABHERE><TABHERE><TABHERE>try:
<TABHERE><TABHERE><TABHERE><TABHERE><TABHERE>topic = topicManager.create("<NORMAL>")
<TABHERE><TABHERE><TABHERE><TABHERE>except:
<TABHERE><TABHERE><TABHERE><TABHERE><TABHERE>print 'Another client created the <NORMAL> topic? ...'
<TABHERE><TABHERE>pub = topic.getPublisher().ice_oneway()
<TABHERE><TABHERE><LOWER>Topic = <NORMAL>Prx.uncheckedCast(pub)
<TABHERE><TABHERE>mprx["<NORMAL>Pub"] = <LOWER>Topic
"""

IMPLEMENTS_STR = """compInfo.interfaces.append(RoboCompRCMaster.interfaceData("<NORMAL>"))"""

]]]
[[[end]]]

#
# Copyright (C)
[[[cog
A()
import datetime
cog.out(' '+str(datetime.date.today().year))
Z()
]]]
[[[end]]]
 by YOUR NAME HERE
#
#    This file is part of RoboComp
#
#    RoboComp is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    RoboComp is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with RoboComp.  If not, see <http://www.gnu.org/licenses/>.
#

# \mainpage RoboComp::
[[[cog
A()
cog.out(component['name'])
]]]
[[[end]]]
#
# \section intro_sec Introduction
#
# Some information about the component...
#
# \section interface_sec Interface
#
# Descroption of the interface provided...
#
# \section install_sec Installation
#
# \subsection install1_ssec Software depencences
# Software dependences....
#
# \subsection install2_ssec Compile and install
# How to compile/install the component...
#
# \section guide_sec User guide
#
# \subsection config_ssec Configuration file
#
# <p>
# The configuration file...
# </p>
#
# \subsection execution_ssec Execution
#
# Just: "${PATH_TO_BINARY}/
[[[cog
A()
cog.out(component['name'])
Z()
]]]
[[[end]]]
 --Ice.Config=${PATH_TO_CONFIG_FILE}"
#
# \subsection running_ssec Once running
#
#
#

import sys, traceback, Ice, IceStorm, subprocess, threading, time, Queue, os, copy

# Ctrl+c handling
import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PySide import *

from specificworker import *

ROBOCOMP = ''
try:
	ROBOCOMP = os.environ['ROBOCOMP']
except:
	print '$ROBOCOMP environment variable not set, using the default value /opt/robocomp'
	ROBOCOMP = '/opt/robocomp'
if len(ROBOCOMP)<1:
	print 'ROBOCOMP environment variable not set! Exiting.'
	sys.exit()


preStr = "-I"+ROBOCOMP+"/interfaces/ -I/opt/robocomp/interfaces/ --all "+ROBOCOMP+"/interfaces/"
Ice.loadSlice(preStr+"CommonBehavior.ice")
import RoboCompCommonBehavior
[[[cog
for imp in component['imports']:
	module = IDSLParsing.gimmeIDSL(imp.split('/')[-1])
	incl = imp.split('/')[-1].split('.')[0]
	cog.outl('Ice.loadSlice(preStr+"'+incl+'.ice")')
	cog.outl('import '+module['name']+'')
]]]
[[[end]]]


class CommonBehaviorI(RoboCompCommonBehavior.CommonBehavior):
	def __init__(self, _handler, _communicator):
		self.handler = _handler
		self.communicator = _communicator
	def getFreq(self, current = None):
		self.handler.getFreq()
	def setFreq(self, freq, current = None):
		self.handler.setFreq()
	def timeAwake(self, current = None):
		try:
			return self.handler.timeAwake()
		except:
			print 'Problem getting timeAwake'
	def killYourSelf(self, current = None):
		self.handler.killYourSelf()
	def getAttrList(self, current = None):
		try:
			return self.handler.getAttrList(self.communicator)
		except:
			print 'Problem getting getAttrList'
			traceback.print_exc()
			status = 1
			return



if __name__ == '__main__':
[[[cog
	if component['gui'] != "none":
		cog.outl('<TABHERE>app = QtGui.QApplication(sys.argv)')
	else:
		cog.outl('<TABHERE>app = QtCore.QCoreApplication(sys.argv)')
]]]
[[[end]]]
	params = copy.deepcopy(sys.argv)
	if len(params) > 1:
		if not params[1].startswith('--Ice.Config='):
			params[1] = '--Ice.Config=' + params[1]
	elif len(params) == 1:
		params.append('--Ice.Config=config')
	ic = Ice.initialize(params)
	status = 0
	mprx = {}
    mprx["name"] = ic.getProperties().getProperty('Ice.ProgramName');
    proxyData = {}

[[[cog
if len(component['requires']) > 0 or len(component['publishes']) > 0 or len(component['subscribesTo']) > 0:
	cog.outl('<TABHERE>try:')
icount = dict()
for rqa in component['requires']:
	if type(rqa) == type(''):
		rq = rqa
	else:
		rq = rqa[0]
	if rq in icount:
		icount[rq] = icount[rq] + 1
		rqx = rq + str(icount[rq])
	else:
		icount[rq] = 0
		rqx = rq
	if rq.lower() == "rcmaster":
		w = REQUIRE_STR_RCMASTER
	else:
		w = REQUIRE_STR.replace("<NORMAL>", rq).replace("<NORMALx>", rqx).replace("<LOWER>", rq.lower())
	cog.outl(w)

try:
	if len(component['publishes']) > 0 or len(component['subscribesTo']) > 0:
		cog.outl("""
<TABHERE><TABHERE># Topic Manager
<TABHERE><TABHERE>proxy = ic.getProperties().getProperty("TopicManager.Proxy")
<TABHERE><TABHERE>obj = ic.stringToProxy(proxy)
<TABHERE><TABHERE>topicManager = IceStorm.TopicManagerPrx.checkedCast(obj)""")
except:
	pass

for pba in component['publishes']:
	if type(pba) == type(''):
		pb = pba
	else:
		pb = pba[0]
	w = PUBLISHES_STR.replace("<NORMAL>", pb).replace("<LOWER>", pb.lower())
	cog.outl(w)

if len(component['requires']) > 0 or len(component['publishes']) > 0 or len(component['subscribesTo']) > 0:
	cog.outl("""<TABHERE>except:
		<TABHERE>traceback.print_exc()
		<TABHERE>status = 1""")
]]]
[[[end]]]


	if status == 0:
		mprx["proxyData"] = proxyData
		worker = SpecificWorker(mprx)
		compInfo = RoboCompRCMaster.compData(name=mprx["name"])
        compInfo.interfaces = []
        
[[[cog
for ima in component['implements']:
	if type(ima) == type(''):
		im = ima
	else:
		im = ima[0]
	w = IMPLEMENTS_STR.replace("<NORMAL>", im).replace("<LOWER>", im.lower())
	cog.outl(w)
	cog.outl("""<TABHERE><TABHERE>idata = rcmaster_proxy.registerComp(compInfo,False,True)""");
]]]
[[[end]]]

        # activate all interfaces
        for iface in idata:
            adapter = ic.createObjectAdapterWithEndpoints(iface.name, iface.protocol+' -h localhost -p '+str(iface.port))
            workerObj = globals()[str(iface.name)+'I'](worker)
            adapter.add(workerObj, ic.stringToIdentity(str(iface.name).lower()))
            adapter.activate()
            print "activated interface :", iface

[[[cog
for st in component['subscribesTo']:
	w = SUBSCRIBESTO_STR.replace("<NORMAL>", st).replace("<LOWER>", st.lower())
	cog.outl(w)
]]]
[[[end]]]

#<TABHERE><TABHERE>adapter.add(CommonBehaviorI(<LOWER>I, ic), ic.stringToIdentity('commonbehavior'))

		app.exec_()

	if ic:
		try:
			ic.destroy()
		except:
			traceback.print_exc()
			status = 1
