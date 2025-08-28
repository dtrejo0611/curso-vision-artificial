# -*- coding: utf-8 -*-
"""
Created on Thu Aug 28 14:59:43 2025

@author: dtrej
"""

#Reutilizacion de hilos

import threading
import time
from concurrent.futures import ThreadPoolExecutor
from threading import current_thread
from concurrent.futures import as_completed

# def suma(a,b):
#     time.sleep(0.1)
#     thread = current_thread()
#     print(thread.name)
#     print(a+b, "\n")
    
# executor = ThreadPoolExecutor(max_workers=4)
# executor.submit(suma, 15,37)
# executor.submit(suma, 4,9)
# executor.submit(suma, 5,7)
# executor.submit(suma, 1,6)
    

def suma(datos):
    time.sleep(1)
    return datos[0]+datos[1]

ex = ThreadPoolExecutor(max_workers=4)
lista = [(2,3), (5,2), (8,6), (9,5)]
# lFuturos = [ex.submit(suma, a,b) for a,b in lista] #Opcion 1
lFuturos = ex.map(suma, lista)

for valor in lFuturos:
    print(valor)
    
    