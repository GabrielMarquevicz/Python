# Python

import cv2
import numpy as np


     

img = cv2.imread('j.png',0)
img_opening = cv2.imread('j_ruido.png',0)
img_closing = cv2.imread('j_furos.png',0)
altura, largura = img.shape
kernel = np.ones((5,5),np.uint8)
print(kernel)
     

erosion = cv2.erode(img,kernel,iterations = 2)
dilation = cv2.dilate(img,kernel,iterations = 2)
     

gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)
opening = cv2.morphologyEx(img_opening, cv2.MORPH_OPEN, kernel)
closing = cv2.morphologyEx(img_closing, cv2.MORPH_CLOSE, kernel)
     


#Caso usa com Python no próprio computador
cv2.imshow('in', img)
cv2.imshow('erosion_out', erosion)
cv2.imshow('dilation_out', dilation)
cv2.imshow('opening_out', opening)
cv2.imshow('closing_out', closing)
cv2.imshow('gradient_out', gradient)
