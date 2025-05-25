# -*- coding: utf-8 -*-
"""
Created on Wed Mar 19 14:24:53 2025

@author: dtrej
"""

import cv2
import numpy as np

img = cv2.imread("coins.png")

_, th = cv2.threshold(img, 100, 255, cv2.THRESH_BINARY)

kernel = np.ones((3, 3), np.uint8)

closing = cv2.morphologyEx(th, cv2.MORPH_CLOSE, kernel)

cv2.namedWindow("Original", cv2.WINDOW_NORMAL)
cv2.namedWindow("Close", cv2.WINDOW_NORMAL)

cv2.imshow("Original", th)
cv2.imshow("Close", closing)

cv2.waitKey()
cv2.destroyAllWindows()