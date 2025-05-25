# -*- coding: utf-8 -*-
"""
Created on Thu Mar 13 20:41:57 2025

@author: dtrej
"""

import cv2
from matplotlib import pyplot as plt
import numpy as np

img = cv2.imread("antes.jpg", 0)

equ = cv2.equalizeHist(img) #Realizamos la equalizacion del histograma

res = np.hstack((img, equ)) #Concatenamos la imagen de entrada con la imagen equalizada

cv2.namedWindow("Resultado", cv2.WINDOW_NORMAL)
cv2.imshow("Resultado", res)
cv2.waitKey()
cv2.destroyAllWindows()

histNormal = cv2.calcHist([img], [0], None, [256], [0, 255])
histEqu = cv2.calcHist([equ], [0], None, [256], [0, 255])

hist, bins = np.histogram(img.flatten(), 256, [0, 256]) #Otra forma de calcular el histograma
plt.hist(img.flatten(), 256, [0, 256], color = 'b') #Otra forma de plottear el histograma
plt.xlim([0, 256])

plt.legend('H', loc = 'upper left')
plt.show()

histequ, binsequ = np.histogram(equ.flatten(), 256, [0, 256]) #Otra forma de calcular el histograma
plt.hist(equ.flatten(), 256, [0, 256], color = 'b') #Otra forma de plottear el histograma
plt.xlim([0, 256])

plt.legend('H', loc = 'upper left')
plt.show()

# plt.plot(histNormal), plt.plot(histEqu)

# plt.xlim([0, 255])

# plt.show()