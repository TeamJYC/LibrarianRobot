import cv2
import numpy as np

def watershed(img_gray, img_source):
    
    img_shape = np.zeros_like(img_gray)
    
    ret, img_thresh = cv2.threshold(img_gray, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU) # 이진화

    kernel = np.ones((3,3),np.uint8)
    
    img_opening = cv2.morphologyEx(img_thresh,cv2.MORPH_OPEN,kernel,iterations=2) # 잡음 제거

    sure_bg = cv2.dilate(img_opening,kernel,iterations=3) # 배경 요소 확보(bg)

    dist_transform = cv2.distanceTransform(img_opening,cv2.DIST_L2,5)
    ret, sure_fg = cv2.threshold(dist_transform,0.5*dist_transform.max(),255,0)
    sure_fg = np.uint8(sure_fg) # skeleton 이미지 & 다시 이진화(fg)

    unknown = cv2.subtract(sure_bg, sure_fg) # bg, fg 제외 영역

    ret, markers = cv2.connectedComponents(sure_fg)
    markers = markers + 1
    markers[unknown == 255] = 0
    
    markers = cv2.watershed(img_source, markers)
    img_shape[markers == -1] = 255
    
    return img_shape