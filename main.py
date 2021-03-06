import cv2
import camera
import imgprocessing as ip
import textprocessing as tp
import ocr

name = ["총류", "철학", "종교", "사회과학", "순수과학", "기술과학", "예슐", "언어", "문학", "역사"]

while True:
    img_source = camera.get_frame_every_nseconds()
    img_gray = cv2.cvtColor(img_source, cv2.COLOR_BGR2GRAY)
    
    img_watershed = ip.watershed(img_gray, img_source)
    
    img_warp = ip.perspective_transformation(img_watershed, img_source)
    
    img_clache = ip.clache(img_warp)
    
    img_gray2 = cv2.cvtColor(img_clache, cv2.COLOR_BGR2GRAY)
    ret, img_thresh = cv2.threshold(img_gray2, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
   
    cv2.imshow('img',img_thresh)
    cv2.imshow('img_source',img_source)
    
    text = ocr.tesseract(img_thresh)
    callnum = tp.get_callnum(text)
    isbn = tp.get_isbn(text)
    
    kdc = None
    
    if callnum and not isbn :
        kdc = tp.callnum_to_kdc(callnum)
    elif isbn:
        kdc = tp.isbn_to_kdc(isbn)
        
    if (kdc != None):
        print(name[kdc] + "분류입니다.")
        break
    
    key = cv2.waitKey(33)
    if key == 27: # Esc
        break

camera.camera_release()
cv2.destroyAllWindows()