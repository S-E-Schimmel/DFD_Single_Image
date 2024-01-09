import matplotlib.pyplot as plt
import numpy as np

focus=250#mm (=focal distance, the distance at which a subject would be in perfect focus)
distance=1000#mm (=actual subject distance, the point whose CoC we are calculating)
F=18#mm (=focal length of lens)
N=3.5 #(=f-number at which the lens aperture is set)


def f(x):
    return (np.abs(x-focus)/x)*((F**2)/(N*(focus-F)))
x=np.linspace(250,12500, 12250)

plt.plot(x,f(x), color='red')
plt.xlabel("Distance to Object [mm]")
plt.ylabel("Diameter of Blur Circle in Image Plane [mm]")
plt.savefig('Distance_to_Object_vs_blur_circle_size.png')
plt.show()
