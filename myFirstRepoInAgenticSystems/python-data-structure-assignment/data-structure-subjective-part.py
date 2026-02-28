import numpy as np

# setup
np.random.seed(42)

# create a 2D- numpy array
data = np.random.rand(100,3)

# statistical calculation for each column
mean_val = np.mean(data, axis=0)
std_val = np.std(data, axis=0)

# normalization
normalized_data = (data-mean_val)/std_val

# slicing
train_data = normalized_data[:80]
test_data = normalized_data[80:]

# view
train_data[0,0] = 555.55

# print results
print(f"Original data shape: {data.shape}")
print(f"Mean shape: {mean_val.shape}")
print(f"Training data shape: {train_data.shape}")
print(f"Test data shape: {test_data.shape}")
print("Explanation")
print("Because we sliced the array, 'train_data' is just a 'view'.")
print(f"The value at normalized_data[0,0] is now {normalized_data[0,0]}")
print("Note: Modifying the slice affected the original array")
