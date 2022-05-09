from sensor import camera

print("Starting Librarian ...")

frame = camera.get_frame()

img_source = camera.get_frame_every_nseconds(frame)