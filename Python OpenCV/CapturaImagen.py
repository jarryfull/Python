import cv2

camera = cv2.VideoCapture(0)

while True:
    #leemos constantemente por el while lo que contiene camera que es la captura de la camara web y lo guardamos en image
    return_value,image = camera.read()

    #Creamos la transformacion de la imagen en binaria y gris
    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    _,binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

    #Creamos las ventanas que nos estara arrojando los resulados de las transformaciones
    cv2.imshow('Camara Binaria', binary)
    cv2.imshow('Camara Gris', gray)
    cv2.imshow('Camara',image)

    #Revisamos si la tecla seleccionada es la "S" para guardar las 3 imagenes
    if cv2.waitKey(1)& 0xFF == ord('s'):
        cv2.imwrite('imgBinaria.jpg', binary)
        cv2.imwrite('imgGris.jpg',gray)
        cv2.imwrite('imgOriginal.jpg',image)
        break

    #Revisamos si la tecla precioanda es "ESC" para salir del programa
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        camera.release()
        cv2.destroyAllWindows()
        break