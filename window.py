import numpy as np
import pandas as pd

class Window:
    def __init__(self, window_num, window_data):
        self.window_num = window_num
        self.window_data = window_data  # 1D pandas dataframe , fft magnitude values of the window (only positive frequencies)
        self.frequency_bands = {'delta': 0, 'theta': 0, 'alpha': 0, 'beta': 0, 'gamma': 0}
        self.frequency_bands_values = np.array([])
        self.freq_range = {'delta': (1, 3), 'theta': (4, 7), 'alpha': (8, 13), 'beta': (14, 30), 'gamma': (30, 50)}
        #self.add_frequency_band()
    
    def get_window_num(self):
        return self.window_num
    
    def get_frequency_bands(self):
        return self.frequency_bands
    
    def get_frequency_bands_values(self):
        return self.frequency_bands_values
    
    def add_frequency_band(self, band_name, band_value):
        assert band_name in self.freq_range, "Invalid frequency band name"
        self.frequency_bands[band_name] = band_value
        self.frequency_bands_values = np.append(self.frequency_bands_values, band_value)
        
    def aggregate_frequency_bands(self):
        # Calculate FFT frequencies
        sampling_rate = len(self.window_data)    # 128 Hz
        fft_freqs = np.fft.fftfreq(sampling_rate, d=1/sampling_rate)

        # Initialize arrays to store band sums and band names
        self.frequency_bands = {band: 0 for band in self.freq_range}

        # Aggregate magnitudes in each band
        for band, (low, high) in self.freq_range.items():
            band_indices = np.where((fft_freqs >= low) & (fft_freqs < high))
            band_magnitudes = self.window_data.iloc[band_indices].values
            magnitude_sum = np.sum(band_magnitudes)
            self.frequency_bands[band] = magnitude_sum
            self.frequency_bands_values = np.append(self.frequency_bands_values, magnitude_sum)
        
    def get_frequency_band(self, band_name):
        return self.frequency_bands[band_name]