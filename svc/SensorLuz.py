'''
Created on 02-04-2016

@author: esanchez
'''
import RPi.GPIO as GPIO
from time import localtime, strftime
from svc import SessionFactory
from libs.log import log

class LM393():
    
    GPIO_PIN = 17

    def capturarDatos(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.GPIO_PIN, GPIO.IN)
        valor = GPIO.input(self.GPIO_PIN)
        estado = "Luz"
        if(valor <= 0.5) :
            estado = "Oscuridad"
        log.debug( '%s (%d)'%(estado, valor))
        self.guardarDatos(valor)

    def guardarDatos(self, valor):
        fecha = strftime("%Y-%m-%d %H:%M:%S", localtime())
        query =         "INSERT INTO luz (id, estado, fecha) "
        query = query + "VALUES (NULL, '%d', '%s')" % (valor, fecha)
        SessionFactory.run(query) 