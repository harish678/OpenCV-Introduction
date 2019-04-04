# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 19:00:57 2019

@author: 540280
"""

import cv2

def main():
    imgpath = "misc/4.1.04.tiff"
    img = cv2.imread(imgpath)
    
    cv2.imshow('Lena', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
if __name__ == "__main__":
    main()