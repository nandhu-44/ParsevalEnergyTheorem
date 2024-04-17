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

    # Phase of the Fourier Transform
    phase_img_FD = np.angle(img_FD)

    # Displaying the images
    img_FD_dis = np.log(np.absolute(img_FD))

    # Plot 1: Original Image and its Fourier Transform
    plt.figure(figsize=(12, 6))
    plt.subplot(1, 2, 1), plt.imshow(img, cmap="gray")
    plt.xlabel(f"Energy: {round(mag_img, 3)}")
    plt.title(f"Original Image ({img_path.split('/')[-1]})")
    plt.xticks([]), plt.yticks([])

    plt.subplot(1, 2, 2), plt.imshow(img_FD_dis, cmap="gray")
    plt.xlabel(f"Energy: {round(mag_img_FD, 3)}")
    plt.title(f"Fourier Transform ({img_path.split('/')[-1]})")
    plt.xticks([]), plt.yticks([])
    plt.suptitle("Parseval's Energy Theorem", fontsize=16)
    plt.show()

    # Plot 2: Magnitude Spectrum
    plt.figure(figsize=(8, 6))
    plt.imshow(img_FD_dis, cmap="gray")
    plt.title(f"Magnitude Spectrum of Fourier Transform ({img_path.split('/')[-1]})")
    plt.xticks([]), plt.yticks([])
    plt.show()

    # Plot 3: Phase Spectrum
    plt.figure(figsize=(8, 6))
    plt.imshow(phase_img_FD, cmap="gray")
    plt.title(f"Phase Spectrum of Fourier Transform ({img_path.split('/')[-1]})")
    plt.xticks([]), plt.yticks([])
    plt.show()


if __name__ == "__main__":
    parseval_energy_theorem("./assets/lena.png")
