"""
S.E. Schimmel - S.E.Schimmel@student.tudelft.nl
Bachelor Final Project - WB3BEP-16 - TU Delft
Depth from Defocus using a single blurred image
"""

import cv2
import numpy as np

# Camera intrinsic values -> CANON EOS 500D
F=18 #mm (= Focal Length of Camera Lens)
focus=250 #mm (= focal distance, the distance at which a subject would be in perfect focus)
f=3.5 # (= f-number at which the lens aperture is set)
sensor_width=22.3 #mm (= width of the camera sensor)
image_width=4752 # (= width of total image captured in pixels)

# Convert image to grayscale image (also changes image shape from height, width, channel to height, width only)
def convert_to_grayscale(blurred_image):
    gray_blurred = cv2.cvtColor(blurred_image, cv2.COLOR_BGR2GRAY)
    return(gray_blurred)

# Load the converted grayscale image and determine the diameter of the blur circle in terms of pixels
def determine_blur_circle_diameter(gray_blurred):
    height, width=gray_blurred.shape

    sum_of_upper_limit_averages=0 # initialize a rolling sum variable for the grayscale pixel value of the upper limit at 0
    sum_of_lower_limit_averages=0 # initialize a rolling sum variable for the grayscale pixel value of the lower limit at 0

    # Determine the average grayscale value of the first 25 columns and last 25 columns respectively
    for n in range(25):
        upper_limit_average=np.average(gray_blurred[:,n]) # calculate the average grayscale value of columns 1-25
        sum_of_upper_limit_averages+=upper_limit_average # add to the rolling sum
        upper_limit=sum_of_upper_limit_averages/(n+1) # divide by amount of columns for total average value
        upper_limit = round(upper_limit, 1) # round total average value by 1 decimal

        lower_limit_average=np.average(gray_blurred[:, -1-n]) # calculate the average grayscale value of last 25 columns
        sum_of_lower_limit_averages += lower_limit_average # add to the rolling sum
        lower_limit = sum_of_lower_limit_averages / (n + 1) # divide by amount of columns for total average value
        lower_limit = round(lower_limit,1) # round total average value by 1 decimal

    threshold=0.125*(upper_limit-lower_limit) # Calculate a threshold variable by taking 12.5% of the difference between the calculated upper and lower limit
    threshold_limit_upper=upper_limit-threshold # Determine an upper threshold value
    threshold_limit_lower=lower_limit+threshold # Determine the lower threshold value

    blur_circle=[] # create an empty list to store the left and right index of the blur circle into
    left_limit=0 # initialize a counting variable at 0
    right_limit=0 # initialize a counting variable at 0

    previous_average_value=[] # initialize a list to store the value of the average grayscale pixel value per column, this is used later for linear interpolation the determine pixel diameter of blur circle more accurately

    for i in range(len(gray_blurred[0])):
        pixel_value = 0 # initialize a rolling sum variable for the grayscale pixel value
        for j in range(len(gray_blurred[:,0])):
            pixel_value+=int(gray_blurred[j][i]) # add grayscale pixel value within each column to rolling sum variable
            average_value=pixel_value/(j+1) # determine average grayscale value per column

            if j==(len(gray_blurred[:,0])-1): # When the last grayscale pixel value of the column has been reached
                previous_average_value.append(average_value) # add average grayscale pixel value per column to list

                if average_value < threshold_limit_upper and left_limit==0: # Only execute when the average grayscale pixel value of a column surpasses the upper threshold value AND the index of the upper limit hasn't been appended to the blur circle list
                    d_tot_upper=(previous_average_value[i-1]-average_value) # Calculate total difference between average grayscale pixel value of current column (that surpassed the threshold) and the average grayscale pixel value of the previous column (that didn't surpass the threshold)
                    d_l_upper=(previous_average_value[i-1]-threshold_limit_upper) # Calculate difference between average grayscale pixel value of the previous column and the corresponding threshold value
                    d_r_upper=(threshold_limit_upper-average_value) # Calculate difference between average grayscale pixel value of current column and the corresponding threshold value
                    left_limit_to_append=((d_r_upper/d_tot_upper)*(i-1))+((d_l_upper/d_tot_upper)*i) # Use linear interpolation between indices to more accurately determine the edge of the (scaled) blur circle
                    blur_circle.append(left_limit_to_append) # Add this value to the blur circle list
                    left_limit+=1 # add 1 to the variable to ensure the if-statement will not execute again (we only require one upper limit)

                elif average_value < threshold_limit_lower and right_limit==0: # Only execute when the average grayscale pixel value of a column surpasses the lower threshold value AND the index of the lower limit hasn't been appended to the blur circle list
                    d_tot_lower=(previous_average_value[i-1]-average_value) # Calculate total difference between average grayscale value of current column (that surpassed the threshold) and the average grayscale of the column before (that didn't surpass the threshold)
                    d_l_lower=(previous_average_value[i-1]-threshold_limit_lower) # Calculate difference between average grayscale pixel value of the previous column and the corresponding threshold value
                    d_r_lower=(threshold_limit_lower-average_value) # Calculate difference between average grayscale pixel value of current column and the corresponding threshold value
                    right_limit_to_append=((d_r_lower/d_tot_lower)*(i-1))+((d_l_lower/d_tot_lower)*i) # Use linear interpolation between indices to more accurately determine the edge of the (scaled) blur circle
                    blur_circle.append(right_limit_to_append) # Add this value to the blur circle list
                    right_limit+=1 # add 1 to the variable to ensure the elif-statement will not execute again (we only require one lower limit)

    blur_circle_diameter=np.abs(blur_circle[0]-blur_circle[1]) # Determine blur circle pixel diameter obtained
    blur_circle_diameter_pixels=(2.2825*blur_circle_diameter) # Multiply blur circle pixel diameter by a factor to compensate for threshold value used earlier to obtain actual blur circle pixel diameter
    return blur_circle_diameter_pixels

# Calculate object distance
def Estimate_Depth(blur_circle_diameter_pixels):
    metric_blur_circle_diameter=(blur_circle_diameter_pixels/image_width)*sensor_width # Convert diameter of blur circle from pixels to millimeters
    depth=((-focus*F**2)/(metric_blur_circle_diameter*f*(focus-F)-F**2)) # Determine object distance using relationship between blur circle diameter in millimeters and camera intrinsic values
    return depth