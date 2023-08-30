import cv2 as cv
import numpy as np
import matplotlib as plt

img_original = cv.imread("PELOTASLISAS-COLORES.jpg")
imgRGB =  cv.cvtColor(img_original,cv.COLOR_BGR2RGB)
img_gray = cv.cvtColor(img_original,cv.COLOR_BGR2GRAY)

#Imagen sin pelotas
ret,thresh= cv.threshold(img_gray,243,255,cv.THRESH_BINARY)



cv.imshow("imagen Pelotas",thresh)
cv.waitKey(0)
cv.destroyAllWindows()
