<<<<<<< Updated upstream
from sensor import camera
=======
import cv2
import camera
>>>>>>> Stashed changes

print("Starting Librarian ...")

frame = camera.get_frame()

img_source = camera.get_frame_every_nseconds(frame)