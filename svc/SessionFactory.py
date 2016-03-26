# -*- coding: utf-8 -*-
'''
Created on 23-03-2016

@author: esanchez
'''
import MySQLdb
import config

def run(query=''):     
 
    conn = MySQLdb.connect(*config.datosDB) # Conectar a la base de datos 
    cursor = conn.cursor()         # Crear un cursor 
    cursor.execute(query)          # Ejecutar una consulta 
 
    if query.upper().startswith('SELECT'): 
        data = cursor.fetchall()   # Traer los resultados de un select 
    else: 
        conn.commit()              # Hacer efectiva la escritura de datos 
        data = None 
 
    cursor.close()                 # Cerrar el cursor 
    conn.close()                   # Cerrar la conexion 
 
    return data

def init(file_path):
    print ("SessionFactory init data base")
    query = ""
    with open(file_path) as f:
        for line in f:
            query = query + line + " "
    #print query
    try:
        conn = MySQLdb.connect(*config.datosDB)
        cursor = conn.cursor()
        cursor.execute(query) 
        conn.commit()
        cursor.close()    
        conn.close()
    except: # catch *all* exceptions
        None