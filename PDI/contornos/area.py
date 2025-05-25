# -*- coding: utf-8 -*-
"""
Created on Thu Mar 20 14:05:58 2025

@author: dtrej
"""

import cv2
import numpy as np

img = cv2.imread("tornillos.jpg")
img2 = img.copy()
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

_, th = cv2.threshold(gray, 230, 255, cv2.THRESH_BINARY_INV)
kernel = np.ones((3, 3), np.uint8)
closing = cv2.morphologyEx(th, cv2.MORPH_CLOSE, kernel)

contours, jerarquia = cv2.findContours(closing, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

contornosLista = []

for index in range(len(contours)):
    
    area = cv2.contourArea(contours[index])
    
    if area > 15000:
        contornosLista.append(contours[index])        
        
cv2.drawContours(img2, contornosLista, -1, (0, 0, 255), 5)
cantidad = len(contornosLista)

img2 = cv2.putText(img2, "Son " + str(cantidad) + " monedas", (10, 50),
                   cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)

print("Son " + str(cantidad) + " monedas")

cv2.namedWindow("original", cv2.WINDOW_NORMAL)
cv2.namedWindow("Binarizacion", cv2.WINDOW_NORMAL)
cv2.namedWindow("conteo", cv2.WINDOW_NORMAL)

cv2.imshow("original", img)
cv2.imshow("Binarizacion", th)
cv2.imshow("conteo", img2)

cv2.waitKey()
cv2.destroyAllWindows()