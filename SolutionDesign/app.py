from flask import Flask, request, jsonify
from flask_cors import CORS
from deduplicate_logic import load_and_prepare_data, compute_similarity_matrix, get_deduplicated_dishes

app = Flask(__name__)
CORS(app)  # Enable CORS for React frontend

# Load and compute once (you can cache for performance)
df_features = load_and_prepare_data("ingredients.csv", "Flavors.csv")
similarity_df = compute_similarity_matrix(df_features)
deduplicated_dishes = get_deduplicated_dishes(similarity_df, threshold=0.9)

# Pagination API
@app.route('/dishes', methods=['GET'])
def get_paginated_dishes():
    user_id = request.args.get('userId', default='1', type=str)
    page = request.args.get('page', default=0, type=int)
    per_page = 5  

    start = page * per_page
    end = start + per_page
    paginated = deduplicated_dishes[start:end]

    return jsonify({
        "userId": user_id,
        "page": page,
        "dishes": paginated
    })

if __name__ == '__main__':
    app.run(port=5004)
