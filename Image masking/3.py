import cv2
import numpy as np

# Load images from database or file paths
image_paths = ['image1.jpg', 'image2.jpg', 'image3.jpg', 'image4.jpg', 'image5.jpg']
images = [cv2.imread(path) for path in image_paths]

# Define different types of masks
mask_triangle = np.array([[1, 0, 0],
                           [1, 1, 0],
                           [1, 1, 1]], dtype=np.uint8)

mask_diagonal = np.array([[1, 0, 0],
                           [0, 1, 0],
                           [0, 0, 1]], dtype=np.uint8)

mask_vertical = np.array([[1, 0, 1],
                           [1, 0, 1],
                           [1, 0, 1]], dtype=np.uint8)

# Apply masks to images and display results
for idx, image in enumerate(images, start=1):
    # Apply triangular mask
    filtered_triangle = cv2.filter2D(image, -1, mask_triangle)
    cv2.imshow(f'Image {idx} - Triangular Mask', filtered_triangle)

    # Apply diagonal mask
    filtered_diagonal = cv2.filter2D(image, -1, mask_diagonal)
    cv2.imshow(f'Image {idx} - Diagonal Mask', filtered_diagonal)

    # Apply vertical mask
    filtered_vertical = cv2.filter2D(image, -1, mask_vertical)
    cv2.imshow(f'Image {idx} - Vertical Mask', filtered_vertical)

    cv2.waitKey(0)

cv2.destroyAllWindows()
