import time

import cv2
import mss
import numpy
import pyautogui
from PIL import Image

with mss.mss() as sct:
    # Part of the screen to capture
    monitor = {"top": 40, "left": 0, "width": 800, "height": 600}

    while "Screen capturing":
        last_time = time.time()

        # Get raw pixels from the screen, save it to a Numpy array
        # img = numpy.array(sct.grab(monitor))

        sct_img = sct.grab(monitor)
        img_array = numpy.array(sct_img)
        img = Image.frombytes("RGB", sct_img.size, sct_img.bgra, "raw", "BGRX")

        # Display the picture
        cv2.imshow("OpenCV/Numpy normal", img_array)

        # Display the picture in grayscale
        # cv2.imshow('OpenCV/Numpy grayscale',
        #            cv2.cvtColor(img, cv2.COLOR_BGRA2GRAY))

        print("fps: {}".format(1 / (time.time() - last_time)))

        # Press "q" to quit
        if cv2.waitKey(25) & 0xFF == ord("q"):
            cv2.destroyAllWindows()
            break
