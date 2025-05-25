# -*- coding: utf-8 -*-
"""
Created on Tue Mar 25 14:11:41 2025

@author: dtrej
"""

import numpy as np
import cv2

def extractColor(frame, r):
    imagenNueva = frame[int(r[1]):int(r[1] + r[3]), int(r[0]):int(r[0] + r[2])]
    altura, ancho = imagenNueva.shape[:2]
    
    H = []
    S = []
    V = []
    
    for i in range(altura):
        for j in range(ancho):
            pixel = imagenNueva[i, j]
            H.append(pixel[0])
            S.append(pixel[1])
            V.append(pixel[2])
            
    hMin = min(H)
    hMax = max(H)
    sMin = min(S)
    sMax = max(S)
    vMin = min(V)
    vMax = max(V)
    
    bajo = np.array([hMin, sMin, vMin], np.uint8)
    alto = np.array([hMax, sMax, vMax], np.uint8)
    
    return bajo, alto

cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cv2.namedWindow("Seguimiento", cv2.WINDOW_NORMAL)

conteo = 0

while True:
    res, frame = cam.read()
    masterCopy = frame.copy()
    frameHSV =cv2.cvtColor(masterCopy, cv2.COLOR_BGR2HSV)
    
    if conteo == 10:
        roi = cv2.selectROI("Seguimiento", masterCopy)
        bajo, alto = extractColor(frame, roi)
    
    try:
        mask = cv2.inRange(frameHSV, bajo, alto)
        kernel = np.ones((3, 3), "uint8")
        mask = cv2.dilate(mask, kernel)
        contornos, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        
        area = cv2.contourArea(contornos[-1])
        if area > 100:
            x, y, w, h = cv2.boundingRect(contornos[-1])
            frame = cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
                
    
    except:
        pass
    
    conteo += 1
    cv2.imshow("Seguimiento", frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
     
cam.release()
cv2.destroyAllWindows()