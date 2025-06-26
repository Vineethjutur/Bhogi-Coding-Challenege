# SolutionDesign/deduplicate_logic.py

import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.metrics.pairwise import cosine_similarity

def load_and_prepare_data(ingredients_path, flavors_path):
    df_ingredients = pd.read_csv(ingredients_path).dropna()
    df_flavors = pd.read_csv(flavors_path).dropna()

    df_combined = pd.merge(df_ingredients, df_flavors, on="dish_name", how="inner")
    df_combined.set_index("dish_name", inplace=True)

    return df_combined

def compute_similarity_matrix(feature_df):
    taste_cols = ['sweet', 'salty', 'sour', 'bitter', 'umami']
    aggregated = feature_df.groupby('dish_name')[taste_cols].mean()
    scaler = StandardScaler()
    scaled_features = scaler.fit_transform(aggregated)
    similarity_matrix = cosine_similarity(scaled_features)
    similarity_df = pd.DataFrame(similarity_matrix, index=aggregated.index, columns=aggregated.index)
    return similarity_df


def get_deduplicated_dishes(similarity_df, threshold=0.9):
    seen = set()
    unique_dishes = []

    for dish in similarity_df.index:
        if dish in seen:
            continue
        similar = similarity_df.loc[dish][similarity_df.loc[dish] >= threshold].index.tolist()
        seen.update(similar)
        unique_dishes.append(dish)

    return unique_dishes
