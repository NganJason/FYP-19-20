import cv2
from darkflow.net.build import TFNet
import numpy as np
import time
import imutils
from datetime import datetime

options = {
	'model': 'cfg/tiny-yolo-voc2.cfg',
	'load': 7000,
	'threshold': 0.2,
}

tfnet = TFNet(options)

capture = cv2.VideoCapture('video6.mov')
#capture.set(cv2.CAP_PROP_FRAME_WIDTH, 200)
#capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 1750
colors = [tuple(255 * np.random.rand(3)) for i in range(5)]
f=open("number.txt","w+")

while (capture.isOpened()):
    stime = time.time()
    ret, frame = capture.read()
    frame = imutils.resize(frame, width = 1080)
    if ret:
        results = tfnet.return_predict(frame)
        for color, result in zip(colors, results):
            tl = (result['topleft']['x'], result['topleft']['y'])
            br = (result['bottomright']['x'], result['bottomright']['y'])
            label = result['label']
            confidence = result['confidence']
            frame = cv2.rectangle(frame, tl, br, color, 5)
            frame = cv2.putText(frame, label, tl, cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 2)
        cv2.imshow('frame', frame)
        now=datetime.now()
        current_time = now.strftime("%H:%M:%S")
        if (len(results) == 1):
        	f.write("Current Time = ")
        	f.write(current_time)
       		f.write(": ")
        	f.write(str(len(results)))
        	f.write("\n")
        print(len(results))
        #print('FPS {:.1f}'.format(1 / (time.time() - stime)))
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        capture.release()
        cv2.destroyAllWindows()
        break
f.close()