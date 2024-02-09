# https://github.com/MikroElektronika/mikrosdk_click_v2/tree/master/clicks/irdistance
from kalman_analysis import apply_kalman_filter
from moving_average_filter import moving_average_filter
from particle_analysis import particle_filter
from scipy.signal import savgol_filter
import matplotlib.pyplot as plt
import numpy as np
import argparse
from wavelet_transform import wavelet_denoise

def generate_synthetic_data(length=50):
    true_distance = np.linspace(0, 100, length)
    measured_distance = true_distance + np.random.normal(0, 10, length)
    return true_distance, measured_distance

def visualize_results(filter_name,true_distance, measured_distance, estimated_distance):
    # Visualization
    plt.figure(figsize=(10, 6))
    plt.plot(true_distance, 'k-', label='True Position')
    plt.scatter(range(len(measured_distance)), measured_distance, color='red', label='Measured Position', alpha=0.5)
    plt.plot(estimated_distance, 'b--', label=f'Estimated Position ({filter_name})')
    plt.legend()
    plt.xlabel('Time Step')
    plt.ylabel('Position')
    plt.title(f'{filter_name} for Position Estimation')
    plt.show()

def apply_filter(filter_name, true_distance, measured_distance, window_size, N):
    if filter_name == 'kalman':
        return apply_kalman_filter(true_distance,measured_distance)
    
    elif filter_name == 'maf':
        if window_size is None:
            raise ValueError("Window size must be specified for MAF.")
        return moving_average_filter(measured_distance, window_size)
    
    elif filter_name == 'particle':
        return particle_filter(true_distance, measured_distance, N)
    
    elif filter_name == 'savgol':
        return savgol_filter(measured_distance, window_length=11, polyorder=3) # I have no idea about these parameters. 
    
    elif filter_name == "wavelet":
        return wavelet_denoise(measured_distance,"db4",2) # I have no idea about these parameters. 
    
    else:
        raise ValueError(f"Unknown filter: {filter_name}")


def main(filter_name, window_size, N=1000):
    true_distance, measured_distance = generate_synthetic_data()
    filtered_distance = apply_filter(filter_name, true_distance, measured_distance, window_size, N)
    if filter_name == 'kalman':
        f = "Kalman Filter"
    elif filter_name == 'maf':
        f = "Moving Average Filter"
    elif filter_name == 'particle':
        f = "Particle Filter"
    elif filter_name == 'savgol':
        f = "Savitzky-Golay Filter"
    elif filter_name == 'wavelet':
        f = "Wavelet Transform"

    visualize_results(f,true_distance, measured_distance, filtered_distance)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Filter sensor data using specified filter method.")
    parser.add_argument('-f', '--filter', choices=['maf', 'particle', 'kalman', "savgol", "wavelet"], required=True, help="Filter method to use: kalman, particle, or maf")
    parser.add_argument('-w', '--window_size', type=float, default=2, help="Window size for MAF. Required if -f MAF is chosen.")
    parser.add_argument('-N', type=int, default=1000, help="Number of particles for particle filter. Used if -f particle is chosen.")
    
    args = parser.parse_args()
    
    if args.filter == 'MAF' and args.window_size is None:
        parser.error("Window size (-w) must be specified if using MAF.")
    
    main(args.filter, args.window_size, args.N)
    

