# -*- coding: utf-8 -*-
"""
Created on Thu Mar 20 18:57:08 2025

@author: dtrej
"""

import cv2
import numpy as np

def umbral(valor):
    img2 = imgRgb.copy()
    w, h =template.shape[::-1]
    res = cv2.matchTemplate(imgGray, template, cv2.TM_CCOEFF_NORMED)
    umbralX = valor/100
    rectangulos = np.where(res >= umbralX)
    
    for punto in zip(*rectangulos[::-1]):
        cv2.rectangle(img2, punto, (punto[0] + w, punto[1] + h), (0,255,0), 2)
    
    cv2.imshow('match', img2)
    

imgRgb = cv2.imread('engranaje.jpg')
imgGray = cv2.cvtColor(imgRgb, cv2.COLOR_BGR2GRAY)

template = cv2.imread("template.jpg", 0)

cv2.namedWindow("match", cv2.WINDOW_NORMAL)
cv2.imshow('match', imgRgb)

cv2.createTrackbar('Umbral', 'match', 0, 100, umbral)

cv2.waitKey()
cv2.destroyAllWindows()
