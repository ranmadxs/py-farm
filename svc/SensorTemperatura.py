'''
Created on 22-03-2016

@author: esanchez
'''
import random

class DHT11():
    
    def capturarDatos(self):
        temperature = random.uniform(0, 100)
        humidity = random.uniform(0, 100)
        print 'Temperatura={0:0.1f}*C  Humedad={1:0.1f}%'.format(temperature, humidity)