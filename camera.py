import cv2
import time

DELAY_N_SECONDS = 3

capture = cv2.VideoCapture(0)

def get_frame_every_nseconds():
    ret, frame = capture.read()
    time.sleep(DELAY_N_SECONDS)
    return frame

def camera_release():
    capture.release()

if __name__ == "__main__":
    while True:
        frame = get_frame_every_nseconds()
        cv2.imshow('img', frame)
        key = cv2.waitKey(33)
        if key == 27: # Esc
            break
    cv2.destroyAllWindows()
    camera_release()