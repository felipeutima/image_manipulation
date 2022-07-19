import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np 
import cv2


#importar imagen 
image_color =mpimg.imread('pare.jpg')
plt.imshow(image_color)

#dimensiones de la imagen 
print('Height = ' , int(image_color.shape[0]), 'pixels')
print('Width = ' , int(image_color.shape[1]), 'pixels')

height, width=image_color.shape[:2]

source_points=np.float32([[50,200],[50,150],[ 180,175],[150,150]])
destination_points=np.float32([[0,0], [width,0], [width,height],[0,height] ])

M=cv2.getPerspectiveTransform(source_points, destination_points)
warped = cv2.warpPerspective(image_color,M, (width, height))

cv2.imshow('imagen warpeada', warped)
cv2.waitKey()
cv2.destroyAllWindows()

