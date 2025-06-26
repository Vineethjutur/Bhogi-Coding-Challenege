# Bhogi Dish Viewer

**Bhogi Dish Viewer** is a full-stack mini project to display deduplicated dishes based on ingredient and flavor similarity. It features a Python + Flask backend and a React frontend with a clean, paginated interface.

## Project Structure
```
Bhogi Coding Challenge/
├── DataScience/
│ ├── data.csv
│ ├── selected_dishes.csv # Final 25 deduplicated dishes
├── SolutionDesign/
│ ├── api.py # Flask API exposing dishes by userId & page
│ ├── deduplicate_dishes.py # Runs similarity + generates final dishes
│ ├── deduplicate_logic.py # Contains logic for similarity and clustering
│ ├── Flavors.csv
│ ├── ingredients.csv
│ └── deduplicated_dishes.csv # Output from deduplication
├── dish_viewer/
│ └── src/
│ ├── App.js # React frontend logic
│ └── App.css # Custom styling
└── README.md

```
---

## How to Run

### 1. Backend (Flask API)

```bash
cd SolutionDesign
python3 -m venv venv
source venv/bin/activate      # Use venv\Scripts\activate on Windows
pip install flask flask-cors pandas scikit-learn
python api.py

Your API will run at: http://127.0.0.1:5003

Sample endpoint: http://127.0.0.1:5003/dishes?userId=123&page=0
```
### 2. Frontend (React)
```
cd dish_viewer
npm install
npm start
```
Frontend will run at: http://localhost:3000

Enter a user ID (any number) and click Fetch Dishes

View paginated, personalized dishes (5 per page × 5 pages)
