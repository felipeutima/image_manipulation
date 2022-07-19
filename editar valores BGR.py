import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np 
import cv2

#importar imagen 
image_color =mpimg.imread('carrtera.jpg')
plt.imshow(image_color)

#colores RGB
image_color.shape

#creo una copia de mi imagen
image_copy=np.copy(image_color)


#juganco con los vaalores BGR
image_copy[ (image_copy[:,:,0]<200) |
           (image_copy[:,:,1]<200) | 
           (image_copy[:,:,2]<200) ] =0


#vemos la imagen
plt.imshow(image_copy, cmap= 'gray')
plt.show()