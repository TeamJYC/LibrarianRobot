#-*- coding: utf-8 -*-
#pip install pytesseract==0.3.5

import cv2
import pytesseract
from collections import Counter

def tesseract(img):
    text = pytesseract.image_to_string(img, lang="kor+eng") # 테서렉트로 글자 추출
    return text

if __name__ == "__main__":
    img = cv2.imread("picture.png")
    text = tesseract(img)
    print(text)