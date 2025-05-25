# -*- coding: utf-8 -*-
"""
Created on Wed Mar 19 12:56:41 2025

@author: dtrej
"""

import cv2

def umbral(valor):
    _, th = cv2.threshold(img, valor, 255, cv2.THRESH_BINARY)
    cv2.imshow("Binarizando", th)

img = cv2.imread("coins.png")

cv2.namedWindow("Binarizando")

cv2.createTrackbar("Umbral", "Binarizando", 0, 255, umbral)

cv2.waitKey()
cv2.destroyAllWindows()