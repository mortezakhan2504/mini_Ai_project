import cv2
import numpy as np

# Load the image
image = cv2.imread('path_to_your_image.jpg', 0)  # Load image in grayscale mode

# Define the kernel for erosion and dilation
kernel = np.ones((5, 5), np.uint8)  # 5x5 square kernel, you can adjust its size

# Apply erosion and dilation
erosion_image = cv2.erode(image, kernel, iterations=1)
dilation_image = cv2.dilate(image, kernel, iterations=1)

# Display the results
cv2.imshow('Original Image', image)
cv2.imshow('Erosion Image', erosion_image)
cv2.imshow('Dilation Image', dilation_image)
cv2.waitKey(0)
cv2.destroyAllWindows()