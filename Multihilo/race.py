# -*- coding: utf-8 -*-
"""
Created on Wed Aug 27 14:20:48 2025

@author: dtrej
"""

import time
import threading

lock = threading.Lock() #Permite bloquear una variable por si se interactua en 2 hilos
                        #distintos al mismo tiempo no genere errores

a = 0

def sumar():
    global a
    for i in range(0,1000000):
        with lock:
            a += 1
        
def restar():
    global a
    for i in range(0,1000000):
        with lock:
            a -= 1
        
hilo1 = threading.Thread(target=sumar)
hilo2 = threading.Thread(target=restar)

hilo1.start()
hilo2.start()
hilo1.join()
hilo2.join()

print(a)