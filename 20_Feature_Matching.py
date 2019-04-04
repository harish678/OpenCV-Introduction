import cv2
import matplotlib.pyplot as plt

img1 = cv2.imread('misc/opencv-feature-matching-template.jpg',1)
img2 = cv2.imread('misc/opencv-feature-matching-image.jpg',1)

# Detector for extracting features
orb = cv2.ORB_create()

#we find the key points and their descriptors with the orb detector.

kp1, des1 = orb.detectAndCompute(img1,None)
kp2, des2 = orb.detectAndCompute(img2,None)

# BFMatcher object
bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

# we create matches of the descriptors, then we sort them based on their distances.
matches = bf.match(des1,des2)
matches = sorted(matches, key = lambda x:x.distance)

img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10],None, flags=2)
# converting RGB to BGR
img3 = cv2.cvtColor(img3, cv2.COLOR_RGB2BGR)
plt.imshow(img3)
plt.show()