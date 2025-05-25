# -*- coding: utf-8 -*-
"""
Created on Wed Mar 19 13:46:56 2025

@author: dtrej
"""

import cv2

#Filtro bilateral

img = cv2.imread("images.jpg", 0)

filtrado = cv2.bilateralFilter(img, 13, 75, 75)

cv2.imshow("original", img)
cv2.imshow("filtrada", filtrado)

cv2.waitKey()
cv2.destroyAllWindows()