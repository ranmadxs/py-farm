'''
Created on 22-03-2016

@author: esanchez
'''

import random
from svc import SessionFactory
from time import localtime, strftime
from libs.log import log
import serial, time, json
from libs.log import log

class Higrometro():

    def capturarDatos(self):
        arduino = serial.Serial('/dev/ttyUSB0', 9600)
        arduino.write("0YL69")
        time.sleep(2)
        #Esto lee todas la lineas
        msg = arduino.read(arduino.inWaiting())
        log.info(msg)
        objs = json.loads(msg)
        #humedad = -1 * (obj["ao"] / 1023) * 100 + 100
        for obj in objs:
            humedad = -1 * (float(obj["ao"]) / float(1023)) * 100 + 100
            sensor = "%d, %d"%( obj["dpin"],  obj["apin"])
            humedadStr = "Humedad Tierra={0:0.1f}%".format(humedad)
            log.debug("%s en sensor %s" % (humedadStr, sensor))            
            self.guardarDatos(obj, humedad)
        
    def guardarDatos(self, obj, humedad):
        fecha = strftime("%Y-%m-%d %H:%M:%S", localtime())
        query =         "INSERT INTO humedad_tierra (id, estado, fecha, ao, do, apin, dpin, humedad) "
        query = query + "VALUES (NULL, '%s', '%s', %d, %d, %d, %d, %f)" % (obj["desc"], fecha, obj["ao"], obj["do"], obj["apin"], obj["dpin"], humedad)
        SessionFactory.run(query)  
        