# -*- coding: utf-8 -*-
"""
Created on Thu Mar 13 14:59:41 2025

@author: dtrej
"""

import cv2

# img1 = cv2.imread("casaVacia.jpg")
# img1 = cv2.resize(img1, (500,500))

# img2 = cv2.imread("casaDibujo.jpg")
# img2 = cv2.resize(img2, (500,500))

# resta = cv2.absdiff(img2, img1)

# cv2.imshow("Resta", resta)

# cv2.waitKey()
# cv2.destroyAllWindows()

cap = cv2.VideoCapture(1) #Cambiar el valor dependiendo las camaras

conteo = 0

while True:
    ret, frame = cap.read()
    
    gris = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    if conteo == 10:
        fondo = gris
    
    if conteo > 10:
        dif = cv2.absdiff(gris, fondo)
        
        #Realizamos la binarizacion de la imagen
        _, imagenBinarizada = cv2.threshold(dif, 15, 255, cv2.THRESH_BINARY)
        
        #Adquirimos los contornos
        contornos, _ = cv2.findContours(imagenBinarizada, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        
        for contorno in contornos:
            area = cv2.contourArea(contorno)
            
            if area > 9000:
                x, y, w, h = cv2.boundingRect(contorno)
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
    
    cv2.imshow("frame", frame)
    conteo = conteo + 1
    
    if cv2.waitKey(1) == 13:
        break
cap.release()
cv2.destroyAllWindows()
    
    