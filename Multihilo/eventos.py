# -*- coding: utf-8 -*-
"""
Created on Thu Aug 28 14:33:56 2025

@author: dtrej
"""

#Eventos

import threading
import time

# def ciclar(evento1, evento2):
#     while not evento2.is_set():
#         print("Ciclo while")
#         evento1.wait() #Permite pausar la ejecucion del ciclo while que sucede dentro del hilo

# evento1 = threading.Event()
# evento2 = threading.Event()

# hilo = threading.Thread(target=ciclar, args=(evento1, evento2))
# hilo.start()

# for i in range(5):
#     time.sleep(0.5)
#     print("Realizando ciclo for")

# evento1.set() #Reanuda el hilo
# time.sleep(1)
# evento2.set()

## Iteracion entre dos ciclos while

# def ciclar1(evento1, evento3):
#     while not evento3.is_set():
#         evento1.wait()
#         print("Nuevo ciclo while 1")
#         evento1.clear()
#         time.sleep(0.1)
        
# def ciclar2(evento2, evento3):
#     while not evento3.is_set():
#         evento2.wait()
#         print("Nuevo ciclo while 2")
#         evento2.clear()
#         time.sleep(0.1)


# evento1 = threading.Event()
# evento2 = threading.Event()
# evento3 = threading.Event()

# hilo1 = threading.Thread(target=ciclar1, args=(evento1, evento3))
# hilo2 = threading.Thread(target=ciclar2, args=(evento2, evento3))

# hilo1.start()
# hilo2.start()

# for i in range(5):
#     evento1.set()
#     time.sleep(0.1)
#     evento2.set()
#     time.sleep(0.1)
    
# evento3.set()


# Time out

def ciclar(evento1):
    print("esperando")
    resp = evento1.wait(timeout=10)
    if resp == True:
        print("liberado por señal")
    else:
        print("nunca llego la señal")
    
evento1 = threading.Event()

hilo = threading.Thread(target=ciclar, args=(evento1,))
hilo.start()

print("Esperando para enviar la señal")

time.sleep(3)
# evento1.set()
time.sleep(0.1)


