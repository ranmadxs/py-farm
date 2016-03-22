'''
Created on 22-03-2016

@author: esanchez
'''

import threading
import time
from svc import SensorTemperatura, SensorHumedarTierra

def threadStart(rango, sensor, tiempo):
    for x in range(0, rango):
        sensor.capturarDatos()
        time.sleep(tiempo)
        
def start():
    
    t1 = threading.Thread(target=threadStart, args = (15, SensorTemperatura.DHT11(), 1), name='WorkerSensorTemperatura')
    t1.start()

    t2 = threading.Thread(target=threadStart, args = (10, SensorHumedarTierra.Higrometro(), 5), name='WorkerSensorTemperatura')
    t2.start()
    
    
print ("pyfarm init")
start()