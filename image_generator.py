# -*- coding: utf-8 -*-
"""
Created on Fri May 19 15:52:12 2017

@author: Kevin
"""

"""This code intakes an avi file name and the folder containing it and fills the folder with jpg images --the frames of the video"""
#%%
import av #makes images from videos 
import os #manipulate directories 

#%%
"""These are the user inputs"""
video_folder = "c:\\users\\kevin\\desktop\\phd\\lisboa\\try" #the folder containing the video-- the images go here 
video_name = "t12.avi" #the name of the video 



#%%

video_path = video_folder+"\\"+video_name #define the path to the video 
os.chdir(video_folder) #this sets the current directory to the video_folder-- this is where the images go
#you could set this directory to wherever you want the images to go


#%%
#define the function to fill the folder containing video_path with the images 

def to_Images(video_path):
    container = av.open(video_path)
    for frame in container.decode(video=0):
        frame.to_image().save('frame-%04d.jpg' % frame.index)



#%%

#fill the video path with images 
to_Images(video_path)