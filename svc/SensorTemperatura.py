'''
Created on 22-03-2016

@author: esanchez
'''
import random
from svc import SessionFactory
from time import localtime, strftime

class DHT11():
    
    def capturarDatos(self):
        temperatura = random.uniform(0, 100)
        humedad = random.uniform(0, 100)
        print 'Temperatura={0:0.1f}*C  Humedad={1:0.1f}%'.format(temperatura, humedad)
        self.guardarDatos(temperatura, humedad)
        
    def guardarDatos(self, temperatura, humedad):
        fecha = strftime("%Y-%m-%d %H:%M:%S", localtime())
        query =         "INSERT INTO temperatura (id, temperatura, humedad, fecha) "
        query = query + "VALUES (NULL, '%f', '%f', '%s')" % (temperatura, humedad, fecha)
        SessionFactory.run(query)
        