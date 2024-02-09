import pywt
import numpy as np
import matplotlib.pyplot as plt

def wavelet_denoise(data, wavelet, level):
    """
    Apply wavelet denoising to a 1D signal.
    
    Parameters:
    - data: The 1D array of measurements to denoise.
    - wavelet: The type of wavelet to use (e.g., 'db1', 'sym2').
    - level: The level of decomposition for the wavelet transform.
    
    Returns:
    - The denoised signal.
    """
    # Decompose to get the wavelet coefficients
    coeff = pywt.wavedec(data, wavelet, mode="per", level=level)
    # Calculate a threshold
    sigma = np.median(np.abs(coeff[-level])) / 0.6745
    threshold = sigma * np.sqrt(2 * np.log(len(data)))
    # Apply threshold to the detail coefficients (not the approximation)
    coeff[1:] = (pywt.threshold(i, value=threshold, mode='soft') for i in coeff[1:])
    # Reconstruct the signal
    return pywt.waverec(coeff, wavelet, mode="per")

# Example usage with synthetic data
np.random.seed(42)  # For reproducibility
true_positions = np.linspace(1, 100, 400)
measured_positions = true_positions + np.random.normal(0, 5, true_positions.shape)  # Adding Gaussian noise

# Denoising with Wavelet Transform
wavelet = 'db4'  # Daubechies wavelet
level = 2  # Level of decomposition
denoised_positions = wavelet_denoise(measured_positions, wavelet, level)
