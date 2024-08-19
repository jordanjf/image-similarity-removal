# Image Similarity Removal

This is a Python script to remove similar images from a directory based on Structural Similarity (SSIM). It compares images and deletes those with a similarity higher than a configurable threshold (80% by default).

## Features

- Compares images in a directory.
- Deletes images with similarity above a certain threshold.
- Supports various image formats (JPG, PNG, BMP, etc.).

## Requirements

- Python 3.x
- Required libraries:
  - `opencv-python`
  - `scikit-image`
  - `numpy`

## Usage
Run the script by passing the path to the directory containing the images:
python exclui_semelhantes.py
## Contributions
Contributions are welcome! If you find any issues or want to improve the project, feel free to open an issue or submit a pull request.
## License
This project is licensed under the Apache License 2.0. See the LICENSE file for more details.

## Example

Suppose you have the following images in a folder "imagens":

- image1.jpg
- image2.jpg
- image3.jpg

After running the script:

```bash
python exclui_semelhantes.py
```

## Install the dependencies
You can install the dependencies using the following command:

```bash
pip install opencv-python scikit-image numpy
