# -*- coding: utf-8 -*-
"""
Created on Thu Aug 28 15:35:39 2025

@author: dtrej
"""

#Multiprocesos

import multiprocessing
import time

def algo():
    print("Inicio proceso")
    time.sleep(5)
    print("Finaliza proceso")
    
    
if __name__ == '__main__':
    proceso = multiprocessing.Process(target=algo)
    proceso.start()
    print("Finalziza proceso padre")