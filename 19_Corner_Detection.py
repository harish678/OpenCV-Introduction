import numpy as np
import cv2

img = cv2.imread('download.png')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

corners = cv2.goodFeaturesToTrack(gray, 500, 0.0001, 3) # how many, quality, minimal distance
corners = np.int64(corners)   # converting float to int for CV to work better

for corner in corners:
    x,y = corner.ravel()
    cv2.circle(img,(x,y),3,255,-1)
    
cv2.imshow('Corner',img)