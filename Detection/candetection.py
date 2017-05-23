import cv2
import numpy as np

can_cascade = cv2.CascadeClassifier('D:\opencv\opencv\sources\data\haarcascades\cascade.xml')

stream= cv2.Videocapture(0)

while true:
    ret, img = stream.read()
    gray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cans = can_cascade.detectMultiScale(gray, 50, 50)

    for (x,y,w,h) in cans:
        cv2.rectangle(img, (x,y), (x+w, y+h), (255,255,0),2)



    cv2.imshow('img', img)
    k=cv2.waitKey(1) &0xff
    if key == ord("q"):
		breakcamera.resolution = (600, 400)
		cv2.destroyAllWindows()


