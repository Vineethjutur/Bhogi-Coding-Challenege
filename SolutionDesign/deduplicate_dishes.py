# SolutionDesign/deduplicate_dishes.py

from deduplicate_logic import load_and_prepare_data, compute_similarity_matrix, get_deduplicated_dishes

# Load and prepare features
df_features = load_and_prepare_data("ingredients.csv", "Flavors.csv")
print("Feature matrix preview:")
print(df_features.head())

# Compute similarity
similarity_df = compute_similarity_matrix(df_features)

# Deduplicate
deduplicated_dishes = get_deduplicated_dishes(similarity_df, threshold=0.9)

# Print or export results
print("\nDeduplicated dishes:")
print(deduplicated_dishes[:25])  # Print first 25

# Save to CSV
import pandas as pd
pd.DataFrame({'deduplicated_dishes': deduplicated_dishes}).to_csv('deduplicated_dishes.csv', index=False)

