# -*- coding: utf-8 -*-
"""
Created on Thu Mar 13 20:56:55 2025

@author: dtrej
"""

import cv2
from matplotlib import pyplot as plt
import numpy as np

img = cv2.imread("aaa.png", 0)

#Creamos la configuracion para el algoritmo CLAHE con un humbral de 1.0 y un 
#kernel de 8x8
clahe = cv2.createCLAHE(clipLimit = 15.0, tileGridSize=(8,8))

clit = clahe.apply(img)
res = np.hstack((img, clit))

cv2.namedWindow("Resultado", cv2.WINDOW_NORMAL)
cv2.imshow("Resultado", res)

cv2.waitKey()
cv2.destroyAllWindows()

histNormal = cv2.calcHist([img], [0], None, [256], [0, 255])
histClit = cv2.calcHist([clit], [0], None, [256], [0, 255])

plt.subplot(211), plt.plot(histNormal)
plt.subplot(212), plt.plot(histClit)

plt.xlim([0, 255])

plt.show()

# hist, bins = np.histogram(img.flatten(), 256, [0, 256]) #Otra forma de calcular el histograma
# plt.hist(img.flatten(), 256, [0, 256], color = 'b') #Otra forma de plottear el histograma
# plt.xlim([0, 256])

# plt.legend('H', loc = 'upper left')
# plt.show()

# histequ, binsequ = np.histogram(clit.flatten(), 256, [0, 256]) #Otra forma de calcular el histograma
# plt.hist(clit.flatten(), 256, [0, 256], color = 'b') #Otra forma de plottear el histograma
# plt.xlim([0, 256])

# plt.legend('H', loc = 'upper left')
# plt.show()
