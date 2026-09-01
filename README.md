# Image Processing Lab

This repository contains Image Processing laboratory assignments implemented in Python using simple, manual image-processing logic. OpenCV is used mainly for reading and saving images, while NumPy is used for basic array operations. Ready-made OpenCV processing functions are avoided where the assignment asks for the algorithm itself.

## Assignments

- **Assignment 1** - Grayscale to binary using mean threshold and user-defined threshold
- **Assignment 2** - RGB to grayscale using mean and user-defined channel weights
- **Assignment 3** - Image border/padding and image complement for grayscale and binary images
- **Assignment 4** - Log transform, gamma transform and contrast stretching
- **Assignment 6** - Averaging, weighted and Gaussian smoothing using manual convolution

> Assignment 5 will be added when the question is provided.

## Structure

```text
image_processing_lab/
├── README.md
├── Assignment1.ipynb
├── Assignment2.ipynb
├── Assignment3.ipynb
├── Assignment4.ipynb
├── Assignment6.ipynb
├── images/
│   └── sample_image.png
└── outputs/
    ├── assignment1/
    ├── assignment2/
    ├── assignment3/
    ├── assignment4/
    └── assignment6/
```

The notebooks already contain executed sample runs and embedded output images. Running a notebook again saves its generated images into the corresponding `outputs/assignmentX/` folder.

## Requirements

```text
opencv-python
numpy
```
