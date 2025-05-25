# -*- coding: utf-8 -*-
"""
Created on Thu Mar 13 14:03:47 2025

@author: dtrej
"""

import cv2
import numpy as np

mT = np.array([[1, 1, 0], [0, 1, 0], [0, 0, 1]])
mR = np.zeros((500, 500, 3), np.uint8)

img = cv2.imread("1.png")
h, w, c = img.shape

for i in range(h):
    for j in range (w):
        vectorPos = np.array([j, i, 1])
        dot = np.dot(mT, vectorPos)
        x = dot[0]
        y = dot[1]
        mR[int(y), int(x)] = img[i, j]

cv2.namedWindow("Original", cv2.WINDOW_NORMAL)
cv2.namedWindow("Perspectiva", cv2.WINDOW_NORMAL)

cv2.imshow("Original", img)
cv2.imshow("Perspectiva", mR)

cv2.waitKey()
cv2.destroyAllWindows()