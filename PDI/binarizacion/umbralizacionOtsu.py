# -*- coding: utf-8 -*-
"""
Created on Wed Mar 19 13:03:41 2025

@author: dtrej
"""

import cv2
from matplotlib import pyplot as plt

img = cv2.imread("coins.png", 0)

hist = cv2.calcHist([img], [0], None, [256], [0, 255])

plt.hist(img.ravel(), 256, [0, 255])

umbral, th = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

print(umbral)

cv2.imshow("Original", img)
cv2.imshow("bin", th)

cv2.waitKey()
cv2.destroyAllWindows()