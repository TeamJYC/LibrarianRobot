import cv2
import camera
import imgprocessing

while True:
    img_source = camera.get_frame_every_nseconds()
    
    img_gray = cv2.cvtColor(img_source, cv2.COLOR_BGR2GRAY)
    
    img_watershed = imgprocessing.watershed(img_gray)
    
    img_warp = imgprocessing.perspectivetransformation(img_watershed)
    
    img_clache = imgprocessing.clache(img_warp)
    
    
    
    #전처리 & OCR
    
camera.camera_release()