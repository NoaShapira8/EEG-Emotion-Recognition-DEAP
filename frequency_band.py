import numpy as np
import pandas as pd


class Frequency_band:
    def __init__(self, band_name):
        self.band_name = band_name
        self.band_range = self.get_band_range(band_name)
        self.band_values =  None
        
    def get_band_name(self):
        return self.band_name
    
    def get_band_range(self, band_name):
        if band_name == 'delta':
            return (1, 3)
        elif band_name == 'theta':
            return (4, 7)
        elif band_name == 'alpha':
            return (8, 13)
        elif band_name == 'beta':
            return (14, 30)
        elif band_name == 'gamma':
            return (31, 50)
        else:
            return None
