
import cv2
import numpy as np

def main():

    img = np.ones((512,512,3), np.uint8)
    cv2.line(img, (0,99), (199,0), (255,0,0), 2) # canvas, x, y, color, thickness
    cv2.rectangle(img, (100,60), (80,70), (0,255,0), 3)
    cv2.circle(img, (40,40), 30, (0,0,255), -1) #image, Point, Radius, color, thickness
    cv2.ellipse(img, (160,260),(50,20), 0,0,360, (127,127,127), 2) #image, focus1, focus2, rotation angle, Start Angle, End Angle, color, thickness
    
    text = 'Shapes'
    cv2.putText(img, text, (100,100), cv2.FONT_HERSHEY_SIMPLEX, 2, (255,255,0)) #image, text, point, font, font_size, color
    cv2.imshow('Shapes', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
if __name__ == "__main__":
    main()