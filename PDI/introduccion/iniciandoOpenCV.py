import cv2 #Se importa la libreria openCV

img = cv2.imread("0.jpg") #Instruccion para leer la imagen

cv2.imshow("Ventana1", img) #Instruccion para mostrar la imagen leida

cv2.waitKey() #Instruccion para detener ejecucion de la imagen

cv2.destroyAllWindows() #Cierra las ventanas abiertas por openCV

cv2.imwrite("imagenguardada0.jpg", img) #instruccion para guardar imagen

