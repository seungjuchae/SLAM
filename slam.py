import cv2
from display import Display
import numpy as np

# Width, height of the window 1920 1080
(width, height) = (1920//2, 1080//2)

# Window display
disp = Display(width, height)


class ExtractingFeatures(object):
    GX = 16//2
    GY = 16//2
    def __init__(self):
        # Initiate ORB detector
        self.orb = cv2.ORB_create(1000)
    
    def extract(self, img):

        features = cv2.goodFeaturesToTrack(np.mean(img, axis=2).astype(np.uint8), 3000, qualityLevel=0.01, minDistance=3)
        print(features)
        return features

# ExtractingFeatures
ex = ExtractingFeatures()

def process_frame(img):
    # resizing the elements in vector
    img = cv2.resize(img, (width, height)) 
    kp = ex.extract(img)
    if kp is not None:
        for p in kp:
            # u,v for coordinate and image
            u,v = map(lambda x: int(round(x)), p[0])
            cv2.circle(img, (u,v), color=(0,255,0), radius=3) 
    else:
        print("lag")
  
    disp.paint(img)
    
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