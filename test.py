import random 
import cv2


def check_matching(img, txt, count):
    index_question = random.randint(0,5)
    txt = txt + str(index_question);
    show_image(img, txt)
    
    print(index_question,question_bank(index_question));
    

def question_bank(index):
    questions = [1,2,3,4,5,6]
    return questions[index]


    
    
def show_image(img,text,color = (0,0,255)):
    cv2.putText(img,text,(10,50),cv2.FONT_HERSHEY_COMPLEX,1,color,2)
    return img
