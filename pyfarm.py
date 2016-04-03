#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 22-03-2016

@author: esanchez
'''
import serial
import threading
import time
from svc import SensorHumedarTierra, Camera, SessionFactory, SensorTemperatura, SensorLuz
from os import path
from libs.log import log

SECONDS_X_HOUR = 3600


def threadStart(rango, sensor, tiempo):
    for x in range(0, rango):
        sensor.capturarDatos()
        time.sleep(tiempo)
        
def initArduino():
    serial.Serial('/dev/ttyUSB0', 9600)       
    continuar = True
    while continuar:
        None
        time.sleep(100)
 
        
def start():
    #t0 = threading.Thread(target=initArduino, name='WorkerInitArduino')
    #t0.start()
    
    t1 = threading.Thread(target=threadStart, args = (500, SensorTemperatura.DHT11(), SECONDS_X_HOUR * 1), name='WorkerSensorTemperatura')
    t1.start()

    time.sleep(2)

    t2 = threading.Thread(target=threadStart, args = (500, SensorHumedarTierra.Higrometro(), SECONDS_X_HOUR * 1), name='WorkerSensorHumedadTierra')
    t2.start()

    time.sleep(2)

    t3 = threading.Thread(target=threadStart, args = (500, SensorLuz.LM393(), SECONDS_X_HOUR * 1), name='WorkerSensorLuz')
    t3.start()
    
    #t4 = threading.Thread(target=threadStart, args = (2, Camera.WebCam(), SECONDS_X_HOUR * 12), name='WorkerCamera')
    #t4.start()

log.info('>> Inicio pyfarm <<')
file_path = path.relpath("resources/basic_data.sql")

SessionFactory.init(file_path)
start()
