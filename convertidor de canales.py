
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np 
import cv2

#importar imagen 
image_color =mpimg.imread('auto.jpg')
plt.imshow(image_color)
image_color.shape

#dimensiones de la imagen 
print('Height = ' , int(image_color.shape[0]), 'pixels')
print('Width = ' , int(image_color.shape[1]), 'pixels')

#mostrando la foto con cv2 
# se puede ver la diferencia de colores entre plt y imshow
#cv2 presenta la paleta de colores BGR  

cv2.imshow('car color', image_color)
cv2.waitKey()
cv2.destroyAllWindows()

#A escala de grises
image_gray= cv2.cvtColor(image_color, cv2.COLOR_BGR2GRAY)
cv2.imshow('car gray', image_gray)
cv2.waitKey()
cv2.destroyAllWindows()

# --------------------A HSV------------

hsv_image=cv2.cvtColor(image_color, cv2.COLOR_BGR2HSV)
cv2.imshow('car HSV', hsv_image)
cv2.waitKey()
cv2.destroyAllWindows()

#separando HSV
plt.imshow(hsv_image[:,:,0])
plt.title('hue channel ')

plt.imshow(hsv_image[:,:,1])
plt.title('Saturation channel ')

plt.imshow(hsv_image[:,:,2])
plt.title('value channel ')

#------------Separando BGR--------------#


B,G,R=cv2.split(image_color)
zeros = np.zeros(image_color.shape[:2], dtype ='uint8')

cv2.imshow ('este es el canal azul', cv2.merge([B, zeros, zeros]))
cv2.waitKey()
cv2.destroyAllWindows()

cv2.imshow ('este es el canal verde', cv2.merge([zeros, G, zeros]))
cv2.waitKey()
cv2.destroyAllWindows()

cv2.imshow ('este es el canal rojo', cv2.merge([zeros, zeros, R]))
cv2.waitKey()
cv2.destroyAllWindows()

#union de los canales 

image_merged=cv2.merge([B,G,R])
cv2.imshow('imagen unidad', image_merged)
cv2.waitKey(0)
cv2.destroyAllWindows()

#para jugar con los canales 

image_merged=cv2.merge([B+30,G+90,R-10]) # se cambian los numeros para interactuar
cv2.imshow('imagen unidad', image_merged)
cv2.waitKey(0)
cv2.destroyAllWindows()





