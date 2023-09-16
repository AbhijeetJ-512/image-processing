import matplotlib.pyplot as plt
import cv2
import numpy as np
image = cv2.imread('class\images\modi.jpg',0)
x = np.arange(0,1431)
y = np.arange(0,1202)
x , y = np.meshgrid(x,y)
z = image

fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.plot_surface(x, y, z,cmap='gray')

# Show the plot
plt.show()