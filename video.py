import numpy as np
import pandas as pd
from channel import *


class Video:
    def __init__(self, video_num : int, video_data, video_label):
        self.video_num = video_num
        self.data = video_data # 2D pandas dataframe
        self.label = video_label # 1D pandas dataframe
        self.channels = {}
        self.build_channels()
        
    def get_video_num(self):
        return self.video_num
    
    def get_video_data(self):
        return self.data
    
    def get_data(self):
        return self.data
    
    def get_label(self):
        return self.label
    
    def get_channel(self, channel_num):
        return self.channels[channel_num]
    
    def get_channels(self):
        return self.channels
    
    def build_channels(self):
        for i in range(self.data.shape[1]):
            self.channels[i] = Channel(i, self.data.iloc[:, i])