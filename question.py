import threading
import cv2
import time
import os
import HandTrackingModule as htm
import test as ts

wCam, hCam = 640, 480


cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)

pTime = 0
detector = htm.handDetector(detectionCon=0.75)

tipIds = [4, 8, 12, 16, 20]

# global variable x
x = 0

def increment():
	print("Ok")

def video():
    global pTime, tipIds, detector, img
    success, img = cap.read()
    img = cv2.flip(img, 1)
    img = detector.findHands(img, draw=True)
    lmList = detector.findPosition(img, handNo=0, draw=True)
    # print(lmList)
    
    print("next")

    if len(lmList) != 0:
        fingers = []
        print('List ', lmList)

        # Thumb Finger Count
        # if lmList[tipIds[0]][1] < lmList[tipIds[0] - 1][1]:
        #     fingers.append(1)
        # else:
        #     fingers.append(0)

        # 4 Fingers
        for id in range(1, 5):
            if lmList[tipIds[id]][2] < lmList[tipIds[id] - 2][2]:
                fingers.append(1)
            else:
                fingers.append(0)

        print(fingers)
        totalFingers = fingers.count(1)
        print(totalFingers)
        
        # Show the folder image over the video
        # h, w, c = overlayList[totalFingers - 1].shape
        # img[0:h, 0:w] = overlayList[totalFingers - 1]

        # cv2.rectangle(img, (20, 225), (170, 425), (0, 255, 0), cv2.FILLED)
        # cv2.putText(img, str(totalFingers), (45, 375), cv2.FONT_HERSHEY_PLAIN,
        #             10, (255, 0, 0), 25)
        ts.check_matching(img, totalFingers)

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(img, f'FPS: {int(fps)}',(500,50),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,0),3)
    


def main_task():
	global x
	# setting global variable x as 0
	x = 0

	# creating threads
	t1 = threading.Thread(target=video)
	# t2 = threading.Thread(target=video)

	# start threads
	t1.start()
	# t2.start()

	# # wait until threads finish their job
	# t1.join()
	# t2.join()

if __name__ == "__main__":
    i = 0
    while True:
        main_task()
        cv2.imshow("Image", img)
        cv2.waitKey(1)
        print("Iteration {0}: x = {1}".format(i,x))
        i = i +1
