import matplotlib.pyplot as plt
import cv2
x = [1,2,3,4,5,6,7]
y = [2,6,2,7,9,3,1]
z = [4,7,9,5,2,6,7]
axis = plt.axes(projection="3d")
axis.scatter(x,y,z,color='red')
plt.show()
img = cv2.imread('images/tree.png')
axis = plt.axes(projection="3d")
axis.plot(img)
plt.show()