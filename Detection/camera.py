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


moveSleepDelay = 0.1
moveSteps = 20

canetteTrouvee = False

#Resolution camera
resolutionX = 320
resolutionY = 240

#Load a cascade file for detecting faces

camera = PiCamera()
camera.resolution = (resolutionX, resolutionY)
camera.framerate = 32
camera.rotation = 90
rawCapture = PiRGBArray(camera, size=camera.resolution )
# allow the camera to warmup
time.sleep(0.1)

#init la position du carre a 0

positions = ''
font = cv2.FONT_HERSHEY_SIMPLEX
center = []


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

        def send_message(self, message):
                print('notification subject')
                self.notify_all(message)
        
        x = 0
        y = 0
        w = 0
        h = 0
        def angle(self,x,y):
                return degrees(atan2(160-x,120-y))
        def threadScanVideo(self,mutexVideo):
                #print "VIDEO"
                               
                '''
                ##########
                # 0 - Set la gamme de couleur a rechercher avec la camera
                ##########
                '''
                color = "yellow"
                if color == "red":
                        lower_color=np.array([150,150,50],dtype=np.uint8)
                        upper_color=np.array([180,255,255],dtype=np.uint8)
                elif color == "yellow":
                        lower_color=np.array([20,100,100],dtype=np.uint8)
                        upper_color=np.array([30,255,255],dtype=np.uint8)
                        
                # capture frames from the camera
                for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
                        image = frame.array
                        #gauche = cv2.line(image, ((resolutionX /2)-40, resolutionY), ((resolutionX/2)-40, 0), (255,0,0), 2)
                        #droite = cv2.line(image, ((resolutionX /2)+40, resolutionY), ((resolutionX/2)+40, 0), (255,255,0), 2)
                        #hauteur = cv2.line(image, (0, (resolutionY /2)), ((resolutionX, resolutionY/2)), (0,255,0), 2)

                        #face=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
                        #faces = face_cascade.detectMultiScale(face, 1.3, 5)
                        
                        
                        
                        '''
                        ##########
                        # 1 - Cherche une cannette en fonction de la couleur
                        ##########
                        '''
                        blur = cv2.blur(image, (3,3))
                        hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

                        threshw=cv2.inRange(hsv, lower_color, upper_color)
                        #threshw=cv2.inRange(hsv, lower_yellow, upper_yellow)

                        # find contours in the threshold image
                        image, contours,hierarchy = cv2.findContours(threshw,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)

                        # finding contour with maximum area and store it as best_cnt
                        max_area = 0
                        best_cnt = 1
                        areas = [cv2.contourArea(c) for c in contours]
                        for cnt in contours:
                                area = cv2.contourArea(cnt)
                                if area > max_area:
                                                max_area = area
                                                best_cnt = cnt
                        
                        M = cv2.moments(best_cnt)
                        cx,cy = int(M['m10']/M['m00']), int(M['m01']/M['m00'])
                        cv2.circle(blur,(cx,cy),10,(0,0,255),-1)

                        '''
                        ##########
                        # 3 - Check si le rebot est assez proche pour attraper la canette
                        ##########
                        '''
                        if areas :
                                cnt2 = contours[np.argmax(areas)]
                                x,y,w,h = cv2.boundingRect(cnt2)
                                cv2.rectangle(blur,(x,y),(x+w,y+h),(0,255,255),2)
                                Angle = self.angle((x+w/2),(y+h/2))
                                surface = w*h
                                print(Angle)
                                print(surface)
                                cameraClass.send_message(Angle) 


                                #if tw*th > 26000:
                                        #pinAttraperRelacherCanette("attraper")
                        
                        



                        # -- Montre l'image
                        #cv2.imshow("face", image)
                        #key = cv2.waitKey(1) & 0xFF
                        #rawCapture.truncate(0)     
                        cv2.imshow("can", image)
                        cv2.imshow("frame", blur)
                        key = cv2.waitKey(1) & 0xFF
                        rawCapture.truncate(0)
                 
                        # if the `q` key was pressed, break from the loop
                        if key == ord("q"):
                                breakcamera.resolution = (600, 400)
                                cv2.destroyAllWindows()
    
    
                while True:
                        if mutexVideo.wait(1):
                                print("[HALT] Video thread")
                                break
                        #print "Video"

class CameraObserver(Observer):
    def notify(self, message):
        print(message)
    
# Interrupt Signal
halt = False
def stopAll(signum, frame):
    print("Interrupt!!")
    global halt
    halt = True
    mutexVideo.set()
signal.signal(signal.SIGINT, stopAll)

try:
    tScan.start()

    while not halt:
        continue
    print("[HALT] Main thread")

except Exception as ex:
        print(ex)
