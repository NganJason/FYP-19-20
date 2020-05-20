from PIL import Image
import cv2
import os

try:
    if not os.path.exists('datafliphori'):
        os.makedirs('datafliphori')
except OSError:
    print ('Error: Creating directory of data')

image_folder = '/Users/jasonngan/Desktop/training2/data'
number = 1207

for n, image_file in enumerate(os.scandir(image_folder)):
	if number % 3 == 0:
		image = cv2.imread(image_file.path)
		fliphori = cv2.flip(image, 1)
		name = './datafliphori/fliphori' + str(number) + '.jpg'
		print ('Creating...' + name)
		cv2.imwrite(name, fliphori)
	number+=1

# image = cv2.imread('image598.jpg')
# fliphori = cv2.flip(image, 1)
# name = 'fliphoriimage.jpg'

# cv2.imwrite(name, fliphori)


