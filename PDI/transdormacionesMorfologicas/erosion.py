# -*- coding: utf-8 -*-
"""
Created on Wed Mar 19 14:08:00 2025

@author: dtrej
"""

import cv2
import numpy as np

img = cv2.imread("coins.png")

_, th = cv2.threshold(img, 100, 255, cv2.THRESH_BINARY)

kernel = np.ones((3, 3), np.uint8)

dilatacion = cv2.dilate(th, kernel, iterations = 1)
erosion = cv2.erode(dilatacion, kernel, iterations = 1)

cv2.namedWindow("Original", cv2.WINDOW_NORMAL)
cv2.namedWindow("Erosion", cv2.WINDOW_NORMAL)
cv2.namedWindow("Dilatacion", cv2.WINDOW_NORMAL)

cv2.imshow("Original", th)
cv2.imshow("Erosion", erosion)
cv2.imshow("Dilatacion", dilatacion)

cv2.waitKey()
cv2.destroyAllWindows()