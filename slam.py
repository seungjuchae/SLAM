import cv2


cv2.namedWindow('image', cv2.WINDOW_NORMAL)

def process_frame(img):

    # resizing the elements in vector
    img = cv2.resize(img, (1920//2, 1080//2)) 
    
    # Displaying an image
    # cv2.imshow() to display an image in a window
    cv2.imshow('image',img)

    # The function waits for specified milliseconds for any keyboard event. 
    # If you press any key in that time, the program continues
    cv2.waitKey(0) # If 0 is passed, it waits indefinitely for a key stroke
    
    # Displaying the vectors
    print(img.shape)

if __name__ == "__main__":

    # Create a VideoCapture object and read from input file
    # If the input is the camera, pass 0 instead of the video file name
    cap = cv2.VideoCapture("test.mp4")

    # Read until video is completed
    # Sometimes, cap may not have initialized the capture. 
    # In that case, this code shows error. You can check whether it is initialized or not 
    # by the method cap.isOpened(). If it is True, OK. Otherwise open it using cap.open()
    while cap.isOpened():

        # Capture frame-by-frame
        # cap.read() returns a bool (True/False). If frame is read correctly, it will be True
        ret, frame = cap.read();
        if ret == True:

            # Display the resulting frame
            process_frame(frame)
        else:
            break