import cv2 , time
import numpy as np
import pyautogui
import pygame
from pynput.keyboard import Key, Controller

keyboard = Controller()

# defining video capture object

video = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_alt2.xml')

# defining previous frame

prev = "None"
delta = 7

while True:
    check,frame = video.read()

    frame = cv2.GaussianBlur(frame, (3, 3), 0)

    frame=cv2.flip(frame,1)
    height, width, _ = np.shape(frame)
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)


   # cv2.line(frame, (int(width/3), 0), (int(width/3), int(height)), (0, 255, 255), 4)
   # cv2.line(frame, (int((2*width) / 3), 0), (int((2*width) / 3), int(height)), (0, 255, 255), 4)
    cv2.line(frame,(0,int(height/3)-30),(width,int(height/3)-30),(0,255,255),4)
    cv2.line(frame,(0,int((2*height)/3)),(width,int((2*height)/3)),(0,255,255),4)

    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3)

    right = False
    left = False
    up = False
    down = False

    for (x, y, w, h) in faces:
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = frame[y:y + h, x:x + w]
        img = cv2.rectangle(frame, (x, y), (x + w, y + h), (0,255,0), 4) # box for face

        if ((x>int((2*width)/3))):# and (x+w<int((2*width)/3))):

           if (right==False and prev!="right"):
              # print("right")
              right=True
              prev="right"
              # pyautogui.press('right')
              break

        elif (x+w<int(width/3)):

           if (left==False and prev!="left"):
               # print("left")
               left=True
               prev="left"
               #pyautogui.press('left')
               break

        elif ((int((y+h))<int(height/3)-30)):# and (x>int(width/3)) and (x+h<int((2*width)/3))):

           if (up==False and prev!="up"):# and prev!="left" and prev!="right"):
               print("up")
               up=True
               prev="up"
               #start = time.time()
               #while time.time() - start <1:
                   #pyautogui.press('up')
               #cv2.waitKey(20)
               keyboard.press(Key.up)
               time.sleep(1.1)
               keyboard.release(Key.up)
               break

        elif ((y>int((2*height)/3))):# and (x>int(width/3)) and (x+h<int((2*width)/3))):

           if (down==False and prev!="down"):# and prev!="left" and prev!="right"):
               print("down")
               down = True
               prev="down"
               #pyautogui.press('down')
               keyboard.press(Key.down)
               time.sleep(1.1)
               keyboard.release(Key.down)
               break

        else:
            down = False
            up = False
            prev = "None"

    cv2.imshow("Detecting Motion",frame)
    cv2.imshow("GrayFrameCapture",gray)
    key=cv2.waitKey(1)
    if key==ord('q') :
        break


video.release()
cv2.destroyAllWindows()