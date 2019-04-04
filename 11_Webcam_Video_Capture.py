import cv2

def main():
    
    #create a window
    windowName = "Live Webcam Video Feed Capture"
    cv2.namedWindow(windowName)
    
    # start the camera
    cap = cv2.VideoCapture(0)
    
    # write the video to the filesystem
    filename = 'Output.avi'
    codec = cv2.VideoWriter_fourcc('W', 'M', 'V', '2')  # codec: WMV1, WMV2, H264, XVID, MJPG, DIVX
    framerate = 30
    resolution = (1024, 768)
    
    VideoFileOutput = cv2.VideoWriter(filename, codec, framerate, resolution)

    while True:
        
        # reading the capture
        ret, frame = cap.read()
        # converting to HSV 
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)     
        # writing the frame to the output file
        VideoFileOutput.write(frame)
        # displaying the frames        
        cv2.imshow(windowName, frame)
        
        # press ESC key to break
        if cv2.waitKey(1) == 27:
            break
    
    # destroying the window and releasing the camera
    cv2.destroyAllWindows()    
    VideoFileOutput.release()
    cap.release()

if __name__ == "__main__":
    main()