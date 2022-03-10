import random 
import cv2
import time


start = time.time()
question = random.randint(0,4);


counter = 0;
finger_count = 0;

buffer_result_for_single_qstn = []


# Generating new question
def generate_qstn(img):
    global counter;
    global question;
    counter += 1;
    
    if counter == 30:
        new_question = random.randint(1,4);
        if question == new_question:
            if question == 1:
                new_question = question + 1;
            else:
                new_question = question -1;
                
        counter = 0;
        question = new_question;
    
    display_question(img, question);
    return question;

#Edit image frame with question
def display_question(img, question):
    text = "show finger " + str(question)
    cv2.rectangle(img, (180, 20), (470, 60), (0, 255, 0), cv2.FILLED)
    cv2.putText(img,text,(200,50),cv2.FONT_HERSHEY_COMPLEX,1,(255, 0, 0),2)
    return img


def match_q_a(img, given_finger_count, asked_finger_count):
    
    global buffer_result_for_single_qstn;
    
    if given_finger_count == asked_finger_count:
        buffer_result_for_single_qstn.append(1);
    else:
        buffer_result_for_single_qstn.append(0);
