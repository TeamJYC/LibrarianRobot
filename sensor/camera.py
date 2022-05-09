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
    cv2.imshow('img_source', img_source)
    timer = Timer(DELAY_N_SECONDS, get_frame_every_nseconds(frame))
    timer.start()
    return img_source

def camera_release():
    capture.release()

if __name__ == "__main__":
    frame = get_frame()
    img_source = get_frame_every_nseconds(frame)
    cv2.destroyAllWindows()