# -*- coding: utf-8 -*-
"""
Created on Wed Mar 19 13:43:18 2025

@author: dtrej
"""

import cv2

#Filtro de desenfoque gaussiano

img = cv2.imread("images.jpg", 0)

filtrado = cv2.GaussianBlur(img, (5, 5), 3)

cv2.imshow("original", img)
cv2.imshow("filtrada", filtrado)

cv2.waitKey()
cv2.destroyAllWindows()