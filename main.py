import cv2
import camera
import imgprocessing
import ocr

name = ["총류", "철학", "종교", "사회과학", "순수과학", "기술과학", "예슐", "언어", "문학", "역사"]

while True:
    img_source = camera.get_frame_every_nseconds()
    img_gray = cv2.cvtColor(img_source, cv2.COLOR_BGR2GRAY)
    
    img_watershed = imgprocessing.watershed(img_gray, img_source)
    
    img_warp = imgprocessing.perspective_transformation(img_watershed, img_source)
    
    img_clache = imgprocessing.clache(img_warp)
    
    img_gray2 = cv2.cvtColor(img_clache, cv2.COLOR_BGR2GRAY)
    ret, img_thresh = cv2.threshold(img_gray2, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
   
    cv2.imshow('img',img_thresh)
    cv2.imshow('img_source',img_source)
    
    text = ocr.tesseract(img_thresh)
    destination = ocr.get_classnumber(text)
    
    if (destination != None):
        print(name[destination] + "분류입니다.")
        break
    
    
    key = cv2.waitKey(33)
    if key == 27: # Esc
        break

camera.camera_release()
cv2.destroyAllWindows()