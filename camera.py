import cv2
from threading import Timer

DELAY_N_SECONDS = 3

capture = cv2.VideoCapture(0)

def get_frame():
    ret, frame = capture.read()
    print("Camera on ...")
    return frame

def get_frame_every_nseconds(frame):
    img_source = frame
    timer = Timer(DELAY_N_SECONDS, get_frame_every_nseconds(frame))
    cv2.imshow('a', img_source)
    timer.start()
    return img_source
    
def camera_release():
    capture.release()

if __name__ == "__main__":
    flag = 0
    frame = get_frame()
    if flag == 0:
        img_source = get_frame_every_nseconds(frame)
        flag = 1
    cv2.destroyAllWindows()
    