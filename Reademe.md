# Image Energy Calculation

This project calculates the energy of an image using Parseval's Energy Theorem. It uses the Fourier Transform to calculate the energy in the frequency domain and compares it with the energy in the spatial domain.

## Requirements

- Python
- OpenCV
- NumPy
- Matplotlib

## Usage

To use this project, you need to call the `parseval_energy_theorem` function from `main.py` with the path to the image as an argument. 

```python
parseval_energy_theorem("./assets/your_image.png")
```

This function reads the image, calculates the Fourier Transform, and displays the original image and its Fourier Transform side by side. The energy of the image in both the spatial and frequency domains is displayed below the respective images.

## Example

An example usage is provided in the `main.py` file:

```python
if __name__ == "__main__":
    parseval_energy_theorem("./assets/lena.png")
```

In this example, the energy of the image `lena.png` located in the `assets` directory is calculated.

## Output

The output is a plot with two images. The first image is the original image with the energy in the spatial domain displayed below it. The second image is the Fourier Transform of the original image with the energy in the frequency domain displayed below it. The title of the plot is "Parseval's Energy Theorem".