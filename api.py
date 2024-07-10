from person import *
import pandas as pd
import pickle
import numpy as np


class Api():
    def __init__(self):
        self.persons = {}
        self.create_persons()
        
    def add_person(self, person_num, file_path):
        self.persons[person_num] = Person(person_num, file_path)
        
    def get_person(self, person_num):
        return self.persons[person_num]
    
    def get_persons(self):
        return self.persons

    def create_persons(self):
        for i in range(1, 33):
            file_path = f'./deap_orig/data_preprocessed_python/s{i:02d}.dat'
            self.add_person(i, file_path)
    
    def create_person_df(self, person_num) -> pd.DataFrame:
        df_person = pd.DataFrame()
        person = self.get_person(person_num)
        for video_index in range(len(person.get_videos())):
            video_num = person.get_video(video_index)
            df_video_num = pd.DataFrame()
            number_of_window = 245
            number_of_channels = 14
            for window_index in range(number_of_window):
                df_horizontal = pd.DataFrame()
                for i in range(number_of_channels):
                    channel_num = video_num.get_channel(i)  # person 1 video num channel i
                    window_num = channel_num.get_window(window_index) # person 1 video num channel i window index
                    window_num.aggregate_frequency_bands()
                    freq_bands_values = window_num.get_frequency_bands_values()
                    df_horizontal = pd.concat([df_horizontal, pd.DataFrame([freq_bands_values])], axis=1, ignore_index=True)
                df_video_num = pd.concat([df_video_num, df_horizontal], axis = 0, ignore_index = True)
            df_person = pd.concat([df_person, df_video_num], axis = 0, ignore_index = True)
        return df_person