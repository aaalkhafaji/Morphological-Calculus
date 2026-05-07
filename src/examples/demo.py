import numpy as np
import sys
import os

# Add the parent directory to the path to import src modules
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.core import (
    morphological_convolution, 
    spatial_derivative, 
    plateau_operator
)
from src.pde import (
    discrete_heat_equation_step, 
    discrete_transport_equation_step
)

def run_paper_examples():
    print("--- 1. LSI Filtering (Differential Convolution) ---")
    # Section 3.C: mu = (2,1) star nu = (2,1)
    mu_conv = [2, 1]
    nu_conv = [2, 1]
    lambda_conv = morphological_convolution(mu_conv, nu_conv)
    print(f"Input: {mu_conv} star {nu_conv}")
    print(f"Output: {lambda_conv.tolist()}  (Expected: [4, 3, 1])\n")

    print("--- 2. The Spatial Derivative (High-Pass Filter) ---")
    # Section 5.B: partial(4, 2, 1)
    mu_deriv = [4, 2, 1]
    derived_signal = spatial_derivative(mu_deriv)
    print(f"Input: {mu_deriv}")
    print(f"Derived Output: {derived_signal.tolist()}  (Expected: [3, 2])\n")

    print("--- 3. The Plateau Operator (Spatial Delay) ---")
    # Section 6.C: J(4, 2, 1)
    mu_plat = [4, 2, 1]
    integrated_signal = plateau_operator(mu_plat)
    print(f"Input: {mu_plat}")
    print(f"Integrated Output: {integrated_signal.tolist()}  (Expected: [4, 4, 2, 1])\n")

    print("--- 4. Discrete Morphological Heat Equation ---")
    # Section 8.A.1: mu(0) = (3, 2, 1), alpha = 0.5
    mu_heat = [3, 2, 1]
    diffused_signal = discrete_heat_equation_step(mu_heat, alpha=0.5)
    print(f"Input t=0: {mu_heat}")
    print(f"Diffused t=1: {diffused_signal.tolist()}  (Expected: [2, 2, 1])\n")

    print("--- 5. Discrete Morphological Transport Equation ---")
    # Section 8.B.1: mu(0) = (1, 1, 1), c = 1.0
    mu_trans = [1, 1, 1]
    advected_signal = discrete_transport_equation_step(mu_trans, c=1.0)
    print(f"Input t=0: {mu_trans}")
    print(f"Advected t=1: {advected_signal.tolist()}  (Expected: [3, 3, 1])\n")

if __name__ == "__main__":
    run_paper_examples()
