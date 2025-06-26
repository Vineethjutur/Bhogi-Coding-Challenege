import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import euclidean_distances

# Load dataset
df = pd.read_csv("DataScience/data.csv")

# Define target flavor profiles
target_profiles = {
    "savory": [10, 15, 25, 5, 45],
    "sweet": [65, 10, 5, 10, 10],
    "mixed": [15, 30, 25, 10, 20],
}

# Prepare feature matrix
flavor_cols = ['sweet', 'sour', 'salty', 'bitter', 'umami']
X = df[flavor_cols].values

# Compute distances and store them
for profile_name, target in target_profiles.items():
    target_array = np.array(target).reshape(1, -1)
    df[f'distance_to_{profile_name}'] = euclidean_distances(X, target_array).flatten()

# Select closest dishes
savory_dishes = df.nsmallest(15, 'distance_to_savory')
sweet_dishes = df.nsmallest(5, 'distance_to_sweet')
mixed_dishes = df.nsmallest(5, 'distance_to_mixed')

# Combine into one list
final_dishes = pd.concat([savory_dishes, sweet_dishes, mixed_dishes], ignore_index=True)

# Save or print result
print("Final 25 selected dishes:")
print(final_dishes[['dish_name']])

# save to CSV
final_dishes[['dish_name']].to_csv("DataScience/selected_dishes.csv", index=False)
