import cv2
import matplotlib.pyplot as plt

def main():
    
    imgpath = "misc/4.1.04.tiff"
    img = cv2.imread(imgpath, 1) #Defaukt BGR
    
    img1 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) #convert BGR to RGB
    
    plt.imshow(img) # Default RGB
    plt.title('Color Image BGR')
    plt.xticks([])
    plt.yticks([])
    plt.show()
 
    
    plt.imshow(img1)
    plt.title('Color Image RGB')
    plt.xticks([])
    plt.yticks([])
    plt.show()
 
if __name__ == "__main__":
    main()