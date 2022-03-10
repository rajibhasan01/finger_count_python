import cv2
import time
import os
import HandTrackingModule as htm
import test as ts
import question as qs
import random
import threading


wCam, hCam = 640, 480;
counter = 0;

cap = cv2.VideoCapture(0);


detector = htm.handDetector(detectionCon=0.75);
tipIds = [4, 8, 12, 16, 20];

question_count = 0;
display_duration = 200;
q1_count = 200;
q2_count = 400;
q3_count = 600;
q4_count = 800;
q = None;

quesetion_no = 0;

qstn_ans_array = []

current_qstn = random.randint(1,5);
prev_qstn = 0;
buffer_result_for_single_qstn = [];


def show_random(img, count, prev_qstn):
    global current_qstn;

    if count >= 200 and count <= 399:
       cv2.putText(img, str(prev_qstn), (45, 100), cv2.FONT_HERSHEY_PLAIN,
                    10, (255, 0, 0), 2);
       return prev_qstn;
       
    if count >= 400 and count <= 599:
        if count == 400:
            current_qstn = random.randint(1,5);
        cv2.putText(img, str(current_qstn), (45, 100), cv2.FONT_HERSHEY_PLAIN,
                    10, (255, 0, 0), 2);
        return current_qstn;
    
    if count >= 600 and count <= 799:
        if count == 600:
            current_qstn = random.randint(1,5);
        cv2.putText(img, str(current_qstn), (45, 100), cv2.FONT_HERSHEY_PLAIN,
                    10, (255, 0, 0), 2);
        return current_qstn;

    if count >= 800 and count <= 999:
        if count == 800:
            current_qstn = random.randint(1,5);
        cv2.putText(img, str(current_qstn), (45, 100), cv2.FONT_HERSHEY_PLAIN,
                    10, (255, 0, 0), 2);
        return current_qstn;


# Decision Making for verification
def making_decision(result_array):
    right_ans = result_array.count(1);
    
    if right_ans >= 3:
        cv2.putText(img, str("Verified"), (180, 200), cv2.FONT_HERSHEY_PLAIN,
                    10, (255, 0, 0), 2);
        print("verified")
    else:
        cv2.putText(img, str("Unverified"), (180, 200), cv2.FONT_HERSHEY_PLAIN,
                    10, (255, 0, 0), 2);
        print("Unverified")
    


# Checking percentange of answer
def check_correct_ans(buffer_result_collection_array):
    global buffer_result_for_single_qstn;
    total_number = len(buffer_result_collection_array);
    correct_ans = buffer_result_collection_array.count(1);
    try:
        correct_ans_percentage = (correct_ans / total_number) * 100;
    except:
        correct_ans_percentage = 0;
    
    if correct_ans_percentage > 40:
        qstn_ans_array.append(1);
    else:
        qstn_ans_array.append(0)
    
    making_decision(qstn_ans_array);
    buffer_result_for_single_qstn.clear();
    print("Percentage ", correct_ans_percentage);




# Matching question answer
def match_q_a(counter, given_finger_count, asked_finger_count = None):
    
    global buffer_result_for_single_qstn;
    
    if counter == 400 or counter == 600 or counter == 800 or counter == 1000:
        check_correct_ans(buffer_result_for_single_qstn);
    
    else:
        if given_finger_count == asked_finger_count:
            buffer_result_for_single_qstn.append(1);
            print("True")
        else:
            buffer_result_for_single_qstn.append(0);
            print("false")


while True:
    
    success, img = cap.read();
    img = cv2.flip(img, 1);
    img = detector.findHands(img, draw=True);
    lmList = detector.findPosition(img, handNo=0, draw=True);
    
    counter += 1;
    if counter >= q1_count and counter <= q2_count -1:
        q = show_random(img, counter, current_qstn);
        quesetion_no = 1;
    
    if counter >= q2_count and counter <= q3_count -1:
        q = show_random(img, counter, current_qstn);
        quesetion_no = 2;
        
    if counter >= q3_count and counter <= q4_count-1:
        q = show_random(img, counter, current_qstn);
        quesetion_no = 3;
        
    if counter >= q4_count and counter <= 1000:
        q = show_random(img, counter, current_qstn);
        quesetion_no = 4;
    

    # print("counter", counter);

    if len(lmList) != 0:
        fingers = []

        # Thumb Finger Count
        if lmList[tipIds[0]][1] < lmList[tipIds[0] - 1][1]:
            fingers.append(1)
        else:
            fingers.append(0)

        # 4 Fingers
        for id in range(1, 5):
            if lmList[tipIds[id]][2] < lmList[tipIds[id] - 2][2]:
                fingers.append(1)
            else:
                fingers.append(0)

        totalFingers = fingers.count(1)
        
            
        # q = show_random(img);
        
        if totalFingers == 5:
            cv2.putText(img, "five given", (45, 100), cv2.FONT_HERSHEY_PLAIN,
                    10, (255, 0, 0), 2)


        # cv2.rectangle(img, (20, 225), (170, 425), (0, 255, 0), cv2.FILLED)
        # cv2.putText(img, str(totalFingers), (45, 375), cv2.FONT_HERSHEY_PLAIN,
        #             10, (255, 0, 0), 25)
        
        match_q_a(counter, totalFingers, q);
        
    cv2.imshow("Image", img)
    cv2.waitKey(1)
    

