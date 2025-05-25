# -*- coding: utf-8 -*-
"""
Created on Thu Mar 20 13:51:50 2025

@author: dtrej
"""

import cv2
import numpy as np

img = cv2.imread("tornillos.jpg")
img2 = img.copy()
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

_, th = cv2.threshold(gray, 230, 255, cv2.THRESH_BINARY_INV)
kernel = np.ones((15, 15), np.uint8)
closing = cv2.morphologyEx(th, cv2.MORPH_CLOSE, kernel)

contours, jerarquia = cv2.findContours(closing, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

for index in range(len(contours)):
    cv2.drawContours(img2, contours, index, (0, 0, 255), 5)
    
    cnt = contours[index]
    M = cv2.moments(cnt)
    
    cx = int(M['m10']/M['m00'])#Calculamos la coordenada x del centroide
    cy = int(M['m01']/M['m00'])#Calculamos la coordenada y del centroide

    img = cv2.circle(img, (cx, cy), radius= 2, color = (0, 255, 0), thickness = -1)
    img = cv2.putText(img, str(cx) + ", "  + str(cy), (cx - 20, cy), 
                      cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 5) 

cantidad = len(contours)

img2 = cv2.putText(img2, "Son " + str(cantidad) + " monedas", (10, 50),
                   cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 10, cv2.LINE_AA)

print("Son " + str(cantidad) + " monedas")

cv2.namedWindow("original", cv2.WINDOW_NORMAL)
cv2.namedWindow("Binarizacion", cv2.WINDOW_NORMAL)
# cv2.namedWindow("Bordes", cv2.WINDOW_NORMAL)
cv2.namedWindow("conteo", cv2.WINDOW_NORMAL)

cv2.imshow("original", img)
cv2.imshow("Binarizacion", th)
# cv2.imshow("Bordes", bordes)
cv2.imshow("conteo", img2)

cv2.waitKey()
cv2.destroyAllWindows()
       