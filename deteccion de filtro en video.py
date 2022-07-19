import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np 
import cv2


def convert2canny(image_color):
    threshold_1= 120 
    threshold_2= 200
    image_gray= cv2.cvtColor(image_color, cv2.COLOR_BGR2GRAY)
    canny=cv2.Canny(image_gray, threshold_1, threshold_2)
    
    return canny

def convert2Lapplace(image_color): 
    image_gray= cv2.cvtColor(image_color, cv2.COLOR_BGR2GRAY)
    laplaciane=cv2.Laplacian(image_gray, cv2.CV_64F)
    
    return laplaciane

def convert2sobelx (image_color):
    image_gray= cv2.cvtColor(image_color, cv2.COLOR_BGR2GRAY)
    
    # en x
    x_sobel=cv2.Sobel(image_gray, cv2.CV_64F, 0, 1, ksize = 7)    

    
    return x_sobel

def convert2sobely (image_color):
    
    image_gray= cv2.cvtColor(image_color, cv2.COLOR_BGR2GRAY)
    #en y 
    y_sobel=cv2.Sobel(image_gray, cv2.CV_64F, 1, 0, ksize = 7)
    
    return y_sobel

def convert2cartoon (image_color):
    dst=cv2.stylization(image_color, sigma_s=60 , sigma_r=0.5)
    
    return dst

cap=cv2.VideoCapture(0)

while True:
    
    ret, frame =cap.read()
    cv2.imshow('Our Face Extractor' , convert2canny(frame))
    cv2.imshow('cartoon' , convert2cartoon(frame))
    cv2.imshow('sobel' , convert2sobely(frame))
    cv2.imshow('lapplace' , convert2Lapplace(frame))
    cv2.imshow('webcamvideo', frame )
    if cv2.waitKey(1) ==13: # 13 se refiere a la tecla enter 
        break


cap.release()
cv2.destroyAllWindows() 





        