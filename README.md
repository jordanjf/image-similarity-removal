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

You can install the dependencies using the following command:

```bash
pip install opencv-python scikit-image numpy
