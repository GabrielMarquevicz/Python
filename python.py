# Python

import cv2
import numpy as np

img = cv2.imread('j.png', 0)
img_opening = cv2.imread('j_ruido.png', 0)
img_closing = cv2.imread('j_furos.png', 0)
# Traz o arquivos da imagem para começar a operação
altura, largura = img.shape
 # Consiga o tamanho da imagem
kernel = np.ones((5, 5), np.uint8)
# Define o Kernel
print(kernel)
# Imprime o kernel
erosion = cv2.erode(img, kernel, iterations=2)
dilation = cv2.dilate(img, kernel, iterations=2)
gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)
opening = cv2.morphologyEx(img_opening, cv2.MORPH_OPEN, kernel)
closing = cv2.morphologyEx(img_closing, cv2.MORPH_CLOSE, kernel)
# Começa os processos da Morfologia
cv2.imshow('Original', img)
cv2.imshow('Erosion', erosion)
cv2.imshow('Dilation', dilation)
cv2.imshow('Gradient', gradient)
cv2.imshow('Opening', opening)
cv2.imshow('Closing', closing)
# Mostra as imagens em tela diferentes
cv2.waitKey(0)
cv2.destroyAllWindows()
# Espera você usar ESC para fechar as imagens
