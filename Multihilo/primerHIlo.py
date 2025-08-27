# -*- coding: utf-8 -*-
"""
Created on Wed Aug 27 13:37:36 2025

@author: dtrej
"""

import time
import threading

# def imprimirValor():
#     time.sleep(0.3)
#     print("Hola mundo")
    
# Ejecucion secuencial
# for i in range(15):
#     imprimirValor()

#Ejecucion concurrente

# for i in range(15):
#     hilo = threading.Thread(target=imprimirValor)
#     hilo.start()

# def imprimir1():
#     time.sleep(0.3)
#     print("Ejecutandro hilo 1")
    

# def imprimir2():
#     time.sleep(0.3)
#     print("Ejecutandro hilo 2")

# def imprimir3():
#     time.sleep(0.3)
#     print("Ejecutandro hilo 3")


# hilo1 = threading.Thread(target=imprimir1)
# hilo2 = threading.Thread(target=imprimir2)
# hilo3 = threading.Thread(target=imprimir3)

# hilo1.start()
# hilo2.start()
# hilo3.start()

# def sumar(a,b):
#     print(a+b)
    
# hilo = threading.Thread(target=sumar, args=[3,4])
# hilo.start()

# #Hilo secundario
# def dormir():
#     time.sleep(5)
#     print("Desperté")
    
# hilo = threading.Thread(target=dormir)
# hilo.start()

# #Hilo principal
# for i in range(500):
#     time.sleep(0.01)
#     print(i)

# def prueba1():
#     time.sleep(3)
#     return 5

# def prueba2():
#     time.sleep(2.5)
#     return 3

# def prueba3():
#     time.sleep(1)
#     return 8

# x = prueba1()
# y = prueba2()
# z = prueba3()

# if x == 5 and y == 3 and z == 8:
#     print("Resultado ok")
# else:
#     print("resultado malo")


def prueba1():
    global x
    time.sleep(3)
    x = 5
    print("Terminada 1")

def prueba2():
    global y
    time.sleep(2.5)
    y = 3
    print("Terminada 2")

def prueba3():
    global z
    time.sleep(1)
    z = 8
    print("Terminada 3")

x = 0
y = 0
z = 0

hilo1 = threading.Thread(target=prueba1) #Si coloco los parentecis de las funciones primero ejecuta toda la funcion
hilo2 = threading.Thread(target=prueba2) #eso provoca que no se comporte como deberia
hilo3 = threading.Thread(target=prueba3)

hilo1.start()
hilo2.start()
hilo3.start()

hilo1.join()
hilo2.join()
hilo3.join()

if x == 5 and y == 3 and z == 8:
    print("Resultado ok")
else:
    print("resultado malo")