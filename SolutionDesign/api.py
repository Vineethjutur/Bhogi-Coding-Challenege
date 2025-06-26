from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd
import random

app = Flask(__name__)
CORS(app)

# Load the selected dishes
df = pd.read_csv("../DataScience/selected_dishes.csv")
all_dishes = df['dish_name'].tolist()

@app.route('/dishes', methods=['GET'])
def get_dishes():
    user_id = request.args.get('userId', default=None, type=int)
    page = request.args.get('page', default=0, type=int)

    if user_id is None or page not in range(0, 5):
        return jsonify({"error": "Invalid userId or page number (must be 0–4)"}), 400

    random.seed(user_id)
    randomized = all_dishes.copy()
    random.shuffle(randomized)

    per_page = 5
    start = page * per_page
    end = start + per_page
    page_dishes = randomized[start:end]

    return jsonify({"dishes": page_dishes})

if __name__ == '__main__':
    app.run(port=5003, debug=True)
