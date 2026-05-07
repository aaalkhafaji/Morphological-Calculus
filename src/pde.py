import numpy as np
from .core import extract_gradients, reconstruct_signal

def discrete_heat_equation_step(mu, alpha=0.5):
    """
    Executes one forward temporal step of the Discrete Morphological Heat Equation.
    Models structural diffusion (Gaussian blurring of edges).
    Formula: delta_k(t+1) = delta_k(t) - alpha * k(k+1) * delta_{k+2}(t)
    """
    delta = extract_gradients(mu)
    new_delta = np.copy(delta).astype(float)
    
    n = len(delta)
    
    for i in range(n - 2):
        k = i + 1  # Mathematical spatial index
        dissipation = alpha * k * (k + 1) * delta[i + 2]
        new_delta[i] = delta[i] - dissipation
        
    # Ensure non-negative gradients to maintain monotonicity (if alpha is large)
    new_delta = np.maximum(new_delta, 0)
    
    # Return rounded integers to maintain digital array quantization
    return reconstruct_signal(np.round(new_delta).astype(int))

def discrete_transport_equation_step(mu, c=1.0):
    """
    Executes one forward temporal step of the Discrete Morphological Transport Equation.
    Models spatially amplified wave advection.
    Formula: delta_k(t+1) = delta_k(t) + c * k * delta_{k+1}(t)
    """
    delta = extract_gradients(mu)
    new_delta = np.copy(delta).astype(float)
    
    n = len(delta)
    
    for i in range(n - 1):
        k = i + 1  # Mathematical spatial index
        advection = c * k * delta[i + 1]
        new_delta[i] = delta[i] + advection
        
    return reconstruct_signal(np.round(new_delta).astype(int))
