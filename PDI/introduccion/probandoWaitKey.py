import cv2

img = cv2.imread("0.jpg")
img2 = cv2.imread("0.jpg", cv2.IMREAD_GRAYSCALE)

# while True:
#     cv2.imshow("Color", img)
#     cv2.imshow("Escala de grises", img2)
    
#     key = cv2.waitKey()
    
#     if key == ord("c"):
#         cv2.imwrite("Color.jpg", img)
        
#     elif key == ord("g"):
#         cv2.imwrite("EscalaGrises.jpg", img2)
    
#     else:
#         break

# cv2.destroyAllWindows()

# cv2.imshow("Ventana", img)esta opcion no permite cambiar la escala de la imagen

# cv2.namedWindow("Ventana", cv2.WND_PROP_FULLSCREEN)
# cv2.setWindowProperty("Ventana", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

cv2.namedWindow("Ventana", cv2.WINDOW_NORMAL)

while True:
    
    key = cv2.waitKey()
    
    if key == ord("1"):
        cv2.imshow("Ventana", img)

    elif key == ord("2"):
        cv2.imshow("Ventana", img2)
    
    else:
        break

cv2.destroyAllWindows()