# -*- coding: utf-8 -*-
"""
Created on Tue Mar 25 15:41:35 2025

@author: dtrej
"""

import nonMaximanSuppression as nms
import numpy as np
import cv2

def fun(x):
    pass

cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cv2.namedWindow("seguimiento", cv2.WINDOW_NORMAL)
cv2.createTrackbar("Umbral", "seguimiento", 50, 100, fun)

conteo = 0

while True:
    res, frame = cam.read()
    img = frame.copy()
    
    if conteo == 10:
        r = cv2.selectROI("seguimiento", img)
        crop = img[int(r[1]):int(r[1] + r[3]), int(r[0]):int(r[0] + r[2])]
        plantilla = cv2.cvtColor(crop, cv2.COLOR_BGR2GRAY)
        
    try:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        valor = cv2.getTrackbarPos("Umbral", "seguimiento")
        h, w = plantilla.shape[:2]
        res = cv2.matchTemplate(gray, plantilla, cv2.TM_CCOEFF_NORMED)
        threshold = valor/100
        rectangulos = np.where(res >= threshold)
        boxes = []
        
        for pt in zip(*rectangulos[::-1]):
            box = (pt[0], pt[1], pt[0]+w, pt[1]+h)
            boxes.append(box)
        
        boxes = np.array(boxes)
        boxes = nms.non_max_suppression_fast(boxes, 0.3)
        for box in boxes:
            cv2.rectangle(frame, (box[0], box[1]), (box[2], box[3]), (0, 255, 0), 2)
            cv2.putText(frame, "Objeto", (box[0], box[1]), cv2.FONT_HERSHEY_SIMPLEX,
                        1.0, (0,0,255), 2)
        
    except:
        pass
        
    conteo += 1
    
    cv2.imshow("seguimiento", frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    

cam.release()
cv2.destroyAllWindows()
    