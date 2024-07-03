import pandas as pd
import numpy as np
import pickle
from video import *

class Person:
    def __init__(self, person_num, file_path):
        self.person_num = person_num
        self.file_path = file_path
        self.data = None
        self.labels = None
        self.labels_df = None
        self.database = self.set_database(self.file_path)
        self.videos = {}
        self.create_videos()
    
    def get_csv_path(self):
        return self.file_path
    
    def get_person_num(self):
        return self.person_num
    
    def set_database(self, file_path):
        with open(file_path, 'rb') as file:
            self.database = pickle.load(file, encoding='latin1')  # Adjust encoding as necessary
            
        assert 'data' in self.database, 'Invalid database'
        assert 'labels' in self.database, 'Invalid database'
        self.data = self.database['data'] # 3D numpy array (40, 40, 8064)
        self.labels = self.database['labels'] # 2D numpy array (40, 4)
        self.labels_df = pd.DataFrame(self.labels) # 2D pandas dataframe
                       
    def add_video(self, video_num, video_data, video_label):
        self.videos[video_num] = Video(video_num, video_data, video_label)
        
    def get_video(self, video_num):
        return self.videos[video_num]
    
    def get_videos(self):
        return self.videos

    def get_data(self):
        return self.data
    
    def get_labels(self):
        return self.labels
    
    def create_videos(self):
        for i in range(40):
            video_data = pd.DataFrame(self.data[i]).T # 2D pandas dataframe 
            # We wants to work with specific 14 channels according to the channel selection in thr Article (Table 1).
            # AF3 - 1 , F3 - 2 , F7 - 3 , FC5 - 4 , T4 - 7 , P7 - 11 , O0 - 13 , AF4 - 17 , F4 - 19 , F8 - 20 , FC6 - 21 , T8 - 25 , P8 - 28 , 02 - 31  (Channel content , DEAP index)
            columns_to_keep = [1, 2, 3, 4, 7, 11, 13, 17, 19, 20, 21, 25, 28, 31] 
            video_data = video_data.iloc[:, columns_to_keep]
            video_label = pd.DataFrame(self.labels[i]) # 1D pandas dataframe
            self.add_video(i, video_data, video_label)