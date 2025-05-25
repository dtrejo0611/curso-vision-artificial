# -*- coding: utf-8 -*-
"""
Created on Wed Mar 19 13:45:25 2025

@author: dtrej
"""

import cv2

#Filtro de desenfoque medio

img = cv2.imread("salYpimienta.jpg", 0)

filtrado = cv2.medianBlur(img, 7)

cv2.imshow("original", img)
cv2.imshow("filtrada", filtrado)

cv2.waitKey()
cv2.destroyAllWindows()