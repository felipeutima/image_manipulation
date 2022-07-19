import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np 
import cv2

#importar imagen 
image_color =mpimg.imread('auto.jpg')
plt.imshow(image_color)

#dimensiones de la imagen 
print('Height = ' , int(image_color.shape[0]), 'pixels')
print('Width = ' , int(image_color.shape[1]), 'pixels')

height, width=image_color.shape[:2]

#----------------------rotar-----------#

img_rotation=cv2.getRotationMatrix2D((width/2, height/2), 90, 0.5)
rotated_image=cv2.warpAffine(image_color, img_rotation, (width, height))
cv2.imshow('imagen rotada', rotated_image)
cv2.waitKey()
cv2.destroyAllWindows()

#--------------Translacion---------------#
translation_matrix=np.float32([[1, 0, 300],
                               [0, 1, 50]])

translated_image =cv2.warpAffine(image_color, translation_matrix,
                                 (width, height))
cv2.imshow('corte de imagen', translated_image)
cv2.waitKey()
cv2.destroyAllWindows()

#--------------------redimensionar--------#
resized_image= cv2.resize(image_color, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
cv2.imshow('imagen redimensionada', resized_image)
cv2.waitKey()
cv2.destroyAllWindows()








