import cv2 
import numpy as np
from PIL import ImageColor,Image
from os import *
import imageio
#read orignal function
def readoriginalfun(img):
   originalimg=cv2.imread (img)
   #cv2.imshow('imageorigina',originalimg)
   #cv2.waitKey(0)
   #cv2.destroyAllWindows()
   return originalimg
#convert the image to grayscale
def graytocolor(a):
    grayscaleimag = cv2.cvtColor(a, cv2.COLOR_BGR2GRAY)
    #cv2.imshow('imageorigina',grayscaleimag)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()
    return grayscaleimag
# Canny detection filter 
def cannyfun(a):
    edges = cv2.Canny(a, threshold1=100, threshold2=200) 
    return edges 
#Apply LOOK UP TABLE
def LUT_Inverse(edges):
    tab=np.array(edges)
    #tab1=np.array(readoriginalfun(img))
    print(tab)
    for i in range(tab.shape[0]):
      for j in range(tab.shape[1]):
      # Inverse function
       tab[i,j] =255-tab[i,j]
    print(tab)
    return tab
#Save file with edge
def savenewimage(edges):
   nvimage=ImageColor.fromarray(np.uint8(edges))
   k="C:/Users/bouzi/cartoon/static/store/edge.jpg"
   nvimage.save(k)
   nvimage.show()
   inverse=cv2.imread (k)
   return inverse
 
# creation of quatifization technique
def cartoonize(img,k):
   tab=np.array(img)
   imgout=np.float32(tab).reshape(-1,3)
   print(tab.shape)
   print(imgout.shape)
 # les critére du K-means arrêter l'algo quand l'un des critéres est évalué
   criteria=(cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER ,20,1.0)
 #application du k-mean
   compactness,labels,center=cv2.kmeans(imgout,k,None,criteria,10,cv2.KMEANS_RANDOM_CENTERS)
   center = np.uint8(center)
   print(labels)
   result=center[labels.flatten()]
   result = result.reshape(tab.shape)
   print(result.shape)   
   #cv2.imshow('imageorigina',result)
   return result
   
#Save of quatifizied picture 
def savenewimage(a):
   nvimage=Image.fromarray(np.uint8(a))
   k="C:/Users/bouzi/cartoon/static/store/effectcartoon.jpg"
   im1 = Image.open(k) 
   #save a image using extension
   im1 = im1.save(nvimage,format="BMP")
   return nvimage
   
#Smothing of 
def smothing(a):
   a=cv2.medianBlur(a,3)
   return a
#combine the canny edge detection and the result of the smothing function 
def combine(a,b,c):
   cartoon=cv2.bitwise_and(a,a,mask=b)
   cartoon2=cv2.cvtColor(cartoon,cv2.COLOR_BGR2RGB)
   cartoon1=Image.fromarray(cartoon2)
   cartoon1.save("C:/Users/bouzi/cartoon/static/store/1"+c)
   #cartoon1.show()
   path ="/static/store/1"+c
   print(path)
   return path

#combine the edge  adaptative and the result of the smothing function 
def combine1(a,b,c):
   cartoon=cv2.bitwise_and(a,a,mask=b)
   cartoon2=cv2.cvtColor(cartoon,cv2.COLOR_BGR2RGB)
   cartoon1=Image.fromarray(cartoon2)
   cartoon1.save("C:/Users/bouzi/cartoon/static/store/2"+c)
   #cartoon1.show()
   path ="/static/store/2"+c
   print(path)
   return path

#reduce the noise with linear filter using gaussianBlur 
def eliminenoise(a):
    img_blur = cv2.GaussianBlur(a, (3,3), 0)
    return img_blur
#edges = cv2.adaptiveThreshold(img_blur,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,9,8)
def edges(a):
  edges = cv2.adaptiveThreshold(a,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,9)
  return edges
#using adaptative filter 
def adaptative(img,k,i):
   readoriginalfun(img)
   a=graytocolor(readoriginalfun(img))
   b=eliminenoise(a)
   c=edges(b)
   d=cartoonize(readoriginalfun(img),k)
   e=smothing(d)
   f=combine1(e,c,i)
   print(f)
   return f

   
