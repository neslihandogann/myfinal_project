# -*- coding: utf-8 -*-
"""
Created on Thu Mar 31 06:40:51 2022

@author:neslihan dogan
"""

import cv2 
import numpy as np
import random 

img2=cv2.imread("shawnmendes.jpg",1)
img = cv2.resize(img2, (500,600))
img2=cv2.resize(img, (500,600))

#arr = np.array([[black], [white]) önce bu şekilde deneyecektim lakin 
#numpy.int32' object is not iterable bu hatayı verdiği için sürüm uyuşmazlığı direk değer olarak atadım.
white=250
black=300
#randrange =tek parametreli kayan noktalı sayılar elde etmeyi sağlar
for i in range(black):#siyah nokta oluşturmak için
    for j in range(white):#beyaz nokta oluşturmak için
        #random.randrange(start, stop, step)
        X = random.randrange(500 -1)#x koordinatı yanı width -1 kadarı
        Y = random.randrange(600 -1)#y koordinatı yani height -1 kadarı
        if(i<100):#satır kısmı 100 pixel aşağıdakileri siyah nokta ekle 
            img[Y][X] = 0
        if(j%2==0):
            img[Y][X] = (38, 100, 100)#yesil noktalarda ekler 
        else:
            img[Y][X]= 255
cv2.imshow("Siyah beyaz noktalar olustur",img) 
cv2.imshow("orjinal resim",img2) 

k=cv2.waitKey(0)
if k==ord('q'):
    cv2.imwrite("yeniresim.jpg",img)#resmi kaydetme işlemi yappar
    print("yeni resim başarı ile kaydedildi :)")
    cv2.imwrite("yeniresim.jpg", img) 
    cv2.destroyAllWindows()