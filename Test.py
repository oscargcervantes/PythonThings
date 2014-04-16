#!/usr/bin/env python

from PDF import PDF
from Index import Index
from Search import Reader
from Text import Text 
from Dir_Reader import Dir_Reader
from Notifier import Notifier
from ServerThread2 import Server
import os
import time
import sys


p = PDF("/home/oscargcervantes/Desktop/TACS.pdf")
lectura = p.read()
print lectura
ch = p.check()
print ch

t = Text("/home/oscargcervantes/Issues_Servers/AIX 5.3 Upgrades")
rd = t.read()
print rd

r = Dir_Reader("/home/oscargcervantes/Issues_Servers")
files_found = r.read()
print files_found

time.sleep(5)

#Notifier Threads
n = Notifier("1","Thread-1","/home/oscargcervantes/Issues_Servers")
#n.setDaemon(True)
n.start()

m = Notifier("2","Thread-2","/home/oscargcervantes/CourseInformation")
#m.setDaemon(True)
m.start()

time.sleep(5)

m._Thread__stop()
n._Thread__stop()

print "Ending Main Process"

from ODSReader import *
doc = ODSReader("/home/oscargcervantes/Issues_Servers/Servers_List/Servers_dstadmin_Access.ods")
table = doc.getSheet("Sheet1")
firstRow = table[0]
firstCellOfFirstRow = firstRow[0]
print table
print firstRow
print firstCellOfFirstRow

#print files_found

#try:
#    while(True):
        #pass
#        print n.name + " %s" %n.isAlive()
#        print m.name + " %s" %m.isAlive()

#except (KeyboardInterrupt,SystemExit):
#    for thread in enumerate():
#        if thread.isAlive():
#           try:
#               thread.stop()
#               thread.join()
#               thread._Thread__stop()
#           except:
#               print(str(thread.getName()) + ' could not be terminated')
    #sys.exit and thread.exit are equivalent
    #sys.exit('\n!!!Interrupcion de teclado recibida, cerrando aplicacion.\n')
time.sleep(5)
if m.isAlive():
    print "Ending " + m.getName()
    m._Thread__stop()
elif n.isAlive():
    print "Ending " + n.getName()
    n._Thread__stop()

server = Server()
server.run()
print "Terminated"
