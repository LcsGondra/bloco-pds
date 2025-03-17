import numpy as np
import matplotlib.pyplot as plt
import cv2

linhas = 14
colunas = 11

matriz = np.ones((linhas, colunas), dtype='uint8')

matriz = matriz*255

for colunai in range(0, colunas):
    matriz[0,colunai]=0

for linhai in range(0, linhas):
    matriz[linhai, 5]=0


plt.subplot(1, 2, 1)
plt.imshow(matriz, cmap=plt.cm.gray)

plt.subplot(1, 2, 2)
plt.imshow(matriz, cmap=plt.cm.gray)
plt.axis('off')
plt.show()