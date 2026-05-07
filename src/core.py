import numpy as np

def extract_gradients(mu):
    """
    Extracts the discrete spatial gradient array (backward drops) from a signal.
    Formula: delta_k = mu_k - mu_{k+1}
    """
    # Append 0 to handle the implicit boundary condition at the tail
    return -np.diff(np.append(mu, 0))

def reconstruct_signal(delta):
    """
    Reconstructs the morphological signal from its gradient array via backward integration.
    """
    return np.cumsum(delta[::-1])[::-1]

def morphological_convolution(mu, nu):
    """
    Computes the structural convolution (mu * nu) via gradient polynomial multiplication.
    """
    drops_mu = extract_gradients(mu)
    drops_nu = extract_gradients(nu)
    
    # Algebraic convolution of generative arrays
    drops_lambda = np.convolve(drops_mu, drops_nu)
    
    return reconstruct_signal(drops_lambda)

def spatial_derivative(mu):
    """
    Applies the spatial derivation operator (\partial_z).
    Acts as a high-pass filter: suppresses DC component and shift-weights the tail.
    Formula: delta'_k = k * delta_{k+1}
    """
    delta = extract_gradients(mu)
    
    # If the signal is completely flat (or empty), derivative is 0
    if len(delta) <= 1:
        return np.array([0])
        
    new_delta = np.zeros(len(delta) - 1, dtype=int)
    
    # 0-indexed Python array loop matching the 1-indexed math formula
    for i in range(len(new_delta)):
        k = i + 1  # Mathematical index
        new_delta[i] = k * delta[i + 1]
        
    return reconstruct_signal(new_delta)

def plateau_operator(mu):
    """
    Applies the discrete spatial integration / Plateau operator (\mathcal{J}).
    Translates the gradient array rightward and zero-pads the boundary.
    """
    delta = extract_gradients(mu)
    
    # Insert a zero gradient at the head to create the structural plateau
    new_delta = np.insert(delta, 0, 0)
    
    return reconstruct_signal(new_delta)
