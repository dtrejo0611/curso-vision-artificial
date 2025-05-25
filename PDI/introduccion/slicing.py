# -*- coding: utf-8 -*-
"""
Created on Wed Mar 12 19:53:10 2025

@author: dtrej
"""

import cv2
import numpy as np

img = cv2.imread("candados.jpg") #leemos imagen y guardamos

alto, largo, _ = img.shape #obtenemos las dimensiones de la imagen

print(alto, largo)

candado1 = img[:, 0:int(largo/2)]
candado2 = img[:, int(largo/2):]

img2 = np.zeros((alto, largo, 3), np.uint8) 

img2[:, 0:int(largo/2)] = candado2
img2[:, int(largo/2):] = candado1

cv2.namedWindow("Imagen original", cv2.WINDOW_NORMAL)
cv2.namedWindow("Imagen cambiada", cv2.WINDOW_NORMAL)
cv2.namedWindow("candado1", cv2.WINDOW_NORMAL)
cv2.namedWindow("candado2", cv2.WINDOW_NORMAL)

cv2.imshow("Imagen original", img)
cv2.imshow("Imagen cambiada", img2)
cv2.imshow("candado1", candado1)
cv2.imshow("candado2", candado2)

cv2.waitKey()

cv2.destroyAllWindows()