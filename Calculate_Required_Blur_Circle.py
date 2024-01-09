import numpy as np

focus=250#mm (=focal distance, the distance at which a subject would be in perfect focus)
distance=1500#mm (=actual subject distance, the point whose CoC we are calculating)
F=18#mm (=focal length of lens)
N=3.5 #(=f-number at which the lens aperture is set)
sensor_width=22.3 #mm (= width of the camera sensor)
image_width=4752 # (= width of total image captured in pixels)

#We are going to calculate c, the physical CoC diameter in the image plane)
c1=(np.abs(distance-focus)/distance)*((F**2)/(N*(focus-F)))
print("Circle of Confusion:", c1, "mm")

pixels=(c1/22.3)*4752
print("Pixel Width:", pixels)

blur_circle_diameter=17.5 #pixels
metric_blur_circle_diameter=((blur_circle_diameter*(3.644))/image_width)*sensor_width
print(metric_blur_circle_diameter)
depth=((-focus*F**2)/(metric_blur_circle_diameter*N*(focus-F)-F**2))

print("Depth:", depth)