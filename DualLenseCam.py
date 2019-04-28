#Created by: Dexter Dixon
#Video stream using a dual lens camera
import cv2
import numpy as np

cv2.namedWindow("Vission")

camera1 = cv2.VideoCapture(0)
camera2 = cv2.VideoCapture(1)

camera1.set(3,480);
camera1.set(4,320);

camera2.set(3,480);
camera2.set(4,320);

while(True):
  # Capture frame-by-frame
    ret, frame1 = camera1.read()
    ret, frame2 = camera2.read()

    final = cv2.hconcat([frame1, frame2])

    #Display the resulting frame
    cv2.imshow('Vission',final)

    key = cv2.waitKey(20)
    if key == 27: # exit on ESC
        break

cv2.destroyWindow("Vission")
vc.release()
