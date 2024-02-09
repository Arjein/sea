from filterpy.kalman import KalmanFilter
from filterpy.common import Q_discrete_white_noise
import numpy as np
import matplotlib.pyplot as plt



"""
alman Filter Initialization:
The initial state is set using the first measured position and an assumed initial velocity of 0.
The state transition matrix F, measurement function H, and initial covariance matrix P are defined as before.
The measurement noise variance R is set based on the previously calculated estimate.
Process noise Q is assumed to be white noise with a small variance, 
indicating a relatively high confidence in the model's predictions between measurements.

"""
def apply_kalman_filter(true_positions, measured_positions):
    # Automatically estimate measurement noise variance
    measurement_errors = np.array(measured_positions) - np.array(true_positions)
    measurement_noise_variance = np.var(measurement_errors)
    
    # Initialize the Kalman Filter
    kf = KalmanFilter(dim_x=2, dim_z=1)
    kf.x = np.array([measured_positions[0], 0.])  # Initial state (position and velocity)
    kf.F = np.array([[1., 1.], [0., 1.]])  # State transition matrix
    kf.H = np.array([[1., 0.]])  # Measurement function
    kf.P *= 1000.                 # Initial covariance matrix, large value indicating initial state uncertainty
    kf.R = measurement_noise_variance  # Use the estimated measurement noise variance
    kf.Q = Q_discrete_white_noise(dim=2, dt=1., var=0.01)  # Process noise, assumed small
    
    # Kalman Filter Process
    estimated_positions = []
    for z in measured_positions:
        kf.predict()
        kf.update(z)
        estimated_positions.append(kf.x[0])
    
    
    return estimated_positions
