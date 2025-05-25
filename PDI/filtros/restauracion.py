# -*- coding: utf-8 -*-
"""
Created on Wed Mar 19 13:48:56 2025

@author: dtrej
"""

import cv2
import numpy as np

img = cv2.imread("a.jpg", 0)
equ = cv2.equalizeHist(img)

blur = cv2.blur(equ, (8,8))
blur = cv2.medianBlur(blur, 3)

#Afilamiento

sharpen_kernel = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])

afilada = cv2.filter2D(blur, -1, sharpen_kernel)

result = np.hstack((img, equ, blur, afilada))

cv2.namedWindow("resultado", cv2.WINDOW_NORMAL)
cv2.imshow("resultado", result)

cv2.waitKey()
cv2.destroyAllWindows()