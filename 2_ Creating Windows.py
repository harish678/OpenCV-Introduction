# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 19:05:07 2019

@author: 540280
"""
import cv2

def main():
    imgpath = "misc/4.1.04.tiff"
    img = cv2.imread(imgpath)
    
    # creating named window
    cv2.namedWindow('LENA', cv2.WINDOW_AUTOSIZE)
    cv2.imshow('Lena', img)
    cv2.waitKey(0)
    cv2.destroyWindow('LENA')
    
if __name__ == "__main__":
    main()