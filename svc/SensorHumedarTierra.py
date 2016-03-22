'''
Created on 22-03-2016

@author: esanchez
'''

import random

class Higrometro():

    def capturarDatos(self):
        lectura = random.uniform(0, 1)
        estado = "Seco"
        valor = 1;
        if(lectura <=0.5) :
            estado = "Humedo"
            valor = 0
        print 'Estado Tierra : %s (%d)'%(estado, valor)