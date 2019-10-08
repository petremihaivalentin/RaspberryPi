#importing the OpenCV(cv2), NumPy(numpy) and glob libraries
import cv2
import numpy as np
import glob

#creating an array out of the output .ppm files and sorting it in ascending order
#for some reason, I couldn't just call glob(something), even if I had imported the glob library
#instead, I call glob.glob(something) and it works

filenames = sorted(glob.glob('out.*.ppm'))

#using a variable to count the frames that are processed
i = 0

#creating a for loop to cycle through all the files in the filename array
for a in filenames:

	#creating a variable to store the information of each file of the array
	#the first argument is the file
	#the second argument is the storing mode, where '1' means BGR, '0' means GrayScale and '-1' means Unchanged
	
	img = cv2.imread(a, 1)

	#creating a variable that stores each pixel of the matrix of the original file (except the last 10 of each line and column)
	#but converted to Hue/Saturation/Value (HSV) mode

	hsv = cv2.cvtColor(img[:-10,:-10], cv2.COLOR_BGR2HSV)
		
	#setting lower and upper ranges for the Hue
	#the first arguments in the square brackets are variables and should be changed
	#according to the color of the object that should be detected in the image files
	#the specific values of these arguments can be calculated by opening the image file
	#using GIMP or other Image Manipulation Program, selecting the Colour Picker Tool,
	#selecting a pixel of the specific object, and inputting the BGR values (in this order)
	#into the converter.py program. The output of converter.py should represent the 
	#square brackets. The Saturation and Value values should be changed according to the
	#lighting system that is used in the experimental setup.
	#The second argument of the np.array function is the data type. The images' data type is uint8.
	#This means that it is an 8 bit integer, because the maximum value for Hue/Saturation/Value is 255.

	lower_range = np.array([52, 50, 75], dtype = np.uint8)
	upper_range = np.array([72, 255, 255], dtype = np.uint8)

	#creating a variable that represents the mask of the pixels from the hsv image, that 
	#have the Hue value between the lower_range and upper_range values.
	#The program will perform operations only using this mask from now on. 
	
	mask = cv2.inRange(hsv, lower_range, upper_range)
	
	#converting the HSV image to binary using Otsu's Binarization Method
	
	#firstly, I use the Gaussian Blur to make the image appear smoother
	#the first parameter is the source, the second are the distance (amount) of blur on X and Y
	#these parameters should be positive and odd
	#the third parameter is the standard deviation
	
	blur = cv2.GaussianBlur(mask,(5,5),0)
	#secondly, I convert the HSV image (with the blur applied) to binary and apply the threshold
	#using Otsu's Binarization Method. 
	#first parameter is the source image, the second is the treshold value which is used to classify pixel values
	#the third is the maxVal which represents the value to be given if pixel value is more than 
	#(or sometimes less than) the threshold value. The fourth is the used thresholding method.
	#This function has two outputs: a retValue and the image with the threshold applied.
	
	ret,thresh = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
	
	#Calculating the moments of the thresholded image
	
	M = cv2.moments(thresh)

	#Calculating the centre of the object using moments
	
	if M['m00'] != 0:
		cX = int(M['m10']/M['m00'])
		cY = int(M['m01']/M['m00'])
	else:
		cX, cY = 0, 0

	#Marking the centre of the object with a small black circle
	
	cv2.circle(mask, (cX, cY), 5, (0, 0, 0), -1)
	

	#Displaying the thresholded image, with the centre of the object found
	
	#cv2.imshow('final', mask)
	#cv2.waitKey(0)
	#cv2.destroyAllWindows()
	
	
	
	#Writing the matrix of the timestamp (in seconds) and the abscise of the centre of the object (in meters)
	#the 0.012/27 constant is the meters to pixels ratio, in this case. It should be updated for every different object
	#used in the experiment.
	
	f = open('centre_matrix.txt', 'a')
	if cY  != 0 or cY < 551:
		f.write(str(float(i)*0.0015) + ' ' + str(float(cX)*0.012/27) + '\n')		
		#f.write(str(cX) + ',' + str(cY) + '\n')
		i = i + 1
	f.close()


