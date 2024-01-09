"""
S.E. Schimmel - S.E.Schimmel@student.tudelft.nl
Bachelor Final Project - WB3BEP-16 - TU Delft 2023-2024
Depth from Defocus using a single blurred image
"""

import functions
import cv2
import time

# Start timer
start_time = time.time()

# Load the image patch
blurred_image = cv2.imread(r'25CM-A.png')

# Convert images to grayscale
gray_blurred = functions.convert_to_grayscale(blurred_image)

# Determine the diameter of the blur circle in terms of pixels
blur_circle_diameter_pixels = functions.determine_blur_circle_diameter(gray_blurred)

# Estimate the object distance based on the blur circle diameter (in pixels)
depth=functions.Estimate_Depth(blur_circle_diameter_pixels)

# Print the estimated Depth
print("Estimated Depth: ", depth,"mm")

# Print blur circle diameter
print("Blur Circle Diameter in Pixels:", blur_circle_diameter_pixels, "pixels")

# Print script runtime
print("--- %s seconds ---" % (time.time() - start_time))

# Display the Blurred Image
cv2.imshow('Blurred Image', blurred_image)
cv2.waitKey(0)
cv2.destroyAllWindows()