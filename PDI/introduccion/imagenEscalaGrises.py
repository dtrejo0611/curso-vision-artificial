# -*- coding: utf-8 -*-
"""
Created on Wed Mar 12 16:34:08 2025

@author: dtrej
"""

import cv2

img = cv2.imread("0.jpg", cv2.IMREAD_GRAYSCALE)#Instruccion para mandar a llamar en escala de grises

cv2.imshow("Ventana1", img)

cv2.waitKey()

cv2.destroyAllWindows()