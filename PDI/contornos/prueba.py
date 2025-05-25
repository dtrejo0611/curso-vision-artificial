# -*- coding: utf-8 -*-
"""
Created on Sat Feb 26 15:03:08 2022

@author: Jesus-Mtz
"""

import cv2
import numpy as np
from datetime import datetime

clasificador = cv2.CascadeClassifier("haarcascade_fullbody.xml")
cap = cv2.VideoCapture("personas.avi")

cuenta = 0
while(cap.isOpened()):
    ret, frame = cap.read()

    if ret == True:
        if cuenta == 0:
            roi = cv2.selectROI(frame)
        
            if roi == (0, 0, 0, 0):
                print("No se seleccionó ninguna región. Cerrando...")
                cap.release()
                cv2.destroyAllWindows()
                exit()
            

            else:
                x1 = roi[0]
                y1 = roi[1]
                w1 = roi[2]
                h1 = roi[3]
            
            cv2.waitKey(0)  # Esperar para que el usuario seleccione ROI

        if cuenta >= 1:
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            img2=frame.copy()
            personas = clasificador.detectMultiScale(gray, scaleFactor=1.2,
                                                     minNeighbors=1,
                                                     minSize=(35,35),
                                                     maxSize=(150,150))
            
            for (x,y,w,h) in personas:
                cx = int((x+(w/2)))
                cy = int((y+(h/2)))
                box = np.array([[x1,y1], [x1+w1,y1],[x1+w1,y1+h1],
                                [x1,y1+h1]])
                box = np.int0(box)
                contornos = [box]
                res = cv2.pointPolygonTest(box, (cx,cy), False)
                cv2.drawContours(frame, contornos, -1,(255,0,0),5)

                if res == 1:
                    cv2.rectangle(frame,(x,y), (x+w,y+h), (0,0,255),2)
                    croppedImage = img2[y:y+h, x:x+w]
                    date = datetime.now()
                    nombreArchivo = ("./capturas/"+str(date.hour)
                                     +str(date.minute)+str(date.second)
                                     +".jpg")
                    cv2.imwrite(nombreArchivo, croppedImage)

            cv2.namedWindow("Frame", cv2.WINDOW_NORMAL)
            cv2.namedWindow("Recorte", cv2.WINDOW_NORMAL)
            cv2.imshow("Frame", frame)
            cv2.imshow("Recorte", croppedImage)

            if cv2.waitKey(25) & 0xFF == ord('q'):
                break
        cuenta += 1
    else:
        break

cap.release()
cv2.destroyAllWindows()