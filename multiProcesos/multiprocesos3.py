# -*- coding: utf-8 -*-
"""
Created on Thu Aug 28 15:52:00 2025

@author: dtrej
"""

#Multiprocesos 3

#Procesos demonios, matar el proceso secundario cuando el proceso padre termine

import multiprocessing
import time

def conteo(cantidad):
    for i in range(cantidad):
        time.sleep(0.5)
        print(i)
        
if __name__ == '__main__':
    proceso = multiprocessing.Process(target=conteo, kwargs={"cantidad":20}, daemon=True)
    proceso.start()
    time.sleep(5)
    print("Finaliza proceso padre")