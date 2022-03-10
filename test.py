import random 
import cv2
import time


start = time.time()
question = random.randint(0,4)
qstn_ans = []
right_ans = []

final_result = None

def show_qstn(img,count="none"):
    question = question_generate(count);
    
    if final_result == "pass":
        # show_result(img, "Verified");
        txt = "Verified"
    
    elif final_result == "failed":
        # show_result(img, "Unverified")
        txt = "Unverified"
    
    else:
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
    if start + 2 < end:
        # if len(qstn_ans) <= 5:
        new_question = random.randint(0,4)
        if question == new_question:
            if question == 0:
                new_question = question + 1
            else:
                new_question = question - 1
        
        question = new_question
        start = time.time()
        print("ans array", qstn_ans)
        answer_check(qstn_ans)
        print('New_question', new_question)
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
    global final_result
    global right_ans
    total_number = len(ans);
    right_ans_count = ans.count(1)
    try:
        right_percentage = (right_ans_count/total_number)*100;
    except:
        right_percentage = 0
    print("Percentage ", right_percentage);
    
    if(right_percentage > 50):
        right_ans.append(1)
    else:
        right_ans.append(0)
        
    if len(right_ans) == 5:
        tik_mark = right_ans.count(1)
        if tik_mark >= 4 and final_result == None:
            print ("Pass")
            right_ans.clear()
            final_result = "pass"
            return True
        elif tik_mark < 4 and final_result == None:
            print("Failed")
            right_ans.clear()
            final_result = "failed"
            return False
