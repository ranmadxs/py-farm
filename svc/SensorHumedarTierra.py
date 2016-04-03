'''
Created on 22-03-2016

@author: esanchez
'''

from svc import SessionFactory
from time import localtime, strftime
from libs.log import log
import serial, time, json


class Higrometro():
    arduino = None
    
    def __init__(self):
        self.arduino = serial.Serial('/dev/ttyUSB0', 9600)
        log.info("Iniciando Arduino Serial")
        continuar = True
        while continuar:
            comando = raw_input('Introduce un comando: ') #Input
            if comando == 'exit':
                continuar = False

        self.arduino.close() #Finalizamos la comunicacio

    def capturarDatos(self):
        self.arduino.write("0YL69")
        time.sleep(2)
        #Esto lee todas la lineas
        msg = self.arduino.read(self.arduino.inWaiting())
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
        