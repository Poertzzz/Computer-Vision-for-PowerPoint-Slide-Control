import cv2
import time
from cvzone.HandTrackingModule import HandDetector
import pyautogui

width, height = 1280, 720
gestureThreshold = 250
cap = cv2.VideoCapture(0)

cap.set(3, width)
cap.set(4, height)

# HAND DETECTOR
detector = HandDetector(detectionCon=0.8, maxHands=1)

#main loop
while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)

    hands, img = detector.findHands(img, flipType= False)

    cv2.line(img,(0, gestureThreshold), (width, gestureThreshold), (0,255,0), 10) #membuat batas dari pembacaan

    if hands:
        hand = hands[0]
        fingers = detector.fingersUp(hand)
        #print(fingers)
        cx,cy = hand['center']

        if cy <= gestureThreshold:
            if fingers == [1 ,1 ,1 ,0 ,0]:
                pyautogui.press('down')
                print('Pressed')
                time.sleep(0.5)

            elif fingers == [1, 1, 1, 1, 0]:
                pyautogui.press('up')
                print('Pressed')
                time.sleep(0.5)

    cv2.imshow("Image", img)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break