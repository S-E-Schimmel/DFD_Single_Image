# Bachelor End Project -- Direct Depth from Defocus

## Setup
Before running the script please specify the intrinsic camera values used to capture the images in 'functions':
- Focal length of lens
- Focus distance
- Aperture setting (f-number)
- Width of camera sensor 
- Pixel width of full image

## Calibration
1. Take a blurred photo of an object that has high contrast and a sharp transition in terms of grayscale pixel value (with known intrinsic camera parameters and known object distance)
2. Run `Depth_Estimation` to obtain measured blur circle diameter (in pixels)
2. Run `Calculate_Required_Blur_Circle` to calculate theoretical blur circle and determine calibration factor
3. Enter value for calibration factor in `functions`

## Steps
1. Specify the path to the cropped image patch
2. Run `Depth_Estimation` to obtain distance value

## Note
- Script currently doesn't take camera feed and crops image patches automatically, thus isn't working in real-time.

