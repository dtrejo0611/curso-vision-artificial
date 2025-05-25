# -*- coding: utf-8 -*-
"""
Created on Wed Mar 19 14:51:20 2025

@author: dtrej
"""

import cv2
import numpy as np

img = cv2.imread("coins.png", 0)

x = cv2.Sobel(img, cv2.CV_16S, 1, 0, ksize = 3) 
#Se aplica el fitro sobel derivando orden 1  y con un kernel de 3x3 tanto en y como en x
y = cv2.Sobel(img, cv2.CV_16S, 0, 1, ksize = 3)

#Se convierten los valores obtenidos en absolutos y nos regresa la imagen en 8 bits
absX = cv2.convertScaleAbs(x) 
absY = cv2.convertScaleAbs(y)

#se combinan las dos imagenes con una transparencia de 0.5
destino = cv2.addWeighted(absX, 0.5, absY, 0.5, 0)

cv2.imshow("absx", absX)
cv2.imshow("absy", absY)

cv2.imshow("resultado", destino)

cv2.waitKey()
cv2.destroyAllWindows()
