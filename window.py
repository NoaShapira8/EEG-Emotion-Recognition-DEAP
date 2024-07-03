import numpy as np
import pandas as pd
from frequency_band import *

class Window:
    def __init__(self, window_num):
        self.window_num = window_num
        self.size = 2 # seconds
        self.step_size = 0.125 # seconds
        self.frequency_bands = {}
    
    def get_window_num(self):
        return self.window_num
    
    def get_size(self):
        return self.size
    
    def get_step_size(self):
        return self.step_size
    
    def get_frequency_bands(self):
        return self.frequency_bands
    
    def add_frequency_band(self, band_name, band_inst):
        assert band_name in ['delta', 'theta', 'alpha', 'beta', 'gamma'], 'Invalid band name'
        self.frequency_bands[band_name] = band_inst
        
    def get_frequency_band(self, band_name):
        return self.frequency_bands[band_name]