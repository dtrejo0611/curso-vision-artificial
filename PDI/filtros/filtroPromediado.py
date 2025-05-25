# -*- coding: utf-8 -*-
"""
Created on Wed Mar 19 13:23:54 2025

@author: dtrej
"""

import cv2

#Filtro de promediado

img = cv2.imread("salYpimienta.jpg", 0)

imgBlurred = cv2.blur(img, (5,5)) #Aplicamos filtro de promediadio con kernel 8x8

cv2.imshow("original", img)
cv2.imshow("filtrada", imgBlurred)

cv2.waitKey()
cv2.destroyAllWindows()