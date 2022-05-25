import cv2
import PIL
import os, os.path
from PIL import Image, ImageOps
from numpy import asarray

#define file location of bubble images
sfile=r'PATH'


for img in os.listdir(sfile):
    f_img = sfile +"/"+img
    img1= Image.open(f_img)
    img=ImageOps.grayscale(img1) #rgb to gray
    
    #crop bubble region 4
    img =img.crop((296,848,1479,1726)) #region4
    img.save(f_img + '__R4.jpg',quality=100)

    #crop bubble region 6
    img1= Image.open(f_img)
    img=ImageOps.grayscale(img1)
    img = img.crop((2652,834,3762,1704)) #region6
    img.save(f_img + '__R6.jpg',quality=100)

    #crop bubble region 7
    img1= Image.open(f_img)
    img=ImageOps.grayscale(img1)
    img = img.crop((296,1740,1479,2580)) #region7
    img.save(f_img + '__R7.jpg',quality=100)

    #crop bubble region 9
    img1= Image.open(f_img)
    img=ImageOps.grayscale(img1)
    img = img.crop((2652,1746,3882,2604)) #region9
    img.save(f_img + '__R9.jpg',quality=100)

