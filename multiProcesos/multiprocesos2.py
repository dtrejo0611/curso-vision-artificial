# -*- coding: utf-8 -*-
"""
Created on Thu Aug 28 15:47:05 2025

@author: dtrej
"""

#Multiprocesos 2

import multiprocessing
import time

def suma(a,b):
    print("El resultado es: ", a+b)
    
if __name__ == '__main__':
    proceso1 = multiprocessing.Process(target=suma, args=(10,25))
    proceso2 = multiprocessing.Process(target=suma, args=(5,25))
    proceso3 = multiprocessing.Process(target=suma, args=(1,5))
    proceso1.start()
    proceso2.start()
    proceso3.start()