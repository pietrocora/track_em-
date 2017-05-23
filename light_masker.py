# -*- coding: utf-8 -*-
"""
Created on Tue May 23 14:00:03 2017

@author: Kevin
"""
"""
apply DBSCAN algorithm to find all clustered white pixels above some big size-- this will be the only cluster that big
the particles in motion will classify as noise 
"""
#%%
import numpy as np
import cv2
import os #to manipulate paths 
from PIL import Image #pillow image manipulation module
import time

#%%

#not sure if this will work 

#import the last L image and last R image in path 

path = "C:\\Users\\Kevin\\Desktop\\PhD\\lisboa\\23may\\four lights and white screen\\TimeAlignedFrames"
os.chdir(path)

#iterate through every image in path and remove the top 200 pixels and the biggest contour 
n = 1
N = len([f for f in os.listdir('.') if filename.endswith(".jpg") or filename.endswith(".png")])
t0 = time()
for filename in os.listdir('.'):
    if filename.endswith(".jpg") or filename.endswith(".png") :
        im = cv2.imread(filename)[200:,:]
        imgray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        ret, thresh = cv2.threshold(imgray, 127, 255, 0)
        im2, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
        
        csizes = []
        for nn in range(len(contours)): 
            csizes.append(len(contours[nn]))
        csizes = np.array(csizes)
        ind = np.argsort(csizes)[-1]
        c = contours[ind] #the biggest contour 
        out = cv2.drawContours(im2,[c],0,0,-1)
        newfilename = "M_"+filename
        cv2.imwrite(newfilename,out)
        n=n+1
    print("Image " + str(n) + " of " + str(N) + " masked by " + str(time()-t0) + "s.")    

#%%
#if you fuck up delete them with this: 
for filename in os.listdir('.'):   
    if filename.endswith(".jpg") or filename.endswith(".png") and filename.startswith('M'):
        os.remove(path+"\\"+filename)
#okay that works alright... 

