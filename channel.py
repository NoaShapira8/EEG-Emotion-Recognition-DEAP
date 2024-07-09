import numpy as np
import pandas as pd
from window import *

class Channel:
    def __init__(self, channel_num, channel_data):
        self.channel_num = channel_num
        self.data = channel_data #  1D pandas dataframe , time domain data
        self.windows = {}
        #self.create_windows()
         
    def get_channel_num(self):
        return self.channel_num
    
    def get_data(self):
        return self.data
    
    def get_channel_data(self):
        return self.data
    
    def get_windows(self):
        return self.windows
    
    def get_window(self, window_num):
        return self.windows[window_num]
    
    def get_windows_num(self):
        return len(self.windows)
    
    def add_window(self, window_num, window_data):
        self.windows[window_num] = Window(window_num, window_data)
    
    def perform_fft(self, window_data):
        # Perform FFT on the window data , here window data size is 256 samples in time domain
        fft_output =  np.fft.fft(window_data)
        fft_magnitude = np.abs(fft_output)
        fft_magnitude = fft_magnitude[0:len(fft_magnitude) // 2]  # Keep only the positive frequencies within the range from 0 to the Nyquist frequency
        return pd.DataFrame(fft_magnitude)
    
    def create_windows(self):
        step_size = 0.125 # seconds
        window_size = 256 # samples (128 Hz * 2 seconds)
        window_jump = int(window_size * step_size) # 32 samples
        index = 0
        for i in range(0, len(self.data) - window_size + 1, window_jump):
            window_data = self.data.iloc[i : i + window_size]
            window_freq_data = self.perform_fft(window_data)  # Perform FFT on the window data , here window_freq_data size is 128 samples in frequencey domain
            self.windows[index] = Window(index, window_freq_data)
            index += 1
            