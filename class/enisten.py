import cv2
import matplotlib.pyplot as plt
import numpy as np
img = cv2.imread('class\images\enistein.png')
print(img.shape) 
x = np.arange(0,493)
y = np.arange(0,493)
x,y = np.meshgrid(x,y)
axis = plt.axes(projection="3d")
axis.plot_surface(x,y,img[:,:,[0,1]],color='gray')
plt.show()