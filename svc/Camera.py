'''
Created on 22-03-2016

@author: esanchez
'''
import pygame.camera
import pygame.image
from time import gmtime, strftime
import os

FOLDER_WEBCAM = '/tmp/motion/'
PIC_WIDTH = 352
PIC_HEIGHT = 288

class WebCam():
    def capturarDatos(self):
        if not os.path.exists(FOLDER_WEBCAM):
            os.makedirs(FOLDER_WEBCAM)        
        pygame.camera.init()
        cameras = pygame.camera.list_cameras()
        print "Usando camara %s ..." % cameras[0]
        webcam = pygame.camera.Camera(cameras[0], (PIC_WIDTH, PIC_HEIGHT))
        webcam.start()
        image= webcam.get_image()
        fileTime = strftime("%Y-%m-%d %H:%M:%S", gmtime())
        fileName = '%spic %s.jpg'%(FOLDER_WEBCAM, fileTime)
        print 'Guardando imagen %s'%fileName
        pygame.image.save(image, fileName)
        webcam.stop()