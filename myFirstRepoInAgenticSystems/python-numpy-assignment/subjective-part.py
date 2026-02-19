# creating a program using numpy library

import numpy as np

data = np.array([10, 20, 30, 40])
data_mean = np.mean(data)
data_std = np.std(data)
normalized = (data - data_mean) / data_std
reshaped_data = data.reshape(2,2)

print(f"Original data: {data}")
print(f"Mean of data: {data_mean}")
print(f"Standard Deviation of data: {data_std}")
print(f"Normalized data: {normalized}")
print(f"Reshaped data: {reshaped_data}")
print(f"Shape of reshaped data: {reshaped_data.shape}")
