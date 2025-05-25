# -*- coding: utf-8 -*-
"""
Created on Thu Mar 20 18:47:07 2025

@author: dtrej
"""

import cv2
import numpy as np

imgRgb = cv2.imread("waldo.jpg")
imgGray = cv2.cvtColor(imgRgb, cv2.COLOR_BGR2GRAY)

template = cv2.imread("waldotemplate.jpg", 0)

w, h = template.shape[::-1]

res = cv2.matchTemplate(imgGray, template, cv2.TM_CCOEFF_NORMED)
umbral = 0.8

rectangulos = np.where(res >= umbral)

for punto in zip(*rectangulos[::-1]):
    cv2.rectangle(imgRgb, punto, (punto[0] + w, punto[1] + h), (0,255,0), 2)
   
cv2.namedWindow("resultado", cv2.WINDOW_NORMAL)

cv2.imshow("resultado", imgRgb)

cv2.waitKey()
cv2.destroyAllWindows()