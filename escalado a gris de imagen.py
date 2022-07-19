import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np 
import cv2

#importar imagen 
image_color =mpimg.imread('carrtera.jpg')
plt.imshow(image_color)

#colores RGB
image_color.shape

#convertir a imagen gris
image_gray= cv2.cvtColor(image_color, cv2.COLOR_BGR2GRAY)
plt.imshow(image_gray, cmap= 'gray')
image_gray.shape

#representación de la imagen en matriz 
image_gray

#guadar la imagen
cv2.imwrite ('carretera_gray.jpg', image_gray)