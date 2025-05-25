# -*- coding: utf-8 -*-
"""
Created on Thu Mar 13 20:31:03 2025

@author: dtrej
"""

import cv2
from matplotlib import pyplot as plt
import numpy as np

img = cv2.imread("lena.png", 0)

mask = np.zeros(img.shape[:2], np.uint8)

mask[0 : 300, 0 : 300] = 255

#aplicamos una compuerta and bit a bit entre img e img, pero solo en la parte de
#la mascara con pixeles blancos
masked_img = cv2.bitwise_and(img, img, mask = mask) 

histCompleto = cv2.calcHist([img], [0], None, [256], [0, 255])
histMask = cv2.calcHist([img], [0], mask, [256], [0, 255])

plt.subplot(221), plt.imshow(img, "gray")
plt.subplot(222), plt.imshow(mask, "gray")
plt.subplot(223), plt.imshow(masked_img, "gray")
plt.subplot(224), plt.plot(histCompleto), plt.plot(histMask)

plt.xlim([0, 255])

plt.show()