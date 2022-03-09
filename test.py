import random 
import cv2
import time


start = time.time()
question = random.randint(0,4)
qstn_ans = []
right_ans = []

def show_qstn(img,count="none"):
    question = question_generate(count);
    txt = "Show " + str(question);
    show_image(img, txt);
    
    # print("Question",question);
    # print("Count", count);
    
    # # if len(qstn_ans) <= 5:
    # if count == question:
    #     result = "OK";
    #     qstn_ans.append(1);
    #     show_result(img, result);
    #     # question = question_generate(result);
    # else:       
    #     print("Failed")
    #     result = "Failed";
    #     qstn_ans.append(0);
    #     show_result(img, result);
        
    # print("Question Ans ", qstn_ans);
    
    
def check_matching(img, count):
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
    
    

    
# Edit the Frame
def show_image(img,text,color = (0,0,0)):
    cv2.rectangle(img, (250, 20), (470, 60), (0, 255, 0), cv2.FILLED)
    cv2.putText(img,text,(300,50),cv2.FONT_HERSHEY_COMPLEX,1,color,2)
    return img

def show_result(img, result, color =(0,0,0)):
    cv2.putText(img,result,(300,100),cv2.FONT_HERSHEY_COMPLEX,1,color,2)
    return img

# Generate Question
def question_generate(count):
    end = time.time();
    global start
    global question
    global qstn_ans
    # print('start', start)
    # print("End", end)
    if start + 3 < end:
        # if len(qstn_ans) <= 5:
        question = random.randint(0,4)
        start = time.time()
        print("ans array", qstn_ans)
        answer_check(qstn_ans)
        return question
    
    if count != "none":
        if question == count:
            print("True")
            qstn_ans.append(1);
        else:
            print("False")
            qstn_ans.append(0);
    return question


# Answer Check
def answer_check(ans):
    total_number = len(ans);
    right_ans_count = ans.count(1)
    try:
        right_percentage = (right_ans_count/total_number)*100;
    except:
        right_percentage = 0
    print("Percentage ", right_percentage);
    
    if(right_percentage > 70):
        right_ans.append(1)
    else:
        right_ans.append(0)
        
    if len(right_ans) == 5:
        tik_mark = right_ans.count(1)
        if tik_mark >= 4:
            print ("Pass")
            return True
        else:
            print("Failed")
            return False
    global qstn_ans
    qstn_ans.clear()
    