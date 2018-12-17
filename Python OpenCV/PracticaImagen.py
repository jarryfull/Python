#Importamos la libreria "Numpy" que esta hecha para realizar operaciones matematicas
#Importamos la libreria "cv2" que esta es la que nos creara la intefaz y el prosesamiento de imagenes
import numpy as np 
import cv2

#Crea la variable IMG la cual almacenara el resultado de la funcion imread(), primer parametro la ruta de la imagen, segundo parametro: 0 escala de grices o 1 a color
img = cv2.imread('veigar.jpg',0)
#Crea una ventana, Primer parametro: Nombre de la ventana, Segundo parametro: La imagen a desplegar
cv2.imshow('Imagen Con Python', img)
#WaitKey Detiene el programa, en espera de cualquier tecla sea precionada
k = cv2.waitKey(0)

if k == 27: #Si la tecla es 27(ESC)
	#destroyAllwindows() destruye todas las ventanas creadas por CV2
	cv2.destroyAllWindows()	
elif k == ord('s'): #Si la tecla es 'S' 
	#imwrite() guarda la imagen, Primer parametro nombre de la imagen, Segundo parametro la Imagen a guardar
	cv2.imwrite('Imagen Blanco y Negro.jpg', img)
	cv2.destroyAllWindows()