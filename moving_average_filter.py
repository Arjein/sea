import numpy as np
import matplotlib.pyplot as plt
# Easiest one, not complex as the others.
def moving_average_filter(measured_positions, window_size):
    # Convert the measured positions to a numpy array if not already one
    measured_positions = np.array(measured_positions)
    
    # Compute the moving average using a convolution operation
    weights = np.ones(window_size) / window_size
    smoothed_positions = np.convolve(measured_positions, weights, mode='same')
    
    return smoothed_positions
