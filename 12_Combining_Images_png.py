import cv2

def main():
    img1 = cv2.imread('misc/4.1.04.tiff')
    img2 = cv2.imread('misc/download.png')

    scale_percent = 30 # percent of original size
    width = int(img2.shape[1] * scale_percent / 100)
    height = int(img2.shape[0] * scale_percent / 100)
    dim = (width, height)

    img2 = cv2.resize(img2, dim, interpolation=cv2.INTER_AREA)
    
    rows, cols, channels = img2.shape  # getting shape
    roi = img1[0:rows, 0:cols]      # region of interest (show at top-left)
    
    img2gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY) # convert to gray
    ret, mask = cv2.threshold(img2gray, 220, 255, cv2.THRESH_BINARY_INV) # eliminating the bg using threshold
    
    mask_inv = cv2.bitwise_not(mask)    # inverse the mask affect
    
    img1_bg = cv2.bitwise_and(roi, roi, mask = mask_inv)    # prep bg img
    img2_fg = cv2.bitwise_and(img2, img2, mask = mask)  # prep fg img
    
    dst = cv2.add(img1_bg, img2_fg) # combining both the imgs
    img1[0:rows, 0:cols] = dst     # replacing the roi of img1 with the final img2
    
    cv2.imshow('res',img1)  
    

if __name__ == "__main__":
    main()