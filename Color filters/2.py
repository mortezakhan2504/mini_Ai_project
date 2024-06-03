import cv2
import numpy as np
from skimage import color

# Load the image
image_path = 'path_to_your_image.jpg'
image = cv2.imread(image_path)

# Convert the image to different color spaces
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # RGB
image_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)  # HSV
image_lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)  # LAB

# Display the images
cv2.imshow('RGB Image', image_rgb)
cv2.imshow('HSV Image', image_hsv)
cv2.imshow('LAB Image', image_lab)
cv2.waitKey(0)
cv2.destroyAllWindows()