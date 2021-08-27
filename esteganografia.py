# Trabalho Final da disciplina "DCOM3105 - Processamento Digital de Imagens"

import cv2 
import numpy as np 
import random 
 
img1 = cv2.imread('img/new-york.jpg') 
img2 = cv2.imread('img/wallet.jpg') 
cv2.imshow("Original", img1)
cv2.imshow("Esconder", img2)
 
# Esconde a imagem da wallet
for i in range(img2.shape[0]): 
    for j in range(img2.shape[1]): 
        for l in range(3): 
            # img1 em binario
            v1 = format(img1[i][j][l], '08b')
            # img2 em binario
            v2 = format(img2[i][j][l], '08b') 
            # junta as partes binarias -> (img1bin + img2bin)
            v3 = v1[:4] + v2[:4]
            # converte de binario para int --> int(var, base_de_var)
            img1[i][j][l]= int(v3, 2)        
cv2.imshow("Imagem Ocultando Algo", img1)
 
# Aqui é carregada a imagem com algo oculto
img = img1[:]
width = img.shape[0] 
height = img.shape[1] 
img1 = np.zeros((width, height, 3), np.uint8) 
img2 = np.zeros((width, height, 3), np.uint8) 
 
# Revela a imagem da carteira de Bitcoin
for i in range(width): 
    for j in range(height): 
        for l in range(3): 
            # imagem em binario
            v1 = format(img[i][j][l], '08b')
            # imagem normal + 4bits de ruido aleatorio
            v2 = v1[:4] + chr(random.randint(0, 1)+48) * 4
            # imagem oculta + 4bits de ruido
            v3 = v1[4:] + chr(random.randint(0, 1)+48) * 4
            # converte de binario para int
            img1[i][j][l]= int(v2, 2) 
            img2[i][j][l]= int(v3, 2) 
#cv2.imshow("Original_Recuperada", img1)
cv2.imshow("Imagem Oculta Recuperada", img2)
cv2.waitKey(0)
cv2.destroyAllWindows()