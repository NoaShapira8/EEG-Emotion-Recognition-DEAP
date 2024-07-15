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
    
    def create_data_person_df(self, person_num) -> pd.DataFrame:
        df_person = pd.DataFrame()
        person = self.get_person(person_num)
        for video_index in range(len(person.get_videos())):
            video_num = person.get_video(video_index)
            df_video_num = pd.DataFrame()
            number_of_window = 488
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
            print(f"finish aggregating frequency bands for video {video_index} in person {person_num}")
            df_person = pd.concat([df_person, df_video_num], axis = 0, ignore_index = True)
        return df_person
    
    def create_emotion_person_label_df(self, person_num, emotion_index) -> pd.DataFrame:
        # emotion_index = 0 - valence, 1 - arousal, 2 - dominance, 3 - liking 
        assert emotion_index in range(4), "Invalid emotion index"
        score = 9
        person_inst = self.get_person(person_num)
        df_person_emotion_label = pd.DataFrame()
        person_labels = person_inst.get_labels()
        round_labels = np.round(person_labels).astype(int)
        emotion = round_labels[:, emotion_index]

        # Create a zero matrix with rows equal to the length of the array and score columns
        emotion_matrix = np.zeros((len(emotion), score), dtype=int) # (40 * 9)
        # Set the appropriate elements to 1
        for i, val in enumerate(emotion):
            emotion_matrix[i, val-1] = 1  # val-1 to convert 1-based index to 0-based index
            
        # Repeat each row 488 times # number of windows
        repeated_label = np.repeat(emotion_matrix, 488, axis=0)
        df_person_emotion_label = pd.DataFrame(repeated_label, columns=[f'{i+1}' for i in range(9)])
        return df_person_emotion_label
    
    def create_nerlent_df_person(self, person_num, emotion_index) -> pd.DataFrame:
        df_person = self.create_data_person_df(person_num)
        print(f"finish creating data for person {person_num}")
        df_person_label = self.create_emotion_person_label_df(person_num, emotion_index)
        print(f"finish creating emotion label df for person {person_num}")
        df_person = pd.concat([df_person, df_person_label], axis = 1, ignore_index = True)
        return df_person