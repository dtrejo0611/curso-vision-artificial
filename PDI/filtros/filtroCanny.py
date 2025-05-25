# -*- coding: utf-8 -*-
"""
Created on Wed Mar 19 15:04:47 2025

@author: dtrej
"""

import cv2
import numpy as np

# img = cv2.imread("coins.png", 0)

# #Se aplica el filtro canny para detectar los bordes, se selecciona un umbral
# #minimo de 135 y un maximo de 255
# bordes = cv2.Canny(img, 135, 255) 
# cv2.imshow("result", bordes)

# cv2.waitKey()
# cv2.destroyAllWindows()

# img = cv2.imread("coins.png", 0)

# gaussiana = cv2.GaussianBlur(img, (9, 9), 0)

# _, th = cv2.threshold(gaussiana, 100, 255, cv2.THRESH_BINARY)

# bordes = cv2.Canny(th, 135, 255)

# cv2.imshow("result", bordes)

# cv2.waitKey()
# cv2.destroyAllWindows()

imgC = cv2.imread("coins.png")
imgD = imgC.copy()
img = cv2.cvtColor(imgC, cv2.COLOR_BGR2GRAY)

gaussiana = cv2.GaussianBlur(img, (9, 9), 0)

_, th = cv2.threshold(gaussiana, 100, 255, cv2.THRESH_BINARY)

bordes = cv2.Canny(th, 135, 255)

alto, largo = img.shape

for i in range(largo):
    for j in range(alto):
        if bordes[j, i] == 255:
            imgD[j, i] = (0, 0, 255)
        
cv2.imshow("Original", imgC)
cv2.imshow("Bordes", bordes)
cv2.imshow("Resultado", imgD)

cv2.waitKey()
cv2.destroyAllWindows()


