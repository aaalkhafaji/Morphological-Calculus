# Morphological-Calculus
Python implementation of Morphological Hopf Algebras for Digital Signal Processing.
# Morphological Hopf Algebras for Digital Signal Processing

This repository contains the Python implementation for the paper: **"Morphological Hopf Algebras for Digital Signal Processing: An Algebraic Calculus for Discrete Structural Filtering."**

It demonstrates the application of discrete difference operator polynomials and the Morphological Hopf framework to 1D and 2D digital signals.

## Files Included
* `morphological_calculus.py`: The core implementation of the Spatial Calculus ($\partial_z$ and $\mathcal{J}$) and the Discrete Morphological Convolution ($\star$).
* `a4.png`: A sample 2D image used to demonstrate the separable 2D filtering application.

## Requirements
To run this code, you will need Python 3 and the following libraries:
* `numpy`
* `matplotlib`
* `Pillow` (PIL)

## How to Run
Simply execute the script from your terminal or command prompt:
`python morphological_calculus.py`

The script will:
1. Generate the 1D benchmark plots (`example-image-a.pdf` and `example-image-b.pdf`) used in the empirical validation section of the paper.
2. Load `a4.png`, add Additive White Gaussian Noise (AWGN), and apply the $\star$ algebra separably to reconstruct the image.
