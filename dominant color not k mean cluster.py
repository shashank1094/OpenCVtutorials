# import the necessary packages
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import argparse
import utils
import cv2
import os
from collections import Counter
from collections import Counter

# # construct the argument parser and parse the arguments
# ap = argparse.ArgumentParser()
# ap.add_argument("-i", "--image", required = True, help = "Path to the image")
# ap.add_argument("-c", "--clusters", required = True, type = int,
# 	help = "# of clusters")
# args = vars(ap.parse_args())


# load the image and convert it from BGR to RGB so that
# we can display it with matplotlib
# image = cv2.imread(args["image"])
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
IMAGES_FOLDER_PATH = os.path.join(CURRENT_DIR, "Images")
IMAGE_FILE = os.path.join(IMAGES_FOLDER_PATH, "image2.jpg")

image = cv2.imread(IMAGE_FILE)
# image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV_FULL)

all_colors = Counter([tuple(colors) for i in image for colors in i])


def calculate_percentage(value, out_of):
    print((value / out_of) * 100,"%")


total_colors = (image.shape[0] * image.shape[1])
#print(total_colors)

counter = 1
for w in sorted(all_colors, key=all_colors.get, reverse=True):
    if counter > 7:
        break
    print(w, end=" ====>>>> ")
    calculate_percentage(all_colors[w], total_colors)
    counter = counter + 1
