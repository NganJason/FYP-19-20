import cv2
from darkflow.net.build import TFNet
import numpy as np
import time
import imutils
from datetime import datetime
import os

options = {
	'model': 'cfg/tiny-yolo-voc2.cfg',
	'load': 8000,
	'threshold': 0.2,
}

tfnet = TFNet(options)
image_folder = '/Users/jasonngan/Desktop/darkflow/testset'
savedir = 'testresult8000'
f= open("result.txt","w+")

for n, image_file in enumerate(os.scandir(image_folder)):

    img = image_file
    try:
    	image = cv2.imread(image_file.path)
    	image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    	results = tfnet.return_predict(image)
    	save_path = os.path.join(savedir, img.name.replace('jpg', 'txt'))
    	# print(results[0]['topleft']['x'])
    	with open(save_path, 'w+') as a:
            for i in range(len(results)):
                print(i)
                a.write(str(results[i]['label']))
                a.write(' ')
                a.write(str(results[i]['confidence']))
                a.write(' ')
                a.write(str(results[i]['topleft']['x']))
                a.write(' ')
                a.write(str(results[i]['topleft']['y']))
                a.write(' ')
                a.write(str(results[i]['bottomright']['x']))
                a.write(' ')
                a.write(str(results[i]['bottomright']['y']))
                a.write('\n')
    except:
    	pass


    # for color, result in zip(colors, results):
    #     tl = (result['topleft']['x'], result['topleft']['y'])
    #     br = (result['bottomright']['x'], result['bottomright']['y'])
    #     label = result['label']
    #     confidence = result['confidence']
    #     frame = cv2.rectangle(frame, tl, br, color, 5)
    #     frame = cv2.putText(frame, label, tl, cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 2)
f.close()

# capture = cv2.VideoCapture('video3.mov')

# colors = [tuple(255 * np.random.rand(3)) for i in range(5)]
# f=open("number.txt","w+")

# while (capture.isOpened()):
#     stime = time.time()
#     ret, frame = capture.read()
#     frame = imutils.resize(frame, width = 1080)
#     if ret:
#         results = tfnet.return_predict(frame)
#         for color, result in zip(colors, results):
#             tl = (result['topleft']['x'], result['topleft']['y'])
#             br = (result['bottomright']['x'], result['bottomright']['y'])
#             label = result['label']
#             confidence = result['confidence']
#             frame = cv2.rectangle(frame, tl, br, color, 5)
#             frame = cv2.putText(frame, label, tl, cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 2)
#         cv2.imshow('frame', frame)
#         now=datetime.now()
#         current_time = now.strftime("%H:%M:%S")
#         if (len(results) == 1):
#         	f.write("Current Time = ")
#         	f.write(current_time)
#        		f.write(": ")
#         	f.write(str(len(results)))
#         	f.write("\n")
#         print(len(results))
#         #print('FPS {:.1f}'.format(1 / (time.time() - stime)))
#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break
#     else:
#         capture.release()
#         cv2.destroyAllWindows()
#         break
# f.close()