import cv2
import os

# try:
#     if not os.path.exists('datagrey'):
#         os.makedirs('datagrey')
# except OSError:
#     print ('Error: Creating directory of data')

# image_folder = '/Users/jasonngan/Desktop/training2/data'
# number = 3623

# for n, image_file in enumerate(os.scandir(image_folder)):
# 	image = cv2.imread(image_file.path)
# 	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# 	name = './datagrey/grey' + str(number) + '.jpg'
# 	print ('Creating...' + name)
# 	cv2.imwrite(name, gray)
# 	number+=1

image = cv2.imread('image598.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
name = 'grayimage.jpg'

cv2.imwrite(name, gray)