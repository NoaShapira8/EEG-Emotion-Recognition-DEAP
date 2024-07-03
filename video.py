import numpy as np
import pandas as pd
from window import *


class Video:
    def __init__(self, video_num : int, video_data, video_label):
        self.video_num = video_num
        self.data = video_data # 2D pandas dataframe
        self.label = video_label # 1D pandas dataframe
        self.windows = {}
        
    def add_window(self, window_num):
        self.windows[window_num] = Window(window_num)
        
    def get_video_num(self):
        return self.video_num
    
    def get_video_data(self):
        return self.data
    
    def get_data(self):
        return self.data
    
    def get_label(self):
        return self.label
    
    def get_windows(self):
        return self.windows
    