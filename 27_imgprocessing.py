#-*- coding: utf-8 -*-
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


def perspective_transformation(img, img_source):
    
    contours, ret = cv2.findContours(img, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE) # 컨투어링(테두리)

    cnt = contours[0]
    
    epsilon = 0.1*cv2.arcLength(cnt, True)
    approx = cv2.approxPolyDP(cnt, epsilon, True) # 외곽선 근사화
    
    if len(approx) != 4: # 꼭짓점이 4개가 나오지 않을 때 임의로 좌표값 설정
        pts1 = np.float32([[0,0], [0,0], [0,0], [0,0]])
    else : # 꼭짓점이 정상적으로 4개 나오면 꼭짓점 설정 맞추고 투시 변환
        mean = approx.mean(axis = 2).squeeze()
        idx_sort = mean.argsort()
        sub = approx[idx_sort[1]] - approx[idx_sort[2]]
        
        if sub[0][0] > 0:
                a = idx_sort[1]
                b = idx_sort[2]
        else:
                a = idx_sort[2]
                b = idx_sort[1]    
        pts1 = np.float32([approx[idx_sort[0]], approx[a], approx[b], approx[idx_sort[3]]])   
    
    pts2 = np.float32([[0,0], [500,0], [0,500], [500,500]])
    
    M = cv2.getPerspectiveTransform(pts1, pts2)
    
    img_warp = cv2.warpPerspective(img_source, M, (500,500))
    
    return img_warp


def clache(img):
    img_yuv = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)

    img_clahe = img_yuv.copy()
    clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8,8)) #CLAHE 생성
    img_clahe[:,:,0] = clahe.apply(img_clahe[:,:,0])           #CLAHE 적용
    img_clahe = cv2.cvtColor(img_clahe, cv2.COLOR_YUV2BGR)
    
    return img_clahe

if __name__ == "__main__":
    while True:
        img = cv2.imread('test.jpg', cv2.IMREAD_COLOR)
        
        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        
        img_watershed = watershed(img_gray, img)
        
        img_warp = perspective_transformation(img_watershed, img)
        
        img_clache = clache(img_warp)
        
        img_gray2 = cv2.cvtColor(img_clache, cv2.COLOR_BGR2GRAY)
        ret, img_thresh = cv2.threshold(img_gray2, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)

        cv2.imshow('img',img_thresh)
        
        key = cv2.waitKey(33)
        if key == 27: # Esc
            break
    cv2.destroyAllWindows()