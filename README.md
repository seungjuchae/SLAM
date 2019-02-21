# SLAM Side Project


**SLAM** stands for simultaneous localization and mapping and it is about constructing or updating a map of an unknown environment while simultaneously keeping track of an agent's location within it. (Wikipedia)[https://en.wikipedia.org/wiki/Simultaneous_localization_and_mapping]

Feature based SLAM (not dense based SLAM)
What features do is that it track points in an image, from one image to the next image(Frame by Frame)
and we are going to use (ORB feature of Opencv)[https://docs.opencv.org/3.1.0/d1/d89/tutorial_py_orb.html]
## Installation
Opencv 
pygame
numpy
pysdl2 - 
1. download pystdl2 from the (Official website)[https://bitbucket.org/marcusva/py-sdl2/downloads/]2. ```python setup.py install``` 
3. put the sdl folder in the path environmental variable
4. inside the sdl folder put sdl2.dll which is a runtime binary file from (this website)[https://www.libsdl.org/download-2.0.php]

References :
(OpenCV readthedocs)[https://opencv-python-tutroals.readthedocs.io/en/latest/index.html]

(Learn OpenCv)[https://www.learnopencv.com/read-write-and-display-a-video-using-opencv-cpp-python/]

(Opencv image viewer)[https://docs.opencv.org/3.0-beta/doc/py_tutorials/py_gui/py_image_display/py_image_display.html]

(creating surface with PYSDL2)[https://pysdl2.readthedocs.io/en/latest/install.html]
pip3 install pysdl2