# -*- coding: utf-8 -*-
"""
Created on Tue May 23 10:21:27 2017

@author: Kevin
"""

"""This code takes a directory containing videos from the M5 and concatenates the videos in it in order, because for some reason this camera doesn't do it...  """ 

#based upon https://gist.github.com/nkint/8576156
#modifed for python 3 with http://docs.opencv.org/3.2.0/dd/d43/tutorial_py_video_display.html

import numpy as np
import cv2 
import os


#%%
path = "C:\\Users\\Kevin\\Desktop\\PhD\\lisboa\\23may\\23 may_L\\four lights and white screen"
os.chdir(path)


vids = [p for p in os.listdir('.') if p[-4:]=='.avi']
vids = sorted(vids, key=lambda item: item[-5]) #sort videos by last number before the .avi 

             
             
video_index = 0
cap = cv2.VideoCapture(vids[0])
fourcc = cv2.VideoWriter_fourcc(*'DIVX')
# video resolution: (1680,720)
out = cv2.VideoWriter('output.avi', fourcc, 190, (1680,720)) 

while(cap.isOpened()):
    ret, frame = cap.read()
    if frame is None:
        print( "end of video " + str(video_index) + " .. next one now")
        video_index += 1
        if video_index >= len(vids):
            break
        cap = cv2.VideoCapture(vids[ video_index ])
        ret, frame = cap.read()
    cv2.imshow('frame',frame)
    out.write(frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()

print("end.")

                                               