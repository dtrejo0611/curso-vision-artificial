# -*- coding: utf-8 -*-
"""
Created on Thu Mar 20 13:24:24 2025

@author: dtrej
"""

import cv2
import numpy as np

img = cv2.imread("coins.png")
img2 = img.copy()

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

_, th = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)

kernel = np.ones((3, 3), np.uint8)
closing = cv2.morphologyEx(th, cv2.MORPH_CLOSE, kernel)
bordes = cv2.Canny(closing, 135, 255)

contours, jerarquia = cv2.findContours(bordes, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

cv2.drawContours(img2, contours, -1, (0, 255, 0), 2)

cantidadMonedas = len(contours)

img2 = cv2.putText(img2, "Son " + str(cantidadMonedas) + "monedas", (10, 50),
                   cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)

print("Son " + str(cantidadMonedas) + " monedas")

cv2.imshow("original", img)
cv2.imshow("Binarizacion", th)
cv2.imshow("Bordes", bordes)
cv2.imshow("conteo", img2)

cv2.waitKey()
cv2.destroyAllWindows()
