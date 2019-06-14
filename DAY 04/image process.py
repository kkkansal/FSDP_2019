# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 04:36:25 2019

@author: kunal
"""

from PIL import Image
import os
img = Image.open("rdj.jpg")
print (img.size)
print (img.width)
print (img.height)
print (img.format)
print (img.mode)
img.show()
img_rotate = img.transpose(Image.ROTATE_90)
img_rotate.show()  
img_rotate.save("rdj.jpg") 
small_im = img.resize((300, 150), resample=Image.BICUBIC)
small_im.save('small_rdj.jpg')
img = Image.open("rdj.jpg")
img.thumbnail((75, 75))
print(img.width, img.height)
img.save('thumb_rdj.jpg')
img = Image.open("rdj.jpg")
crop_im = img.crop(box=(340, 20, 560, 164))
crop_im.save('crop_rdj.jpg')
img.show()


