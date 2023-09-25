import cv2
import numpy as np
import matplotlib.pyplot as plt


class Assignment:
    def __init__(self, path):
        self.image = cv2.imread(path)
        if self.image is None:
            raise Exception("Failed to load image.")

    def rgb2gray(self):
        return cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)

    def histogram(self):
        colours = ["b", "g", "r"]
        plt.figure(figsize=(12, 5))
        for i, col in enumerate(colours):
            hist = cv2.calcHist(
                images=[self.image],
                channels=[i],
                mask=None,
                histSize=[256],
                ranges=[0, 256],
            )
            plt.plot(hist, color=col)
            plt.xlim([0, 256])
        plt.show()

    def compute_and_plot_histogram(self):
        gray_image = self.rgb2gray()
        plt.figure(figsize=(12, 5))
        plt.hist(gray_image.ravel(), bins=256, range=(0, 255))
        plt.xlabel("Pixel Value")
        plt.ylabel("Frequency")
        plt.title("Histogram")
        plt.show()

    def gaussian_filter(self, kernel_size=(7, 7), sigma=1.0):
        blurred_image = cv2.GaussianBlur(self.image, kernel_size, sigma)
        return blurred_image

    def histogram_equalization(self):
        gray_image = self.rgb2gray()
        equalized_image = cv2.equalizeHist(gray_image)
        return equalized_image


def image_resize(frame, width=1080, height=720):
    dim = (width, height)
    return cv2.resize(frame, dim, interpolation=cv2.INTER_AREA)


def disp(image, window_name: str):
    cv2.imshow(winname=window_name, mat=image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


try:
    image = Assignment("assignment/images/modi.jpg")
    disp(image.image, "original image")
    image.histogram()

    gray_image = image.rgb2gray()
    disp(gray_image, "gray image")

    blurred_image = image.gaussian_filter()
    disp(blurred_image, "Blurred Image")

    equalized = image.histogram_equalization()
    stacked_images = np.hstack((gray_image, equalized))
    stacked_images = image_resize(stacked_images)
    disp(stacked_images, "Original gray vs. Equalized")

except Exception as e:
    print(f"Error: {e}")
