# -*- coding: utf-8 -*-
"""
Created on Thu Mar 13 20:26:03 2025

@author: dtrej
"""

import cv2
from matplotlib import pyplot as plt
import numpy as np

img = cv2.imread("lena.png") 

color = ('b', 'g', 'r')

for i, col in enumerate(color): #Recorremos la variable color y con funcion enumerate
#obtendriamos cada espacio de la tupla enumerado, se obtendria lo siguiente: 0 b 1 g 2 r
    print(i, col)    
    hist = cv2.calcHist([img], [i], None, [256], [0, 255])
    
    plt.plot(hist, color = col) #Graficamos el histograma por color
    plt.xlim([0, 256])

plt.show()
    