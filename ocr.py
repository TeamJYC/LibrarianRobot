import cv2
import pytesseract
from collections import Counter

queue = []

def tesseract(img):
    text = pytesseract.image_to_string(img, lang="kor+eng") # 테서렉트로 글자 추출
    return text

def get_classnumber(text):
    text = text.replace(" ", "") # 띄어쓰기 제거
    
    call_sign = [0,0,0] # 청구기호 3자리 숫자 넣을 리스트
    count = 0 # 텍스트에서 숫자가 연속으로 나올 때 카운트
    global queue
    
    for idx, val in enumerate(text): # 리스트 요소 하나씩 접근
        
        if (val == "0" or val == "1" or val == "2" or val == "3" or val == "4" 
         or val == "5" or val == "6" or val == "7" or val == "8" or val == "9"):
            count += 1
        else:
            count = 0
            
        if count == 3:
            call_sign[2] = text[idx]
            call_sign[1] = text[idx-1]
            call_sign[0] = text[idx-2]
            queue.append(call_sign[0])  
            
            print(''.join(call_sign))
            
            if len(queue) == 10:
                queue.pop(0)
                
            counter = Counter(queue)
            
            if int(counter.most_common(1)[0][1]) >= 3:
                n = int(counter.most_common(1)[0][0])
                return n
            break
    

if __name__ == "__main__":
    for i in range(0,9):
        text = "aaa 567,.86-x492"
        destination = get_classnumber(text)
        if (destination != None):
            print(destination)
            break
        
        