import numpy
import matplotlib
import cv2
import sys
import pyzbar
import imutils
import skimage
import sklearn
import mahotas

print("Hello World")
print("Numpy version", numpy.__version__)
print("Matplotlib version", matplotlib.__version__)
print("OpenCV version", cv2.__version__)
print("PyzBar version", pyzbar.__version__)
print("imutils version", imutils.__version__)
print("skimage version", skimage.__version__)
print("sklearn version", sklearn.__version__)
print('mahotas version', mahotas.__version__)
print("Python Version", sys.version)

import tensorflow as tf
hello = tf.constant('Hello, TensorFlow!')
sess = tf.Session()
print(sess.run(hello))


# Hello World
# Numpy version 1.15.2
# Matplotlib version 3.0.0
# OpenCV version 3.4.3
# PyzBar version 0.1.7
# imutils version 0.5.1
# skimage version 0.14.1
# sklearn version 0.20.0
# mahotas version 1.4.4
# Python Version 3.6.5 (default, Apr  1 2018, 05:46:30)
# [GCC 7.3.0]
# b'Hello, TensorFlow!'
