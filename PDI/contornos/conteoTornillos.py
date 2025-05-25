# -*- coding: utf-8 -*-
"""
Created on Thu Mar 20 13:42:13 2025

@author: dtrej
"""

import cv2
import numpy as np

img = cv2.imread("tornillos.jpg")
img2 = img.copy()

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

_, th = cv2.threshold(gray, 230, 255, cv2.THRESH_BINARY_INV)

#Cuando aparentan tener muchos bordes se debe jugar con el kernel
kernel = np.ones((15, 15), np.uint8)
closing = cv2.morphologyEx(th, cv2.MORPH_CLOSE, kernel)
# bordes = cv2.Canny(closing, 135, 255)

contours, jerarquia = cv2.findContours(closing, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

cv2.drawContours(img2, contours, -1, (0, 0, 255), 10)

cantidadTornillos = len(contours)

img2 = cv2.putText(img2, "Son " + str(cantidadTornillos) + " tornillos", (10, 50),
                   cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 10, cv2.LINE_AA)

print("Son " + str(cantidadTornillos) + " monedas")

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