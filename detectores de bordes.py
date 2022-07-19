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

#A escala de grises
image_gray= cv2.cvtColor(image_color, cv2.COLOR_BGR2GRAY)
cv2.imshow('car gray', image_gray)
cv2.waitKey()
cv2.destroyAllWindows()

#-----------Sobel calcula las derivadas--------------#

# en x
x_sobel=cv2.Sobel(image_gray, cv2.CV_64F, 0, 1, ksize = 7)
cv2.imshow('car sobel', x_sobel)
cv2.waitKey()
cv2.destroyAllWindows()

#en y 
y_sobel=cv2.Sobel(image_gray, cv2.CV_64F, 1, 0, ksize = 7)
cv2.imshow('car sobel', y_sobel)
cv2.waitKey()
cv2.destroyAllWindows()

#Laplaciane
laplaciane=cv2.Laplacian(image_gray, cv2.CV_64F)
cv2.imshow('Laplacian', laplaciane)
cv2.waitKey()
cv2.destroyAllWindows()

# -------------detector de bordes canny------------------#

# para canny es necesario definir umbrales
threshold_1= 120 
threshold_2= 200

canny=cv2.Canny(image_gray, threshold_1, threshold_2)
cv2.imshow('Laplacian', canny)
cv2.waitKey()
cv2.destroyAllWindows()







