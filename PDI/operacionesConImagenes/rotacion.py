# -*- coding: utf-8 -*-
"""
Created on Thu Mar 13 12:56:51 2025

@author: dtrej
"""

import cv2
import numpy as np
import imutils

img = cv2.imread("2.png")
img2 = cv2.resize(img, (200, 200))

alto, ancho, canales = img2.shape

angle = 50

center = (ancho // 2, alto // 2)
scale = 1

M = cv2.getRotationMatrix2D(center, angle, scale)
print(M)

imgT = np.zeros((alto + 50, ancho + 50, canales), np.uint8)

for i in range(alto):
    for j in range(ancho):
        px = np.array(([j, i, 1]), np.uint8)
        dot = np.dot(M, px)
        x = int(dot[0])
        y = int(dot[1])
        imgT[y, x] = img2[i, j]
        
#Forma facil 1
imgTF = cv2.warpAffine(img2, M, (ancho, alto))

#Forma facil 2
imgTF2 = imutils.rotate_bound(img2, angle)
        
cv2.namedWindow("Original", cv2.WINDOW_NORMAL)
cv2.namedWindow("Rotada", cv2.WINDOW_NORMAL)
cv2.namedWindow("Rotada 2", cv2.WINDOW_NORMAL)
cv2.namedWindow("Rotada 3", cv2.WINDOW_NORMAL)

cv2.imshow("Original", img2)
cv2.imshow("Rotada", imgT)
cv2.imshow("Rotada 2", imgTF)
cv2.imshow("Rotada 3", imgTF)

cv2.waitKey()
cv2.destroyAllWindows()
    