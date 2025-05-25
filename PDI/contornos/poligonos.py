# -*- coding: utf-8 -*-
"""
Created on Thu Mar 20 14:05:58 2025

@author: dtrej
"""

import cv2
import numpy as np

img = cv2.imread("contorno2.jpeg")
img2 = img.copy()
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

_, th = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)
kernel = np.ones((3, 3), np.uint8)
closing = cv2.morphologyEx(th, cv2.MORPH_CLOSE, kernel)

contours, jerarquia = cv2.findContours(closing, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

contornosLista = []

for index in range(len(contours)):
    
    area = cv2.contourArea(contours[index])
    
    if area > 50000:
        contornosLista.append(contours[index])  
    
        cnt = contours[index]
        M = cv2.moments(cnt)
        
        cx = int(M['m10']/M['m00'])#Calculamos la coordenada x del centroide
        cy = int(M['m01']/M['m00'])#Calculamos la coordenada y del centroide
        
        cx2 = cx + 444
        
        resultado = cv2.pointPolygonTest(cnt, (int(cx2), int(cy)), False)
        
        if resultado == 1:
            img = cv2.circle(img2, (cx2, cy), radius= 10, color = (255, 0, 0), thickness = -1)
            img = cv2.putText(img2, "El punto se encuentra dentro del contorno", (10, 50),
                               cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)
            
        elif resultado == -1:
            img2 = cv2.circle(img2, (cx2, cy), radius= 10, color = (0, 0, 255), thickness = -1)
            img2 = cv2.putText(img2, "El punto se encuentra fuera del contorno", (10, 50),
                               cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)
        
        elif resultado == 0:
            img2 = cv2.circle(img2, (cx2, cy), radius= 10, color = (0, 255, 0), thickness = -1)
            img2 = cv2.putText(img2, "El punto se encuentra sobre el contorno", (10, 50),
                               cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
        
        img2 = cv2.circle(img2, (cx, cy), radius= 5, color = (255, 200, 0), thickness = -1)
        
        
cv2.drawContours(img2, contornosLista, -1, (0, 0, 255), 5)
# cantidad = len(contornosLista)

# img2 = cv2.putText(img2, "Son " + str(cantidad) + " monedas", (10, 50),
#                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)

# print("Son " + str(cantidad) + " monedas")

cv2.namedWindow("conteo", cv2.WINDOW_NORMAL)

cv2.imshow("conteo", img2)

cv2.waitKey()
cv2.destroyAllWindows()