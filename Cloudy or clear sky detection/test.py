import cv2
import numpy as np


image = cv2.imread('01.jpg')


hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)


sky_lower = np.array([100, 50, 50]) 
sky_upper = np.array([130, 255, 255])


sky_mask = cv2.inRange(hsv_image, sky_lower, sky_upper)


sky_area = np.count_nonzero(sky_mask)


cloudy_threshold = 50000
is_cloudy = sky_area > cloudy_threshold


if is_cloudy:
    print("The sky is clear.")
else:
    print("The sky is cloudy.")


cv2.imshow('Sky Mask', sky_mask)
cv2.imshow('Original Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
