import cv2
import numpy as np

left_img = cv2.imread("class/images/lef2t.jpg", 0)
right_img = cv2.imread("class/images/right.png", 0)

print(left_img.shape)
print(right_img.shape)

stereo = cv2.StereoBM_create(numDisparities=16, blockSize=15)  # type: ignore
# compute disparity
disparity = stereo.compute(left_img, right_img)
print(disparity[0][0])

cv2.imwrite("class/images/disparity.png", disparity)
cv2.imshow("disparity", disparity)
cv2.waitKey(0)
cv2.destroyAllWindows()
