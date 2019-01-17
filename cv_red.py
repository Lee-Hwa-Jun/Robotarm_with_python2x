#-*- coding:utf-8 -*-
import cv2
import numpy as np
import time
cap = cv2.VideoCapture(0)

while True:
    ret,frame = cap.read()
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    lower_red = np.array([150,150,50])
    upper_red = np.array([200,255,180])

    mask = cv2.inRange(hsv,lower_red,upper_red)
    res = cv2.bitwise_and(frame,frame,mask=mask)
    # kernel = np.ones((15,15),np.float32)/255
    # smoothed = cv2.filter2D(res,-1,kernel)
    blur = cv2.GaussianBlur(res,(15,15),0)

    blur = np.array(blur)
    li = np.array(np.where(blur > [150,150,50]))

    x,y = mask.shape
    cv2.line(mask,(0,int(x/3)),(y,int(x/3)),(255,0,0),1)
    cv2.line(mask,(0,int(x/3*2)),(y,int(x/3*2)),(255,0,0),1)
    cv2.line(mask,(int(y/3),0),(int(y/3),x),(255,0,0),1)
    cv2.line(mask,(int(y/3*2),0),(int(y/3*2),x),(255,0,0),1)

    try:
        x1 = li[1].min(axis=0)
        y1 = li[0].min(axis=0)
        x2 = li[1].max(axis=0)
        y2 = li[0].max(axis=0)

        cv2.rectangle(mask,(x1,y1),(x2,y2),(255,0,0),3)

        xc=int((x1+x2)/2)
        yc=int((y1+y2)/2)
        cv2.circle(mask,(xc,yc),30,(255,255,255),3)

        RLposition = "center"
        TBposition = "center"
        if(xc<y/3):
            RLposition = "left"
        elif(xc>y/3*2):
            RLposition = "right"
        if(yc<x/3):
            TBposition = "top"
        elif(yc>x/3*2):
            TBposition = "bottom"

        print(RLposition,TBposition)
    except:
        pass

    cv2.imshow('test', mask)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()