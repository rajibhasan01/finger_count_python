import random 
import cv2
import time

start = time.time()
question = random.randint(0,4)

def check_matching(img, count):
    question = question_generate()
    txt = "Show " + str(question);
    show_image(img, txt)
    
    
    print("Question",question);
    

    
# Edit the Frame
def show_image(img,text,color = (0,0,0)):
    cv2.rectangle(img, (250, 20), (470, 60), (0, 255, 0), cv2.FILLED)
    cv2.putText(img,text,(300,50),cv2.FONT_HERSHEY_COMPLEX,1,color,2)
    return img



# Generate Question
def question_generate():
    end = time.time();
    global start
    global question
    print('start', start)
    print("End", end)
    if start + 5 < end:
        question = random.randint(0,4)
        start = time.time()
        return question
    
    return question


# Answer Check