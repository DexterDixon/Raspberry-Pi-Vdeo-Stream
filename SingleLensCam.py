#Created by: Dexter Dixon
#Video stream using a single lens camera
import cv2
import numpy as np

cv2.namedWindow("Vission")

camera1 = cv2.VideoCapture(0)

camera1.set(3,480);
camera1.set(4,320);


while(True):
    # Capture frame-by-frame
    ret, frame = camera1.read()


    #Display the resulting frame
    cv2.imshow('Vission',frame)

    key = cv2.waitKey(20)
    if key == 27: # exit on ESC
        break

cv2.destroyWindow("Vission")
vc.release()
