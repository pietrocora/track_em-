# -*- coding: utf-8 -*-
"""
by kev 
"""

"""
This code takes in a photo img.jpg or img.png in the directory path. It then saves a binary photo B_img.jpg in path

Binary image is generated using Otsu method: https://en.wikipedia.org/wiki/Otsu%27s_method"""
#%%
from skimage import filters #this is for the binary filter 
import os #to manipulate paths 
from PIL import Image #pillow image manipulation module 
import numpy as np #numpy array magic 
from time import time #time how long stuff takes 

#%%
img_folder = "c:\\users\\kevin\\desktop\\phd\\lisboa\\calibration1_L" #the folder containing the image 
oimg_folder =  "c:\\users\\kevin\\desktop\\phd\\lisboa\\calibration1_R"
img_name = "1.jpg" #the name of the image

def to_binary(img_folder,img_name): #the function which intakes an image img_name and returns binary version B_img_name  using OTSU METHOD
    os.chdir(img_folder) #set the current directory to img_folder
    image = Image.open(img_name).convert('L') #open image with PIL and convert to each pixel having 1 value between 0 and 255
    im_array = np.array(image) 
    threshold = filters.threshold_otsu(im_array) #this is the threshold value 
    bi_array = (im_array>threshold).astype(int) #form binary boolean array from a condition and then convert to integer values 
    binary_image = Image.fromarray(np.uint8(bi_array*255)) #https://stackoverflow.com/questions/10965417/how-to-convert-numpy-array-to-pil-image-applying-matplotlib-colormap
    binary_image.save("B_"+img_name)
    
def all_to_binary(img_folder): #iterate over every photo in a folder img_folder and turn them all binary USING OTSU METHOD
    os.chdir(img_folder)
    excluded = [] #you could add images you don't want to change here 
    n = 1 #iteration counter
    N=0 #total number of iterations              
    for filename in os.listdir('.'): #for all filenames in the working directory
        if (filename.endswith('.png') or filename.endswith('.jpg')) and filename not in excluded: #if they're not excluded and they're png
            N = N+1 #this part calculates the total number of images which will be converted
    print('Image conversion beginning- ' + str(N) + ' to convert in current directory.')
    for filename in os.listdir('.'): #for all filenames in the working directory
        if (filename.endswith('.png') or filename.endswith('.jpg')) and filename not in excluded: #if the filename represents a jpg image and is not excluded from manipulation
            t0 = time() #initial time of the manipulation of a single image 'filename' 
            to_binary(img_folder,filename)
            excluded.append(filename) #make sure the old image is not modified again
            excluded.append("B_"+filename) #make sure the new image is not modified again
            print('Image ' + str(n) + ' of ' + str(N) + ' has been converted in %0.3fs.' % (time() - t0) ) #print how long it took 
            n = n+1 
    print('Image conversion complete.')                              
             
"""This does the same thing my previous code based upon the k-means algorithm did-- 
all_to_binary converts folders of images to binary colors, except now it is much faster (and also less accurate).""" 

