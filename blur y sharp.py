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

#--------------sharp --------------#
#creo el filtro
sharp_kernel= np.array([[0, -1, 0],
                       [-1, 9, -1],
                       [0, -1, 0]])


#añado el filtro 
sharpe_image=cv2.filter2D(image_gray,-1, sharp_kernel)
cv2.imshow('LAPLACIANE', sharpe_image)
cv2.waitKey()
cv2.destroyAllWindows()

#-----------------blurr--------------------------------#
#creo el filtro
blurr_kernel =np.ones((3,3)) # me crea una matriz 3x3 con solo unos

#añado el filtro 
blurred_image=cv2.filter2D(image_gray,-1, blurr_kernel)
cv2.imshow('BLURR', blurred_image)
cv2.waitKey()
cv2.destroyAllWindows()

#-----------------Normalización o suavizado--------------#
#creo el filtro
normal_kernel =np.ones((3,3))*1/9 # me crea una matriz 3x3 con solo unos
normal_kernel 
#añado el filtro 
normal_image=cv2.filter2D(image_gray,-1, normal_kernel)
cv2.imshow('Imagen normalizdda', normal_image)
cv2.waitKey()
cv2.destroyAllWindows()

#------------Blurr mas grande------------#

#creo el filtro
super_kernel =np.ones((8,8))*1/64
super_kernel 
#añado el filtro 
sup_image=cv2.filter2D(image_gray,-1, super_kernel)
cv2.imshow('Imagen normalizada', sup_image)
cv2.waitKey()
cv2.destroyAllWindows()














