import numpy as np
import pandas as pd

class Window:
    def __init__(self, window_num, window_data):
        self.window_num = window_num
        self.window_data = window_data  # 1D pandas dataframe , fft power values of the window (only positive frequencies)
        self.frequency_bands = {'delta': 0, 'theta': 0, 'alpha': 0, 'beta': 0, 'gamma': 0}
        self.frequency_bands_values = np.array([])
        self.freq_range = {'delta': (1, 3), 'theta': (4, 7), 'alpha': (8, 13), 'beta': (14, 30), 'gamma': (31, 50)}
        #self.add_frequency_band()
    
    def get_window_num(self) -> int:
        return self.window_num
    
    def get_frequency_bands(self) -> dict:
        return self.frequency_bands
    
    def get_frequency_bands_values(self) -> np.array:
        return self.frequency_bands_values  # 1D numpy array , fft power values of the window (only positive frequencies)
    
    def get_window_data(self) -> pd.DataFrame:
        return self.window_data  # 1D pandas dataframe , fft power values of the window (only positive frequencies)
    
    def add_frequency_band(self, band_name, band_value):
        assert band_name in self.freq_range, "Invalid frequency band name"
        self.frequency_bands[band_name] = band_value
        self.frequency_bands_values = np.append(self.frequency_bands_values, band_value)
        
    def aggregate_frequency_bands(self):
        # Calculate FFT frequencies
        sampling_rate = len(self.window_data) # 128 Hz
        window_time_size = sampling_rate * 2 # 256 samples (2 seconds)
        fft_freqs = np.fft.fftfreq(window_time_size, d=1/sampling_rate)

        # Initialize arrays to store band sums and band names
        self.frequency_bands = {band: 0 for band in self.freq_range}
        self.frequency_bands_values = np.array([])

        # Aggregate powers in each band
        for band, (low, high) in self.freq_range.items():
            band_indices = np.where((fft_freqs >= low) & (fft_freqs <= high))
            band_power_spectrum = self.window_data.iloc[band_indices].values
            band_power_sum = np.sum(band_power_spectrum)
            self.frequency_bands[band] = band_power_sum
            self.frequency_bands_values = np.append(self.frequency_bands_values, band_power_sum)
        
    def get_frequency_band(self, band_name) -> float:
        return self.frequency_bands[band_name]