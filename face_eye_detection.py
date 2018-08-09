# -*- coding: utf-8 -*-
"""
Created on Wed Aug  8 14:50:50 2018

@author: Yu Wang
"""
import cv2

# load the CascadeClassifier
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier("haarcascade_eye.xml")

# define a function that does the detection

def detection(gray, frame):
    
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    
    for x,y,w,h in faces:
        cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), 3)
        
        roi_gray = gray[y:y+h, x:x+w] # We get the region of interest in the black and white image.
        roi_frame = frame[y:y+h, x:x+w] # We get the region of interest in the colored image.
        eyes = eye_cascade.detectMultiScale(roi_gray, 1.1, 3) # We apply the detectMultiScale method to locate one or several eyes in the image.
        for (ex, ey, ew, eh) in eyes: # For each detected eye:
            cv2.rectangle(roi_frame,(ex, ey),(ex+ew, ey+eh), (255, 0, 0), 2)
    
    
    return frame

# open camera, input frame, implement detection func, terminate until press q
    
video_cap = cv2.VideoCapture(0)

while True:
    
    _, frame = video_cap.read()
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    img = detection(gray, frame) # return frame with detected faces and eyes
    
    cv2.imshow("video", img)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_cap.release()
cv2.destroyAllWindows()
    