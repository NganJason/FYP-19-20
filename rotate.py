from PIL import Image
import cv2
import os

try:
    if not os.path.exists('datarotate'):
        os.makedirs('datarotate')
except OSError:
    print ('Error: Creating directory of data')

image_folder = '/Users/jasonngan/Desktop/training2/data'
number = 603

for n, image_file in enumerate(os.scandir(image_folder)):
	if number % 2 == 0:
		image = cv2.imread(image_file.path)
		(h,w) = image.shape[:2]
		center = (w/2,h/2)
		angle180 = 180
		scale = 1.0
		m = cv2.getRotationMatrix2D(center, angle180, scale)
		rotated180 = cv2.warpAffine(image, m, (w,h))
		name = './datarotate/rotate' + str(number) + '.jpg'
		print ('Creating...' + name)
		cv2.imwrite(name, rotated180)
	number+=1

# image = cv2.imread('image598.jpg')
# (h,w) = image.shape[:2]
# center = (w/2,h/2)
# angle180 = 180
# scale = 1.0
# m = cv2.getRotationMatrix2D(center, angle180, scale)
# rotated180 = cv2.warpAffine(image, m, (w,h))
# name = 'rotateimage.jpg'

# cv2.imwrite(name, rotated180)




