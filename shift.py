from PIL import Image
import cv2
import numpy as np
import os
from skimage.transform import warp,AffineTransform
from skimage import io

try:
    if not os.path.exists('datashift'):
        os.makedirs('datashift')
except OSError:
    print ('Error: Creating directory of data')

image_folder = '/Users/jasonngan/Desktop/training2/data'
number = 2415

for n, image_file in enumerate(os.scandir(image_folder)):
	if number % 4 == 0:
		image = cv2.imread(image_file.path,0)
		transform = AffineTransform(translation=(-200,0))
		warp_image = warp(image,transform, mode="wrap")	
		name = './datashift/shift' + str(number) + '.jpg'
		print ('Creating...' + name)
		io.imsave(name,warp_image)
	number+=1


# image = cv2.imread('image598.jpg')
# transform = AffineTransform(translation=(-200,0))
# warp_image = warp(image,transform, mode="wrap")	
# name = 'shiftimage.jpg'

# io.imsave(name,warp_image)





# img = cv2.imread('/Users/jasonngan/Desktop/training2/data/image3.jpg',0)
# transform = AffineTransform(translation=(-300,0))
# warp_image = warp(img,transform, mode="wrap")
# name='hihi.jpg'
# io.imsave(name,warp_image)

# rows,cols = img.shape

# M = np.float32([[1,0,100],[0,1,50]])
# dst = cv2.warpAffine(img,M,(cols,rows))

# cv2.imshow("hi",warp_image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


