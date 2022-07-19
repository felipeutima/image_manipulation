import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np 
import cv2

image_gray =mpimg.imread('carretera_gray.jpg')
image_gray.shape

gray_copy=np.copy(image_gray)

#eliminamos cualquier valor menor a 100 en este caso
gray_copy[ (gray_copy[:,:]<100)] =0

#solo quedará lo blanco si se borra lo menos a 250

plt.imshow(gray_copy, cmap='gray')
plt.show()