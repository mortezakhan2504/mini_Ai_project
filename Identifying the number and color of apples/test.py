import cv2
import numpy as np


image = cv2.imread('02.jpg') 


hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

red_lower = np.array([0, 100, 100])
red_upper = np.array([10, 255, 255])

yellow_lower = np.array([20, 100, 100])
yellow_upper = np.array([30, 255, 255])

green_lower = np.array([35, 50, 50])  
green_upper = np.array([85, 255, 255])


red_mask = cv2.inRange(hsv_image, red_lower, red_upper)
yellow_mask = cv2.inRange(hsv_image, yellow_lower, yellow_upper)
green_mask = cv2.inRange(hsv_image, green_lower, green_upper)


red_contours ,rt = cv2.findContours(red_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
yellow_contours ,gt  = cv2.findContours(yellow_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
green_contours , yt = cv2.findContours(green_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)


red_result = cv2.bitwise_and(image, image, mask=red_mask)
yellow_result = cv2.bitwise_and(image, image, mask=yellow_mask)
green_result = cv2.bitwise_and(image, image, mask=green_mask)


red_apples = len(rt)
yellow_apples = len(yt)
green_apples = len(gt)

print(f"Red Apples: {red_apples}")
print(f"Yellow Apples: {yellow_apples}")
print(f"Green Apples: {green_apples}")


cv2.imshow('HSV', hsv_image)
cv2.imshow('Red Mask', red_result)
cv2.imshow('Yellow Mask', yellow_result)
cv2.imshow('Green Mask', green_result)
cv2.waitKey(0)
cv2.destroyAllWindows()
