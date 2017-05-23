# import the necessary packages
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
import numpy as np
 
#require XML classifiers
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

# initialize the camera and grab a reference to the raw camera capture
camera = PiCamera()
camera.resolution = (320, 240)

camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(320, 240))

 
# allow the camera to warmup
time.sleep(0.1)
 
# capture frames from the camera
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):

	# grab the raw NumPy array representing the image, then initialize the timestamp
	#and occupied/unoccupied text
	image = frame.array

	# Convert BGR to HSV
	hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        
	# define range of blue color in HSV
        lower_blue = np.array([110,50,50])
        upper_blue = np.array([130,255,255])

        # Threshold the HSV image to get only blue colors
        mask = cv2.inRange(hsv, lower_blue, upper_blue)
	
	# Bitwise-AND mask and original image
	res = cv2.bitwise_and(image,image, mask= mask)

	#Load a cascade file for detecting faces
	#face_cascade = cv2.CascadeClassifier('/usr/share/opencv/haarcascades/haarcascade_frontalface_alt.xml')
	can_cascade = cv2.CascadeClassifier('/home/pi/Desktop/Script_Arduino_Rpi/can_cascade.xml')
	#convert to grayscale
	#face=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
        can=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    
	#Look for faces in the image using the loaded cascade file
	#faces = face_cascade.detectMultiScale(face, 1.1, 5)
        cans = can_cascade.detectMultiScale(can, 2, 5)
        
	#print "Found "+str(len(faces))+" face(s)"
	print "Found "+str(len(cans))+" can(s)"

	#Draw a rectangle around every found face
	for (x,y,w,h) in cans:
    		cv2.rectangle(image,(x,y),(x+w,y+h),(255,255,0),2)

	# show the frame
	cv2.imshow("cans", image)

	#cv2.imshow("HSV Mask", mask)
        #cv2.imshow('res',res)
	key = cv2.waitKey(1) & 0xFF
        

	# clear the stream in preparation for the next frame
	rawCapture.truncate(0)
 
	# if the `q` key was pressed, break from the loop
	if key == ord("q"):
		breakcamera.resolution = (600, 400)
		cv2.destroyAllWindows()
