# Open an image whose absolute path is provided and close it if ESC key is pressed or save it in current directory if 's' is pressed
# https://stackoverflow.com/questions/35180764/opencv-python-image-too-big-to-display
import os
import cv2

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
IMAGES_FOLDER_PATH = os.path.join(CURRENT_DIR, "Images")
IMAGE_FILE = os.path.join(IMAGES_FOLDER_PATH, "image1_3840x2160.jpg")

img = cv2.imread(IMAGE_FILE, 0)
img = cv2.resize(img, (960, 540))   # Resize image to fit screen
cv2.imshow('Custom Name', img)
k = cv2.waitKey(0)
if k == 27:  # wait for ESC key to exit
    cv2.destroyAllWindows()
elif k == ord('s') or k == ord('S'):  # wait for 's' key to save and exit, ord() gives ASCII value of a letter
    cv2.imwrite('another name.jpg', img)
    cv2.destroyAllWindows()
