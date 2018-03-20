import os
import cv2

# #####################################
# os.walk(PATH) To traverse a folder recursively.
# #####################################
# for BASE_DIR, SUB_DIRS, FILES in os.walk(IMAGES_FOLDER_PATH):
#     print(BASE_DIR, SUB_DIRS, FILES)

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
IMAGES_FOLDER_PATH = os.path.join(CURRENT_DIR, "Images")
IMAGE_FILE = os.path.join(IMAGES_FOLDER_PATH, "image1_3840x2160.jpg")

# ######################################
#  Read an image
# ######################################
# Use the function cv2.imread() to read an image. The image should be in the working directory or a full path of image should be given.
# Even if the image path is wrong, it won’t throw any error, but the object returned will give you None
# Second argument is a flag which specifies the way image should be read.
# • cv2.IMREAD_COLOR : Loads a color image. Any transparency of image will be neglected. It is the default flag.
# • cv2.IMREAD_GRAYSCALE : Loads image in grayscale mode
# • cv2.IMREAD_UNCHANGED : Loads image as such including alpha channel
# Note: Instead of these three flags, you can simply pass integers 1, 0 or -1 respectively.

img = cv2.imread(IMAGE_FILE)

print("Type of object returned :", type(img))  # <class 'numpy.ndarray'>
print("All attributes :", dir(img))

# ######################################
# Display an image
# ######################################
# Use the function cv2.imshow() to display an image in a window. The window automatically fits to the image size.
# First argument is a window name which is a string. second argument is our image. You can create as many windows
# as you wish, but with different window names.
#
# cv2.waitKey() is a keyboard binding function. Its argument is the time in milliseconds. The function waits for
# specified milliseconds for any keyboard event. If you press any key in that time, the program continues. If 0 is passed,
# it waits indefinitely for a key stroke. It can also be set to detect specific key strokes like, if key a is pressed etc which
# we will discuss below.
#
# cv2.destroyAllWindows() simply destroys all the windows we created. If you want to destroy any specific window,
# use the function cv2.destroyWindow() where you pass the exact window name as the argument.

img = cv2.resize(img, (960, 540))   # Resize image to fit screen
cv2.imshow('Any name here', img)
cv2.waitKey(0)
cv2.destroyAllWindows()


# #######################################
# Write an image
# #######################################
# Use the function cv2.imwrite() to save an image.
# First argument is the file name, second argument is the image you want to save.
# This will save the image in PNG format in the working directory.

cv2.imwrite('any_name_here.png', img)

