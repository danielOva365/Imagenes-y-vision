import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors

img_original = cv.imread("PELOTASLISAS-COLORES.jpg")
imgRGB =  cv.cvtColor(img_original,cv.COLOR_BGR2RGB)
img_gray = cv.cvtColor(img_original,cv.COLOR_BGR2GRAY)

r,g,b = cv.split(img_original) #Separo los canales de color

#Imagen sin pelotas
ret, img_sbolas= cv.threshold(img_gray,243,255,cv.THRESH_BINARY_INV)

canal_r = imgRGB[:, :, 0]
canal_g = imgRGB[:, :, 1]
canal_b = imgRGB[:, :, 2]

img_r = np.zeros_like(imgRGB)
img_r[:, :, 0] = canal_r

img_g = np.zeros_like(imgRGB)
img_g[:, :, 1] = canal_g

img_b = np.zeros_like(imgRGB)
img_b[:, :, 2] = canal_b

# Mostrar las imágenes resultantes
plt.figure(figsize=(10, 4))
plt.subplot(131)
plt.imshow(img_r)
plt.title('Canal Rojo')

plt.subplot(132)
plt.imshow(img_g)
plt.title('Canal Verde')

plt.subplot(133)
plt.imshow(img_b)
plt.title('Canal Azul')

plt.tight_layout()
plt.show()

#Imagenes 
#cv.imshow("Rojo",canal_g)
#cv.imshow("Verde",g)
#cv.imshow("Azul",b)


#Separación de las pelotas.
#Pelota naranja
hsv_image = cv.cvtColor(img_original,cv.COLOR_BGR2HSV)
orange_low = np.array([5, 75, 25])
orange_up = np.array([25, 255, 255])
orange_mask = cv.inRange(hsv_image,orange_low,orange_up)
Naranjita =  cv.bitwise_and(img_original, img_original, mask= orange_mask)

cv.imshow("Mascara del Naranja", orange_mask)
cv.imshow("Pelota Naranja",Naranjita)

orange_mask = cv.cvtColor(orange_mask,cv.COLOR_GRAY2BGR)
Resultado = cv.bitwise_and(Naranjita,orange_mask)

cv.imshow("imagen sin Pelotas",img_sbolas)
cv.imshow("Resultado Final",Resultado)
cv.waitKey(0)
cv.destroyAllWindows()


