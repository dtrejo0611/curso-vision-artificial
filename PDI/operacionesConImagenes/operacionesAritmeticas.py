# -*- coding: utf-8 -*-
"""
Created on Thu Mar 13 14:43:52 2025

@author: dtrej
"""

import cv2

img1 = cv2.imread("1.png")
img1 = cv2.resize(img1, (500,500))

img2 = cv2.imread("2.png")
img2 = cv2.resize(img2, (500,500))

suma = cv2.add(img1, img2)
resta = cv2.subtract(img2, img1)
mult = cv2.multiply(img1, img2)
division = cv2.divide(img2, img1)

cv2.imshow("Original1", img1)
cv2.imshow("Original2", img2)
cv2.imshow("Suma", suma)
cv2.imshow("Resta", resta)
cv2.imshow("Multiplicacion", mult)
cv2.imshow("Division", division)

cv2.waitKey()
cv2.destroyAllWindows()