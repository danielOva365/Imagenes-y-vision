import numpy as np
import cv2 

# Carga la imagen
image = cv2.imread("PELOTASLISAS-COLORES.jpg", cv2.IMREAD_GRAYSCALE)  # Lee la imagen en escala de grises

# Especifica los parámetros del filtro de Gabor
ksize = 9  # Tamaño del kernel
sigma = 4.0  # Desviación estándar de la envolvente gaussiana
theta = np.pi / 4  # Orientación del filtro
lambd = 10.0  # Longitud de onda de la sinusoidal
gamma = 0.5  # Relación aspecto de la envolvente gaussiana

# Crea el filtro de Gabor
gabor_filter = cv2.getGaborKernel((ksize, ksize), sigma, theta, lambd, gamma)

# Aplica el filtro de Gabor a la imagen
filtered_image = cv2.filter2D(image, cv2.CV_64F, gabor_filter)

# Muestra la imagen original y la imagen filtrada
cv2.imshow('Imagen Original', image)
cv2.imshow('Imagen Filtrada', filtered_image)
cv2.waitKey(0)
cv2.destroyAllWindows()