import cv2
import numpy as np

base_img = cv2.imread("class/images/base_img.jpg")
target_img = cv2.imread("class/images/subject.jpg")

points = [[108, 186], [456, 70], [480, 249], [91, 359]]

h_base, w_base = base_img.shape[:2]
h_subject, w_subject = target_img.shape[:2]  # Fix the typo here

# Define the four corners of the target image
pts1 = np.float32([[0, 0], [w_subject, 0], [w_subject, h_subject], [0, h_subject]])  # type: ignore

pts2 = np.float32(points)  # type: ignore

transformation_matrix = cv2.getPerspectiveTransform(pts1, pts2)  # type: ignore
warped_img = cv2.warpPerspective(target_img, transformation_matrix, (w_base, h_base))
mask = np.ones(base_img.shape, dtype=np.uint8) * 255
rel_corner = np.int32(points)  # type: ignore
mask = cv2.fillConvexPoly(mask, rel_corner, (0, 0, 0))  # type: ignore
masked_img = cv2.bitwise_and(base_img, mask)
output = cv2.bitwise_or(masked_img, warped_img)

# cv2.imshow("subject", target_img)
# cv2.imshow("Base", base_img)
# cv2.imshow("warped", warped_img)
# cv2.imshow("masked", masked_img)
# cv2.imshow("mask", mask)
cv2.imshow("output", output)
cv2.waitKey(0)
cv2.destroyAllWindows()
