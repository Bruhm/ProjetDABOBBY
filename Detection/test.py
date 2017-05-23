import numpy as np
import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

hauteur = 420
largeur = 420
cam = cv2.VideoCapture(0)
cam.set(3,420)
cam.set(4,420)

while(True):
    # Capture frame-by-frame
    ret, image = cam.read()

    # Our operations on the frame come here
    # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)


    face_cascade = cv2.CascadeClassifier('D:\opencv\opencv\sources\data\haarcascades\haarcascade_eye.xml')
    #face_cascade = cv2.CascadeClassifier('C:\Users\gueryacine\Desktop\Detection\can__cascade.xml')


    # Our operations on the frame come here
    face = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(face, 1.1,5)

    #for (x,y,w,h) in faces:
    	#cv2.rectangle(image,(x,y),(x+w,y+h),(255,255,0),2)
    	
    	
    	


    
    #Draw a rectangle around every found face
    for (x,y,w,h) in faces:
            cv2.circle(image,((x+w/2),(y+h/2)), 5, (0,0,255), -1)
            #print "Found "+str(len(faces))+" face(s)"
            print str(x+w/2)+" x"
            print str(y+h/2)+" y"
            #print str(w)+" w"
            #print str(h)+" h"
            cv2.line(image, (210,0), (210,210), (0,0,255), 2)
            
    # Display the resulting frame
    cv2.imshow('frame',image)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cam.release()
