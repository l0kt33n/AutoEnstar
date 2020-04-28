# TODO: Find Window
# TODO: Program controller
# TODO: Menu
# TODO: Music select
# TODO: Team select
# TODO: For the first time of playing, get tapping positions, and set flag
# TODO: Play Controller

import mss
import numpy
from PIL import Image
import cv2
import pyautogui


def record_screen(monitor):
    with mss.mss() as sct:
        sct_img = sct.grab(monitor)

        # For Debugging
        img_array = numpy.array(sct_img)
        cv2.imshow("Screen Recording", img_array)  # Display the image

        return Image.frombytes("RGB", sct_img.size, sct_img.bgra, "raw", "BGRX")


def find_window(screen):
    try:
        top_left = pyautogui.locateOnScreen('./img/top_left.png', confidence=0.8)
        bottom_right = pyautogui.locateOnScreen('./img/bottom_right.png', confidence=0.8)
    except pyautogui.ImageNotFoundException:
        print("Window Not Found. Terminating program.")
        return False

    if top_left == None or bottom_right == None:
        print("Window Not Found. Terminating program.")
        return False
    else:
        left = top_left[0]
        top = top_left[1]
        right = bottom_right[0]
        bottom = bottom_right[1]

    window = {"top": top, "left": left, "width": right, "height": bottom}
    print(window)
    return window


def controller(screen):
    return


def main():
    with mss.mss() as sct:
        # Default size for screen
        monitor = {"top": 40, "left": 0, "width": 1920, "height": 1080}
        screen = record_screen(monitor)
        monitor = find_window(screen)

        while monitor:
            # Get raw pixels from the screen, and construct it using Image
            screen = record_screen(monitor)

            # controller(screen)

            if cv2.waitKey(25) & 0xFF == ord("q"):
                cv2.destroyAllWindows()
                break

        return 0


if __name__ == "__main__":
    main()
