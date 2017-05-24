# -*- coding: cp1252 -*-
from math import *
import threading
from enum import Enum
''' Global Variable '''
resolutionX = 320
resolutionY = 240
''' END Global Variable  '''

def ThreadStart():
    camera = Camera()
    coloraquisition = ColorAquisition(camera)
    tCamera = threading.Thread(target=camera.start, args=())
    tcam.start()
    tColorDetection = threading.Thread(target=coloraquisition.Recherche)
    tcolor.start()
    
class Camera():
    image = None
    def __init__(self):
        self.camera = PiCamera()
        self.camera.resolution = (resolutionX, resolutionY)
        self.camera.framerate = 32
        self.rawCapture = PiRGBArray(camera, size=camera.resolution )
    def start()
        for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
            image = frame.array

class ColorAquisition:
    def __init__(self,color,camera):
        self.color = color
        self.image = camera.image
    def angle(x,y):
        return degrees(atan2(160-x,120-y))
            
    def Recherche():
        while(true):
            '''=
                # 1 - Reconnaitre une cannette avec la couleur
            '''
            blur = cv2.blur(image, (3,3))
            hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
            lower_color , upper_color= colortoRVB(self.color)

            '''=
                Detection de Contour
            '''
            threshw=cv2.inRange(hsv, lower_color, upper_color)
            image, contours,hierarchy = cv2.findContours(threshw,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
            
            max_area = 0
            best_cnt = 1
            areas = [cv2.contourArea(c) for c in contours]

            '''=
                calcule du point de repére et du carée
            '''
            for cnt in contours:
                    area = cv2.contourArea(cnt)
                    if area > max_area:
                            max_area = area
                            best_cnt = cnt
            if areas :
                cnt2 = contours[np.argmax(areas)]
                x,y,w,h = cv2.boundingRect(cnt2)
                cv2.rectangle(blur,(x,y),(x+w,y+h),(0,255,255),2)
                angle(x+w/2,y+h/2)
                surface = w*h;
                print angle
                print surface
        
    def colortoRVB(color):
        if color == "red":
            lower_color=np.array([150,150,50],dtype=np.uint8)
            upper_color=np.array([180,255,255],dtype=np.uint8)
        elif color == "yellow":
            lower_color=np.array([20,100,100],dtype=np.uint8)
            upper_color=np.array([30,255,255],dtype=np.uint8)
    return lower_color,upper_color




class Deplacement:
    def __init__(self,):
        self.countDetection = 0
        self.ListPos =[]


    
        
#class comportement():
#def esquiveObstacle():
