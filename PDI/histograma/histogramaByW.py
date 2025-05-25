# -*- coding: utf-8 -*-
"""
Created on Thu Mar 13 20:13:09 2025

@author: dtrej
"""

import cv2
from matplotlib import pyplot as plt
import numpy as np

img = cv2.imread("lena.png", 0) #imagen en escala de grises

hist = cv2.calcHist([img], [0], None, [256], [0, 255])

plt.hist(img.ravel(), 256, [0, 255])#Graficamos el histograma, .ravel regresa la matriz en formato plano
#continuo, el siguiente dato es en cuantas artes se divide el grafico, el ultimo dato es el rango de gama

plt.show()


