# -*- coding: utf-8 -*-
"""
Created on Tue May 23 09:59:59 2017

@author: Kevin
"""

"""This code takes a folder containing two subfolders-- left and right. It finds the first image with the bright spot in each. This means the location of the bright
spot must be specified for each image. When the average pixel within the region of the bright spot flips suddenly toward white, this frame is taken as frame 0. 

The code then generates a new folder called aligned inside of folder, and populates it with images named R0,L0,R1,L1, ... RN, LN where N is the last image shared by both cameras"""


from __future__ import division, unicode_literals, print_function  # for compatibility with Python 2 and 3
from time import time #time how long stuff takes 
import matplotlib as mpl
import matplotlib.pyplot as plt

# change the following to %matplotlib notebook for interactive plotting
%matplotlib inline

# Optionally, tweak styles.
mpl.rc('figure',  figsize=(10, 6))
mpl.rc('image', cmap='gray')

import numpy as np
import pandas as pd
from pandas import DataFrame, Series  # for convenience

import pims
import trackpy as tp
import os 
import cv2 #for saving images 

#%%

#specify the directories to the folders containing the images 
path = "C:\\Users\\Kevin\\Desktop\\PhD\\lisboa\\23may\\four lights and white screen" #which should contain folders called left and right of binary images 
dirL = path+"\\left"
dirR = path+"\\right"
prefixL = "B_left-" #the prefix of the binary image filenames 
prefixR = "B_right-"

"""Now you must manually go find the positions of the calibration light in the video and specify a window of pixels where the light will appear"""
Lpos = (550,500) #
w=10
Rpos = (520,1170)
#%%

#http://soft-matter.github.io/pims/v0.4/   for examples on generating frames 

def flash(frames,i,xpos,ypos,w): #given frames array and frame index i, return False if the flash occurs between frames[i][posx-w:posx+w,posy-w:posy+w] and frames[i+1][posx-w:posx+w,posy-w:posy+w]
    if np.abs(np.average(frames[i][(xpos-w):(xpos+w),(ypos-w):(ypos+w)])-np.average(frames[i+1][(xpos-w):(xpos+w),(ypos-w):(ypos+w)]))<=0.5*np.average(frames[i][(xpos-w):(xpos+w),(ypos-w):(ypos+w)]):
        out = True
    else: 
        out = False 
    #this says if the average value of the pixel between xpos-w to xpos+w and ypos-w to ypos+w changes by less than 80 percent
    #between frames i and i+1, then i+1 is NOT the first flash frame 
    #else, flash(frames,i,...) will return False meaning i+1 is the flash frame
    return out 

    
"""This function returns the frame the flash appears in-- frame i+1 when it was not in frame i"""
def flash_frame(side): #if returns False at i then i+1 is the zero position of the video; side is 'L' or 'R'
         #first define the parameters appropriate to side L or R 
         if side=='L':
             xpos,ypos = Lpos
             path = dirL 
             prefix = prefixL
         elif side=='R':
             xpos,ypos = Rpos
             path = dirR
             prefix = prefixR
             
         os.chdir(path) #set the path to the appropriate one 
         frames = pims.ImageSequence(prefix+"*.jpg") #generate the frames
         N = len(frames) #the max index of the frames
         i = 0 #beginning index 
         print("Search for flash on " + side + " side beginning.")
         while flash(frames,i,xpos,ypos,w):
             t0 = time()
             i = i+1
             if i%100==0: 
                 print("Frames up to "+ str(i/190) + "s searched.")
         print(side + " flash found at time " + str(i/190) + "s.")
         return (i+1,N-1) #return flash frame and last frame 
         
        
#%%
"""Here provided the flash positions are correct the flash frames will be calculated"""
frame0_L,frameN_L = flash_frame('L')   #flash frame of left side 

#%%
frame0_R,frameN_R = flash_frame('R')      #flash frame of right side 
             
#and now find the index of the last frame 

number_of_frames = np.amin(np.array([frameN_R-frame0_R,frameN_L-frame0_L]))

#%%
"""now create a folder in path and populate folder with framesR[frame0_R,frameN] and framesL[frame0_L,frameN]"""

#make a new folder in the directory called TimeAlignedFrames                                                               
newpath = path+"\\TimeAlignedFrames" #https://stackoverflow.com/questions/1274405/how-to-create-new-folder
if not os.path.exists(newpath):
    os.makedirs(newpath)
#%%
#now iterate through the right images and save them one by one into newpath as R*.jpg where * is number from 0 to max 
os.chdir(dirR)
frames = pims.ImageSequence(prefixR+"*.jpg")
t0 = time()
for rr in range(number_of_frames):
    oo = frame0_R+rr #rr is the filename index, oo is the frames index on the original series of images 
    cv2.imwrite(newpath+"//R-%s.png" % rr, frames[oo])
    if rr%100==0:
        print(str(rr) + " images of " + str(number_of_frames) + " written in " + str(time()-t0) + "s.")
    
#%%

#and the same for the left 

os.chdir(dirL)
frames = pims.ImageSequence(prefixL+"*.jpg")
t0 = time()
for rr in range(number_of_frames): 
    oo = frame0_L + rr #rr is the filename index and oo the frames index 
    cv2.imwrite(newpath+"//L-%s.png" % rr, frames[oo])
    if rr%100==0:
        print(str(rr) + " images of " + str(number_of_frames) + " written in " + str(time()-t0) + "s.")
    
                                                              

                                                              

