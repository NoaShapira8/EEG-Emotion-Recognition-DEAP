import pandas as pd
import pickle
import os
import numpy as np

# Define the relative file path
file_path = './deap_orig/data_preprocessed_python/s02.dat'

# Load the .dat file
with open(file_path, 'rb') as file:
    data = pickle.load(file, encoding='latin1')  # Adjust encoding as necessary

# Check the type of the data loaded
print(type(data))

# Inspect the keys of the dictionary
print("Keys:", data.keys())

# Inspect the structure of each key's data
for key in data:
    print(f"Key: {key}")
    print(f"Type: {type(data[key])}")
    print(f"Shape/Length: {getattr(data[key], 'shape', len(data[key]))}")

# Further inspection if needed
#print(data['data'])  # Uncomment to inspect specific keys



# Example key names; adjust based on actual inspection
eeg_data_key = 'data'
labels_key = 'labels'

# Flatten the EEG data
eeg_data = data[eeg_data_key]  # Assuming this is a numpy array of shape (trials, channels, samples)
eeg_data_flat = eeg_data.reshape(eeg_data.shape[0], -1)  # Flatten the channel and sample dimensions

# Combine with labels
labels = data[labels_key]  # Assuming this is a 2D array (trials, label_dim)
combined_data = np.hstack((eeg_data_flat, labels))

# Create DataFrame with appropriate column names
column_names = [f'channel_{i}_sample_{j}' for i in range(eeg_data.shape[1]) for j in range(eeg_data.shape[2])]
label_names = [f'label_{i}' for i in range(labels.shape[1])]
all_column_names = column_names + label_names

df = pd.DataFrame(combined_data, columns=all_column_names)
print(df.head())
