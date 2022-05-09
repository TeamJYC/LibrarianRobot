import cv2
import time


capture = cv2.VideoCapture(0)

def get_realtime_frame():
    ret, frame = capture.read()
    return frame


def get_frame_every_nseconds():
    while True:
        ret, frame = capture.read()
        cv2.imshow('b',frame)
        time.sleep(2)
        key = cv2.waitKey(10)
        if key == 27: # Esc
            break
        return frame
    
def camera_release():
    capture.release()

if __name__ == "__main__":
    get_frame_every_nseconds()
    cv2.destroyAllWindows()
    camera_release()
    