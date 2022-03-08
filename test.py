import random 
import cv2
import time

start = time.time()
question = random.randint(0,4)
qstn_ans = []

def check_matching(img, count):
    global qstn_ans;
    question = question_generate();
    txt = "Show " + str(question);
    show_image(img, txt);
    
    print("Question",question);
    print("Count", count);
    
    # if len(qstn_ans) <= 5:
    if count == question:
        result = "OK";
        qstn_ans.append(1);
        show_result(img, result);
        # question = question_generate(result);
    else:       
        print("Failed")
        result = "Failed";
        qstn_ans.append(0);
        show_result(img, result);
        
    print("Question Ans ", qstn_ans);
        

    
# Edit the Frame
def show_image(img,text,color = (0,0,0)):
    cv2.rectangle(img, (250, 20), (470, 60), (0, 255, 0), cv2.FILLED)
    cv2.putText(img,text,(300,50),cv2.FONT_HERSHEY_COMPLEX,1,color,2)
    return img

def show_result(img, result, color =(0,0,0)):
    cv2.putText(img,result,(300,100),cv2.FONT_HERSHEY_COMPLEX,1,color,2)
    return img

# Generate Question
def question_generate(result = "failed"):
    end = time.time();
    global start
    global question
    global qstn_ans
    print('start', start)
    print("End", end)
    if start + 5 < end or result == "OK":
        # if len(qstn_ans) <= 5:
        question = random.randint(0,4)
        start = time.time()
        return question
    
    return question


# Answer Check