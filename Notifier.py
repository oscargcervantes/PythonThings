#!/usr/bin/env python
import pyinotify
import os
import threading
import thread
import time
from threading import *

class EventHandler(pyinotify.ProcessEvent):
	def process_IN_CREATE(self,event):
		if os.path.isfile(event.pathname):
			print 'Se ha creado el archivo ' + event.pathname

	def process_IN_DELETE(self,event):
		#if os.path.isfile(event.pathname):
			print 'Se ha eliminado el archivo ' + event.pathname


class Notifier(threading.Thread):
    def __init__(self, ThreadID, name, path):
        threading.Thread.__init__(self)
        #super(Notifier, self).__init__()
        self.path = path
        self.name = name
        self.ThreadID = ThreadID
        self.stoprequest = threading.Event()
    
    def run(self):
        print "Starting " + self.name
        self.watch()
              
    def watch(self):
        #try:
            wm = pyinotify.WatchManager() # Administrador de vigilancia
            mask = pyinotify.IN_DELETE | pyinotify.IN_CREATE  # Eventos a monitorear
            ev = EventHandler()
            notifier = pyinotify.Notifier(wm, ev)   # Crea el notificador para que llame la case EventHandler cuando suceda el evento
            wdd = wm.add_watch(self.path, mask, rec=True)   # Carga los eventos y el directorio a monitorear   
            print 'Listening folder: ' + self.path
            #while not self.stoprequest.isSet():
            notifier.loop()       # Bucle infinito de monitoreo. En de querer continuar con el programa se puede ejecutar esta accion con un hilo.
        #except (KeyboardInterrupt,SystemExit):
            #sys.exit('\n!!!Interrupcion de teclado recibida, cerrando aplicacion.\n') # Al presionar Crtl+C
     
    def stop(self):
        print "Ending " + self.name
        thread.exit()
        #notifier.stop()
    
    #def join(self, timeout=None):
        #self.stoprequest.set()
        #super(Notifier, self).join(timeout)
