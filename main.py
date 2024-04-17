import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


def parseval_energy_theorem(img_path):
    # Reading the image
    img = cv.imread(img_path, cv.IMREAD_GRAYSCALE)
    if img is None:
        print("Image not loaded")
        return
    
    # Fourier Transform
    img_FD = np.fft.fft2(img, norm="ortho")

    # Magnitude of the image and its Fourier Transform
    mag_img = np.linalg.norm(img, 2, keepdims=False)
    mag_img_FD = np.linalg.norm(img_FD, 2, keepdims=False)

    # Displaying the images
    img_FD_dis = np.log(np.absolute(img_FD))

    # Plotting the images
    plt.subplot(1, 2, 1), plt.imshow(img, cmap="gray")
    plt.xlabel(f"Energy : {round(mag_img,3)}")
    plt.title(f"Original Image ({img_path.split("/")[-1]})"), plt.xticks([]), plt.yticks([])

    plt.subplot(1, 2, 2), plt.imshow(img_FD_dis, cmap="gray")
    plt.xlabel(f"Energy : {round(mag_img_FD,3)}")
    plt.title(f"Fourier Transform ({img_path.split("/")[-1]})"), plt.xticks([]), plt.yticks([])

    plt.suptitle("Parseval's Energy Theorem")
    plt.show()


if __name__ == "__main__":
    parseval_energy_theorem("./assets/lena.png")