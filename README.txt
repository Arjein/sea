How to run: python3 main.py -f <Filter method to use: kalman, particle, maf, savgol, wavelet")>

Analysis options for GP2Y0A60SZ0F/GP2Y0A60SZLF:

NOTE: There are various Kalman filters. However, as far as i understood, 
they are not appropriate for our case since they require non-linearity in measurement. If necessary i will implement it.

Standard (Linear) Kalman Filter:    
Designed for linear systems with Gaussian noise. It consists of a set of mathematical equations 
providing an efficient computational means to estimate the state of a linear process.

1. Particle Filtering: 
Also known as Sequential Monte Carlo methods, particle filters are 
a set of genetic-type particle Monte Carlo methodologies aimed at implementing a recursive 
Bayesian filter by Monte Carlo simulations. Particle filters can manage non-linear and non-Gaussian systems,
making them more flexible in certain applications than Kalman filters.

2.Bayesian Filtering: 
This method provides a powerful framework for predicting the state of dynamic systems. 
It updates the state estimate based on new measurements, incorporating the uncertainty associated with sensor errors and the predicted state. 
Bayesian filters can be a base for more complex filtering techniques, including both Kalman and particle filters.

3. Moving Average Filter (MAF): 
A simpler method that can be effective in reducing noise is the moving average filter,
which smooths data by creating an average of different subsets of the full data set. It's easy to implement 
and can be useful for data with a constant statistical profile.

4. Savitzky-Golay Filter: 
This filter essentially performs a local polynomial regression on a 
series of values to determine the smoothed value for each data point. It can provide the advantage of 
preserving the features of the signal better than a simple moving average, especially when you're interested 
in capturing the signal's peak and width accurately.

5. Wavelet Transform: 
This technique is useful for analyzing non-stationary signals. 
It decomposes a signal into components at various scales, allowing for the analysis of signal characteristics 
that vary over time. Wavelet transform can be particularly useful for identifying transient features and anomalies in sensor data.

6. Adaptive Filtering: 
Adaptive filters modify their parameters (coefficients) according to an adaptive algorithm, 
allowing them to perform well even when the statistical characteristics of the input signal 
or the underlying system are changing. They're particularly useful in scenarios
 where the sensor data is affected by time-varying phenomena.

7. Signal Decomposition (Empirical Mode Decomposition - EMD): 
EMD decomposes a signal into a set of intrinsic mode functions (IMFs) 
with the goal of analyzing the original signal at different scales or frequencies.
This can be particularly useful for non-linear and non-stationary time series data analysis.
