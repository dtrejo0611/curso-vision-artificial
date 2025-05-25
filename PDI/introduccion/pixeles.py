import cv2
import numpy as np

#Se crea matriz de 3 dimenciones y la llenamos con ceros
imagenObscura = np.zeros((100, 100, 3), np.uint8)

pixel = imagenObscura[97, 97] 
print(pixel)

imagenObscura[97, 97] = [255, 255, 255] #Cambiamos el valor del pixel

pixel = imagenObscura[97, 97] 
print(pixel)

alto, largo, canales = imagenObscura.shape

print(alto, largo, canales)

#Recorrer la imagen
# for i in range(largo):
#     for j in range(alto):
#         print(imagenObscura[i, j])
        
for i in range(largo):
    for j in range(alto):
        pixel = imagenObscura[i,j]
        if pixel[0] == 0 and pixel[1] == 0 and pixel[2] == 0:
            imagenObscura[i, j] = [0, 0, 255]
        
cv2.namedWindow("black", cv2.WINDOW_NORMAL)
cv2.imshow("black", imagenObscura)

cv2.waitKey()
cv2.destroyAllWindows()