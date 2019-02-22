import cv2
from display import Display

# Width, height of the window 1920 1080
(width, height) = (1920//2, 1080//2)

# Window display
disp = Display(width, height)
#orb = cv2.ORB_create()
#print(dir(orb))


class ExtractingFeatures(object):
    GX = 16//2
    GY = 16//2
    def __init__(self):
        self.orb = cv2.ORB_create(1000)
    
    def extract(self, img):
        # run detect in grid
        sy = img.shape[0]//self.GY
        sx = img.shape[1]//self.GX
        akp = []
        for ry in range(0, img.shape[0], sy):
            for rx in range(0, img.shape[1], sx):
                img_chunk = img[ry:ry+sy, rx:rx+sx]
                kp = self.orb.detect(img_chunk, None)
                for p in kp:
                    p.pt = (p.pt[0] + rx, p.pt[1] + ry)
                    akp.append(p)
        return akp
               
# ExtractingFeatures
ex = ExtractingFeatures()

def process_frame(img):
    # resizing the elements in vector
    img = cv2.resize(img, (width, height)) 
    kp = ex.extract(img)

    # https://docs.opencv.org/3.0-beta/modules/features2d/doc/feature_detection_and_description.html
    # keypoint, descriptor
    # https://docs.opencv.org/3.4.3/dc/dc3/tutorial_py_matcher.html
    # this finds the keypoints and descriptors with ORB
    # kp, des = orb.detectAndCompute(img, None)

    for p in kp:
        # u,v for coordinate and image
        u,v =map(lambda x: int(round(x)), p.pt)
        cv2.circle(img, (u,v), color=(0,255,0), radius=5) 
  
    disp.paint(img)
    

    # Displaying an image
    # cv2.imshow() to display an image in a window
    #cv2.imshow('image',img)

    # The function waits for specified milliseconds for any keyboard event. 
    # If you press any key in that time, the program continues
    #cv2.waitKey(0) # If 0 is passed, it waits indefinitely for a key stroke
    
    # Displaying the vectors
    #print(img.shape)

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