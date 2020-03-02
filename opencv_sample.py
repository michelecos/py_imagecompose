import numpy as np
import cv2

# Load a color image in grayscale
img = cv2.imread('images/bimbo_soldato/input.jpg', cv2.COLOR_BGR2BGRA)
cv2.imshow("test", img)
cv2.waitKey(0)

