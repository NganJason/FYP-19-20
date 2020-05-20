import cv2
import numpy as np
import os

# Playing video from file:


try:
    if not os.path.exists('data'):
        os.makedirs('data')
except OSError:
    print ('Error: Creating directory of data')
    
cap = cv2.VideoCapture('video6.mov')
currentFrame = 0
frameno = 488
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    if currentFrame%6 ==0:
    # Saves image of the current frame in jpg file
        name = './data/image' + str(frameno) + '.jpg'
        print ('Creating...' + name)
        cv2.imwrite(name, frame)
        frameno +=1

    # To stop duplicate images
    currentFrame += 1
    

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()