# -*- coding: utf-8 -*-
"""
Created on Thu Mar 13 14:17:34 2025

@author: dtrej
"""

import cv2
import numpy as np

img = cv2.imread("car.jpg")
h, w, c = img.shape

cv2.namedWindow("imagen1", cv2.WINDOW_NORMAL)

global listaPuntos ##Se declara variable global
listaPuntos=[] #Se inicializa la variable global

#Construimos la funcion para trabajar con cv2.setMouseCallback
def obtenerPuntos(event, x, y, flags, params): #Los parametros van por default
    if event == cv2.EVENT_LBUTTONDBLCLK: #Leemos el evento del mouse registrado por cv2.setMouseCallback
    #Si event == doble click izq
        listaPuntos.append([x, y]) #Agregamos las posiciones de x,y a una lista y se agrega a otro array
        
#Utilizamos la función setMouseCallback
cv2.setMouseCallback("imagen1", obtenerPuntos) 
cv2.imshow("imagen1", img)

while True:
    #Si la tecla presionada es "enter" ejecuta el bloque
    if cv2.waitKey(0) == 13: #Enter en asccii
        print(listaPuntos)#se imprime la lista de puntos
        #Obtenemos los puntos de las esquinas de los objetos que queremos transformar 
        pts1 = np.float32(listaPuntos) #Convertimos la lista en un vector tipo float
        #Definimos los puntos donde debe quedar la imagen transformada
        pts2 = np.float32([[0, 0], [w, 0], [0, h], [w, h]])
        
        #Esta funcion devuelve la matriz de transformacion de perspectiva
        M = cv2.getPerspectiveTransform(pts1, pts2)
        
        
        resultadoImagen = cv2.warpPerspective(img, M, (h, w))
        cv2.imshow("imagen1", resultadoImagen)
        
    if cv2.waitKey(0) == 27: #Escape en ascci
        break

cv2.destroyAllWindows()