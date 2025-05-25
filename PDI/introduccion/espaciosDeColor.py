# -*- coding: utf-8 -*-
"""
Created on Wed Mar 12 17:14:22 2025

@author: dtrej
"""

import cv2
import numpy as np

img = cv2.imread("0.bmp") #leemos imagen

B, G, R = cv2.split(img) # Separamos los canales RGB pero python los lee como BGR

alto, largo, canales = img.shape

K = np.zeros((alto, largo), np.uint8)
W = 255 * (np.ones((alto, largo), np.uint8))
#               C, M, Y
#               R, G, B
img2 = cv2.merge((B, G, R)) #Creamos nueva imagen 

cyan = cv2.merge((W, W, 255-R))

cv2.namedWindow("RGB", cv2.WINDOW_NORMAL)
cv2.namedWindow("Cyan", cv2.WINDOW_NORMAL)
# cv2.namedWindow("BGR", cv2.WINDOW_NORMAL)
# cv2.namedWindow("R", cv2.WINDOW_NORMAL)
# cv2.namedWindow("G", cv2.WINDOW_NORMAL)
# cv2.namedWindow("B", cv2.WINDOW_NORMAL)

cv2.imshow("RGB", img)
cv2.imshow("Cyan", cyan)
# cv2.imshow("BGR", img2)
# cv2.imshow("R", R)
# cv2.imshow("G", G)
# cv2.imshow("B", B)


cv2.waitKey()

cv2.destroyAllWindows()

# hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# H, S, V = cv2.split(hsv)

# cv2.namedWindow("HSV", cv2.WINDOW_NORMAL)
# cv2.namedWindow("H", cv2.WINDOW_NORMAL)
# cv2.namedWindow("S", cv2.WINDOW_NORMAL)
# cv2.namedWindow("V", cv2.WINDOW_NORMAL)

# cv2.imshow("HSV", hsv)
# cv2.imshow("H", H)
# cv2.imshow("S", S)
# cv2.imshow("V", V)

# cv2.waitKey()

# cv2.destroyAllWindows()

# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# cv2.imshow("RGB", img)
# cv2.imshow("GRAY", gray)

# cv2.waitKey()

# cv2.destroyAllWindows()
