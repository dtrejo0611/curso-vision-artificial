# -*- coding: utf-8 -*-
"""
Created on Thu Mar 13 13:30:50 2025

@author: dtrej
"""

import cv2
import numpy as np

img = cv2.imread("1.jpg")
h, w, c = img.shape

escala = 0.5

mT = np.array([[escala, 0, 0], [0, escala, 0], [0, 0, 1]])

imgT = np.zeros((int(h * escala), int(w * escala), 3), np.uint8)

for i in range(h):
    for j in range (w):
        vectorPos = np.array([j, i, 1])
        dot = np.dot(mT, vectorPos)
        x = dot[0]
        y = dot[1]
        imgT[int(y), int(x)] = img[i, j]
    
#Forma facil
escalada = cv2.resize(img, (int(h*2), int(w*2)),interpolation = cv2.INTER_LINEAR)

        
cv2.namedWindow("Original", cv2.WINDOW_NORMAL)
cv2.namedWindow("Escalada", cv2.WINDOW_NORMAL)
cv2.namedWindow("Escalada 2", cv2.WINDOW_NORMAL)

cv2.imshow("Original", img)
cv2.imshow("Escalada", imgT)
cv2.imshow("Escalada 2", escalada)

cv2.waitKey()
cv2.destroyAllWindows()