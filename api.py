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