User Manual - Depth From Defocus

This user manual provides instructions on how to set up a proper camera setup and
use the python script to determine the distance to an object. It should be noted that
the python script is only suitable to determine the distance to an object that has a
ample* flat surface placed perpendicular to the optical axis of the camera, with a
sharp horizontal transition in terms of grayscale pixel value at the center of this flat
surface.

(*depends on intrinsic camera values such as focal length and focus distance)

First of all a suitable camera needs to be selected, most importantly the camera
requires the ability to manually set a certain focus distance. The camera needs to be
manually set to a certain (metric) focus distance, where the selected focus distance
is the shortest distance for which depth can be estimated. All camera systems have
a certain minimum focus distance, which should be taken into account.

On top of this the following intrinsic camera values used to capture an image need to
be known: the focal length of the lens, f-number at which the lens aperture is set,
width of the camera image sensor in millimeters, width of full-sized image taken by
the camera in terms of pixels. These parameters need to be entered into the
functions.py script since they are required for the depth estimation calculation.

After an image has been captured using known intrinsic camera values, an image
patch containing the sharp horizontal transition in terms of grayscale pixel value of
the object needs to be cropped out of the image.

The python script takes this cropped image patch as an input. Running the script, the
image is converted to grayscale and the blur circle diameter is determined in terms
of pixel size. Next this value is converted to millimeters and consequently used to
estimate the depth to the object.

Please refer to the comments in the python scripts for detailed step-by-step
explanation on how the size of the blur circle is determined and used to estimate the
depth to an object.