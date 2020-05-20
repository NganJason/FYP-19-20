from PIL import Image
import cv2
import os

try:
    if not os.path.exists('dataflipverti'):
        os.makedirs('dataflipverti')
except OSError:
    print ('Error: Creating directory of data')

image_folder = '/Users/jasonngan/Desktop/training2/data'
number = 1811

for n, image_file in enumerate(os.scandir(image_folder)):
	if number % 3 == 0:
		image = cv2.imread(image_file.path)
		flipverti = cv2.flip(image, 0)
		name = './dataflipverti/flipverti' + str(number) + '.jpg'
		print ('Creating...' + name)
		cv2.imwrite(name, flipverti)
	number+=1



# image = cv2.imread('image598.jpg')
# fliphori = cv2.flip(image, 0)
# name = 'flipvertiimage.jpg'

# cv2.imwrite(name, fliphori)
