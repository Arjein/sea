import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
from filterpy.monte_carlo import systematic_resample

def particle_filter(true_positions, measured_positions, N):
    # Estimate measurement noise variance from the data
    measurement_diffs = np.diff(measured_positions)
    process_noise_variance = np.var(measurement_diffs)  # Estimate process noise as variance of measurement differences
    measurement_noise_variance = np.var(measured_positions - true_positions)
    
    # Initialize particles and weights
    particles = np.random.normal(np.mean(measured_positions), np.sqrt(measurement_noise_variance), size=(N, 1))
    weights = np.ones(N) / N
    
    estimated_positions = []
    
    for z in measured_positions:
        # Predict step: Adjust particles based on estimated process noise
        particles += np.random.normal(0, np.sqrt(process_noise_variance), size=(N, 1))
        
        # Update step: Correctly handle the calculation of weights
        weights *= norm.pdf(z, loc=particles.flatten(), scale=np.sqrt(measurement_noise_variance))
        weights += 1.e-300      # Avoid round-off to zero
        weights /= np.sum(weights)  # Normalize
        
        # Resample if necessary
        if 1. / np.sum(weights**2) < N/2:
            indexes = systematic_resample(weights)
            particles[:] = particles[indexes]
            weights.fill(1.0 / N)
        
        # Estimate position
        estimated_position = np.average(particles, weights=weights, axis=0)
        estimated_positions.append(estimated_position)
    
    return np.array(estimated_positions).flatten()

