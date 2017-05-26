from picamera.array import PiRGBArray
from picamera import PiCamera
from obserBiblio import Subject
from obserBiblio import Observer
import cv2
import numpy as np
import multiprocessing
import signal
import time
import threading
import sys
from math import *
from enum import Enum
import collections

Point = collections.namedtuple('Point',['x','y'])
mutexVideo = threading.Event()

#Resolution camera
resolutionX = 320
resolutionY = 240

camera = PiCamera()
camera.resolution = (resolutionX, resolutionY)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=camera.resolution )
# allow the camera to warmup
time.sleep(0.1)


class Camera(Subject):
        def __init__(self, *args, **kwargs):
                self._observers = []

        def register(self, observer):
                self._observers.append(observer)

        def unregister(self, observer):
                self._observers.remove(observer)

        def notify_all(self, message):
                for observer in self._observers:
                    observer.notify(message)
        
        def notify_observer(self, message,ordre):
                     self._observers[ordre].notify(message)

        def send_message(self, message):
                print 'notification subject'
                self.notify_all(message)
        
        x = 0
        y = 0
        w = 0
        h = 0
        def angle(self,x,y):
                return degrees(atan2(160-x,120-y))
        def threadScanVideo(self,mutexVideo):
                               
                # capture frames from the camera
                for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):

                        '''
                        ##########
                        # 1 - Intialisation de l'image
                        ##########
                        '''

                        image = frame.array                        
                        blur = cv2.blur(image, (3,3))
                        hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
                        

                        '''
                        ##########
                        # 2 - Detection de couleur
                        ##########
                        '''
                        self.ColorDetection(image,hsv,"red",0)
                        self.ColorDetection(image,hsv,"yellow",1)
                        self.ColorDetection(image,hsv,"blue",2)


                        '''
                        ##########
                        # 3 - Affichage
                        ##########
                        '''
                        #TODO : delete
                        #cv2.imshow("can", image)
                        cv2.imshow("frame", blur)
                        key = cv2.waitKey(1) & 0xFF
                        rawCapture.truncate(0)
                 
                        # if the `q` key was pressed, break from the loop
                        
                        if key == ord("q"):
                                breakcamera.resolution = (600, 400)
                                cv2.destroyAllWindows()
                        #TODO: FINISH HER
	
	
                while True:
                        if mutexVideo.wait(1):
                                print "[HALT] Video thread"
                                break
                        #print "Video"

        def ColorDetection(self,image,hsv,color,ordre):
                threshw=cv2.inRange(hsv, self.Color_BGR(color).x, self.Color_BGR(color).y)
                image, contours,hierarchy = cv2.findContours(threshw,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
                areas = [cv2.contourArea(c) for c in contours]
                if areas :
                        cnt2 = contours[np.argmax(areas)]
                        x,y,w,h = cv2.boundingRect(cnt2)
                        Angle = self.angle((x+w/2),(y+h/2))
                        surface = w*h
                        p = Point(Angle,surface)
                        cameraClass.notify_observer(p,ordre)
         
        def Color_BGR(self,color):
                if color == "red":
                        lower_color=np.array([150,150,50],dtype=np.uint8)
                        upper_color=np.array([180,255,255],dtype=np.uint8)
                elif color == "yellow":
                        lower_color=np.array([20,100,100],dtype=np.uint8)
                        upper_color=np.array([30,255,255],dtype=np.uint8)
                elif color == "blue": #TODO: Change proprity of color
                        lower_color=np.array([20,100,100],dtype=np.uint8)
                        upper_color=np.array([30,255,255],dtype=np.uint8)
                p = Point(lower_color,upper_color)
                return p
        
                

class RedObserver(Observer):
    def notify(self, message):
        print message[0] + "  " + message[0]  
        print "RedObserver"

class yellowObserver(Observer):
    def notify(self, message):
        print message[0] + "  " + message[0]
        print "yellowObserver"
        
class BlueObserver(Observer):
    def notify(self, message):
        print message[0] + "  " + message[0]
	print "BlueObserver"
# Interrupt Signal
halt = False
def stopAll(signum, frame):
	print "Interrupt!!"
	global halt
	halt = True
	mutexVideo.set()
signal.signal(signal.SIGINT, stopAll)


# mutexVideo.set() # Stop le threadScanVideo
# stopAll() # Stop all threads
cameraClass = Camera()
RedObserver = RedObserver()
yellowObserver = yellowObserver()
BlueObserver = BlueObserver()
cameraClass.register(RedObserver)
cameraClass.register(yellowObserver)
cameraClass.register(BlueObserver)
threadCamera = threading.Thread(target=cameraClass.threadScanVideo, args=([mutexVideo]))

try:
	threadCamera.start()

	while not halt:
		continue
	print "[HALT] Main thread"

except Exception as ex:
		print ex
