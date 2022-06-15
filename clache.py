# -*- coding: utf-8 -*-
import cv2
import numpy as np
def clache(img):
    img_yuv = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)
    img_clahe = img_yuv.copy()
    clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8,8)) #CLAHE 생성
    img_clahe[:,:,0] = clahe.apply(img_clahe[:,:,0])           #CLAHE 적용
    img_clahe = cv2.cvtColor(img_clahe, cv2.COLOR_YUV2BGR)
    
    return img_clahe
