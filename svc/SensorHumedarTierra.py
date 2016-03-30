'''
Created on 22-03-2016

@author: esanchez
'''

import random
from svc import SessionFactory
from time import localtime, strftime
import RPi.GPIO as GPIO   #Importamos las librerias necesarias para usar los pines GPIO
from libs.log import log

class Higrometro():

    def capturarDatos(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(17, GPIO.IN)
        valor = GPIO.input(17)
        estado = "Seco"
        if(valor <= 0.5) :
            estado = "Humedo"
        log.info('Estado Tierra : %s (%d)'%(estado, valor))

        '''lectura = random.uniform(0, 1)
        estado = "Seco"
        valor = 1;
        if(lectura <=0.5) :
            estado = "Humedo"
            valor = 0
        print 'Estado Tierra : %s (%d)'%(estado, valor)
        '''
        self.guardarDatos(valor)
        
    def guardarDatos(self, valor):
        fecha = strftime("%Y-%m-%d %H:%M:%S", localtime())
        query =         "INSERT INTO humedad_tierra (id, estado, fecha) "
        query = query + "VALUES (NULL, '%d', '%s')" % (valor, fecha)
        SessionFactory.run(query)        