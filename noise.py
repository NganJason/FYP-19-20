from PIL import Image
import cv2
import numpy as np
import os
from skimage.transform import warp,AffineTransform
from skimage import io
from skimage.util import random_noise

try:
    if not os.path.exists('datablur'):
        os.makedirs('datablur')
except OSError:
    print ('Error: Creating directory of data')

image_folder = '/Users/jasonngan/Desktop/training2/data'
number = 3019

for n, image_file in enumerate(os.scandir(image_folder)):
	if number % 5 == 0:
		image = cv2.imread(image_file.path)
		blur = cv2.blur(image,(3,3))
		name = './datablur/blur' + str(number) + '.jpg'
		print ('Creating...' + name)
		cv2.imwrite(name,image)
	number+=1


# img = cv2.imread('image590.jpg')
# noisy = random_noise(img)
# name='hihi1.jpg'
# io.imsave(name,warp_image)

# rows,cols = img.shape

# M = np.float32([[1,0,100],[0,1,50]])
# dst = cv2.warpAffine(img,M,(cols,rows))

cv2.imwrite(name,img)


