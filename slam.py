import cv2

def process_frame(img)
    print(img)

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