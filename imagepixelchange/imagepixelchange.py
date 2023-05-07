# -*- coding: utf-8 -*-
"""
Created on Tue Apr  5 09:40:09 2022

@author:neslihan dogan
"""

import cv2 #cv2 kütüphanesi oluşturuldu
import numpy as np#numpy kütüphanesi oluşturuldu as takma isim vermek için kullanılır
import random as rnd#random kütüphanesi oluşturuldu

#siyah bir arkaplan oluşturuldu
#uint8 ile saklanan işaretsiz bir tam sayıyı temsil eder max 0,255 aralığı oda 2 üzeri 8 den -1 den gelir
imgnew =np.zeros([500,500,3],dtype=np.uint8)
#arkaplan beyaza boyandı img fill görevi görür.
imgnew[:] = 255
img1=cv2.imread("rainbow.png")#resim okunma işlemi gerçekleştirildi
img = cv2.resize(img1, (500,500))#resmin boyutunu ayarlamak için kullanılır
'''burda iki tane for loop kullanmamızın amacı satır ve sütun mantığıdır
çünkü işlem yapıldığı aşamada yani yeni bir resim üretileceği zaman resmin genişliği
ve boyu baz alanır ve o değerler arasında döngü içerisindeki işlemler gerçekleşir
'''
for x in range(500):
    for y in range(500):
        randx = rnd.randint(0, 490)#x eksenine rastgele 0-490 araığında pixel ataması yapsın 
        randy = rnd.randint(0, 490)#y eksenine rastgele 0-490 araığında pixel ataması yapsın 
        '''asıl işlem alt taraftaki satırda gerçekleşir yanı asıl değiştirme işlemi 
        burada yeni oluşturacağımız resmi eski oluşan resmin pixelleri ile oynarak 
         yeni resime atama işlemi yapıyoruz pixelleri matrix mantığı ile ulaşıp 
         değiştirme işlemi sağladım'''
        imgnew[y][x] = img[randy][randx]


cv2.imshow("oldimage",img) #eski resmi çıktıda gösterme
cv2.imshow("newimage", imgnew)#yeni resmi çıktıda gösterme
 
k=cv2.waitKey(0)#bekletme süresi
if k==ord('q'):#q ya basınca hem kapatır hemde resmi kaydetme işlemi yapar
    cv2.imwrite("yeni.jpg", imgnew) 
    print("resimi kaydetme işlemi gerçekleşti")
    cv2.destroyAllWindows()#bütün pencereleri kapat