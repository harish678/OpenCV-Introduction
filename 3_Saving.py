
import cv2

def main():
    imgpath = "misc/4.1.04.tiff"
    img = cv2.imread(imgpath, 0) #1(default) - remove alpha transparency channels; 2 - Greyscale; -1 - RGB + alpha transperancy channels (NORMAL)
    
    outpath = "misc/changed_grayscale.jpg"
    
    cv2.imshow('Lena', img)
    cv2.imwrite(outpath, img) # save image to the path.
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
if __name__ == "__main__":
    main()