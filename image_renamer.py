# -*- coding: utf-8 -*-
"""
Created on Tue May 23 12:01:16 2017

@author: Kevin
"""

#https://stackoverflow.com/questions/2759067/rename-files-in-python
"""I named the files wrong for use into pims.Image_sequence which requires img-0.jpg so this will just rearrange the names cauusee i fuxked up """ 

#current names are B_number_left.jpg or B_number_right.jpg needs to become B_L-number.jpg and so on
import os 

dir1 = "C:\\Users\\Kevin\\Desktop\\PhD\\lisboa\\23may\\four lights and white screen\\left"
dir2 = "C:\\Users\\Kevin\\Desktop\\PhD\\lisboa\\23may\\four lights and white screen\\right"

os.chdir(dir2)
for filename in os.listdir("."):
    if filename.startswith("B") and filename.endswith(".jpg"):
        number = filename.split("_")[1]
        newfilename = "B_right"+"-"+number+".jpg"
        os.rename(filename, newfilename) 
        
#%%
