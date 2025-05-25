# -*- coding: utf-8 -*-
"""
Created on Thu Mar 20 18:35:44 2025

@author: dtrej
"""

import cv2
import numpy as np

img = cv2.imread('engranaje.jpg', 0)
img2 = img.copy()

template = cv2.imread("template.jpg", 0)
w, h =template.shape[::-1]

methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR', 
           'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']

for metodox in methods:
    img = img2.copy()
    metodo = eval(metodox)
    
    res = cv2.matchTemplate(img, template, metodo)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    
    if metodo in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        top_left = min_loc
    else:
        top_left = max_loc
        
    inf_der = (top_left[0] + w, top_left[1] + h)
    cv2.rectangle(img, top_left, inf_der, 255, 2)
    
    cv2.imwrite(metodox + ".jpg", img)