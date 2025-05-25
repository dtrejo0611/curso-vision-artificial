import cv2
import numpy as np

img = cv2.imread("candados.jpg")

imgCopy = img.copy()

alto, largo, canales = img.shape

cv2.namedWindow("ROI", cv2.WINDOW_NORMAL)

roi1 = cv2.selectROI("ROI", img)
print(roi1)

candado1 = img[int(roi1[1]) : int(roi1[1]+roi1[3]), int(roi1[0]) : int(roi1[0] + roi1[2])]

roi2 = cv2.selectROI("ROI", img)
print(roi2)

candado2 = img[int(roi2[1]) : int(roi2[1]+roi2[3]), int(roi2[0]) : int(roi2[0] + roi2[2])]

alto2, largo2, canales2 = candado2.shape
alto1, largo1, canales1 = candado1.shape


newCandado1 = cv2.resize(candado1, (largo2, alto2))
newCandado2 = cv2.resize(candado2, (largo1, alto1))

imgCopy[int(roi1[1]): int(roi1[1] + roi1[3]), int(roi1[0]) : int(roi1[0] + roi1[2])] = newCandado2
imgCopy[int(roi2[1]): int(roi2[1] + roi2[3]), int(roi2[0]) : int(roi2[0] + roi2[2])] = newCandado1

cv2.namedWindow("Imagen original", cv2.WINDOW_NORMAL)
cv2.namedWindow("Imagen cambiada", cv2.WINDOW_NORMAL)
cv2.namedWindow("candado1", cv2.WINDOW_NORMAL)
cv2.namedWindow("candado2", cv2.WINDOW_NORMAL)

cv2.imshow("Imagen original", img)
cv2.imshow("Imagen cambiada", imgCopy)
cv2.imshow("candado1", candado1)
cv2.imshow("candado2", candado2)

cv2.waitKey()

cv2.destroyAllWindows()
