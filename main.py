import cv2
from sensor import camera

print("Starting Librarian ...")

while True:
    frame = camera.get_realtime_frame()
    cv2.imshow('b',frame)
    key = cv2.waitKey(10)
    if key == 27:
        break
    
cv2.destroyAllWindows()
camera.camera_release()