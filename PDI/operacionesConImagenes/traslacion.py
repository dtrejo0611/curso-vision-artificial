# -*- coding: utf-8 -*-
"""
Created on Thu Mar 13 12:15:02 2025

@author: dtrej
"""

import numpy as np
import cv2

img = cv2.imread("1.jpeg")
img2 = cv2.resize(img, (100,50)) #Se redimenciona la imagen

alto, largo, canales = img2.shape

#Se definen la cantidad de pixeles a trasladar
tx = 5 #Traslacion en x de 10px
ty = 5 #Traslacion en y de 2px

#Se crea la matriz de traslacion
mT = np.array(([1, 0, tx], [0, 1, ty], [0, 0, 1]), np.uint8)

#Se crea una imagen obscura para colocar la traslacion
imgT = np.zeros((alto + ty, largo + tx, canales), np.uint8)

for i in range(alto):
    for j in range(largo):
        px = np.array(([j, i, 1]), np.uint8) #Guardamos el vector posicion
        dot = np.dot(mT, px) #Obtenemos el producto punto de la matriz de transformacion con el vector px
        x = dot[0]
        y = dot[1]
        imgT[y, x] = img2[i, j]#Reemplazamos los valores de los pixeles
        
#Forma sencilla de hacer lo mismo:
mTS = np.float32([[1, 0, tx], [0, 1, ty]])
imgTS = cv2.warpAffine(img2, mTS, (largo, alto))
        
cv2.namedWindow("Original", cv2.WINDOW_NORMAL)
cv2.namedWindow("Trasladada", cv2.WINDOW_NORMAL)
cv2.namedWindow("Trasladada 2", cv2.WINDOW_NORMAL)

cv2.imshow("Original", img2)
cv2.imshow("Trasladada", imgT)
cv2.imshow("Trasladada 2", imgTS)

cv2.waitKey()
cv2.destroyAllWindows()

