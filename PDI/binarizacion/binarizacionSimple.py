# -*- coding: utf-8 -*-
"""
Created on Wed Mar 19 12:34:25 2025

@author: dtrej
"""

import cv2

img = cv2.imread("coins.png")


_, binNormal = cv2.threshold(img, 80, 255, cv2.THRESH_BINARY)
_, binInv = cv2.threshold(img, 80, 255, cv2.THRESH_BINARY_INV)

cv2.imshow("Original", img)
cv2.imshow("Binarizada", binNormal)
cv2.imshow("Binarizada invertida", binInv)

cv2.waitKey()

cv2.destroyAllWindows()