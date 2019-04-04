import cv2

img = cv2.imread('misc/bookpage.jpg')

retval, threshold = cv2.threshold(img, 12, 255, cv2.THRESH_BINARY)

grayscaled = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
retval2, threshold2 = cv2.threshold(grayscaled, 12, 255, cv2.THRESH_BINARY)

gaussian_img = cv2.adaptiveThreshold(grayscaled, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)

retval3, otsu = cv2.threshold(grayscaled, 125,255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)

cv2.imshow('original',img)  #too bad
cv2.imshow('threshold',threshold)  #okay
cv2.imshow('threshold2',threshold2)  #bad
cv2.imshow('Gaussian', gaussian_img) #goooooood
cv2.imshow('otsu',otsu)   # too bad

cv2.waitKey(0)
cv2.destroyAllWindows()