# -*- coding: utf-8 -*-
"""
Created on Wed Mar 19 13:11:53 2025

@author: dtrej
"""

import cv2
from matplotlib import pyplot as plt

img = cv2.imread("sudoku.png", 0)

kernel = 3
constante = 0

def updateKernel(krn):
    global kernel
    kernel = krn
    
    if kernel < 3:
        kernel = 3
    elif kernel % 2 == 0:
        kernel += 1
    
    umbralizada = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, kernel, constante)
    cv2.imshow("Binarizando", umbralizada)
    
def updateConstante(cte):
    global constante
    constante = cte
    
    umbralizada = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, kernel, constante)
    cv2.imshow("Binarizando", umbralizada)

cv2.namedWindow("Binarizando")

cv2.createTrackbar("Kernel", "Binarizando", kernel, 255, updateKernel)
cv2.createTrackbar("Constante", "Binarizando", constante, 255, updateConstante)

cv2.waitKey()
cv2.destroyAllWindows()