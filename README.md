# Bhogi Dish Viewer

**Bhogi Dish Viewer** is a full-stack mini project that displays deduplicated dishes based on ingredient and flavor similarity. It combines a Python Flask backend with a modern React frontend. Each user sees a unique, paginated list of 25 clustered dishes based on their user ID.

---

## Features

- Ingredient + flavor-based dish deduplication
- Flask API with pagination logic
- React frontend with clean UI
- User-personalized results
- 5 pages × 5 dishes per page (total 25 dishes)

---

## Project Structure

```
Bhogi Coding Challenge/
├── DataScience/
│ ├── data.csv
│ ├── selected_dishes.csv # Final 25 deduplicated dishes
├── SolutionDesign/
│ ├── api.py # Flask API exposing dishes by userId & page
│ ├── deduplicate_dishes.py # Runs similarity + generates final dishes
│ ├── deduplicate_logic.py # Logic for similarity and clustering
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

##  Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/Vineethjutur/Bhogi-Coding-Challenege.git
cd Bhogi-Coding-Challenege
```
### 2. Backend – Flask API
```
cd SolutionDesign
python3 -m venv venv
source venv/bin/activate        # Use venv\Scripts\activate on Windows
pip install flask flask-cors pandas scikit-learn
python api.py
```
 
API will be running at: http://127.0.0.1:5003

Sample Endpoint: http://127.0.0.1:5003/dishes?userId=123&page=0

### 3. Frontend – React App
```
cd dish_viewer
npm install
npm start
```
Frontend will run at: http://localhost:3000

### How to Use
```
1. Enter a User ID (any integer)
2. Click Fetch Dishes
3. Navigate across 5 pages to view 25 deduplicated dishes
4. The output is consistent per userId (deterministic shuffle)
```
