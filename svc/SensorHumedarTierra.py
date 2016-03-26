'''
Created on 22-03-2016

@author: esanchez
'''

import random
from svc import SessionFactory
from time import localtime, strftime

class Higrometro():

    def capturarDatos(self):
        lectura = random.uniform(0, 1)
        estado = "Seco"
        valor = 1;
        if(lectura <=0.5) :
            estado = "Humedo"
            valor = 0
        print 'Estado Tierra : %s (%d)'%(estado, valor)
        self.guardarDatos(valor)
        
    def guardarDatos(self, valor):
        fecha = strftime("%Y-%m-%d %H:%M:%S", localtime())
        query =         "INSERT INTO humedad_tierra (id, estado, fecha) "
        query = query + "VALUES (NULL, '%d', '%s')" % (valor, fecha)
        SessionFactory.run(query)        