import React, { useState } from 'react';
import axios from 'axios';
import './App.css';

function App() {
  const [userId, setUserId] = useState('');
  const [dishes, setDishes] = useState([]);
  const [page, setPage] = useState(0);

  const fetchDishes = async (uid, pg) => {
    try {
      const response = await axios.get('http://localhost:5003/dishes', {
        params: { userId: uid, page: pg }
      });
      setDishes(response.data.dishes);
    } catch (error) {
      console.error("Error fetching dishes:", error);
    }
  };

  const handleFetch = () => {
    if (userId) {
      setPage(0);
      fetchDishes(userId, 0);
    }
  };

  const handleNext = () => {
    if (page < 4) {
      const nextPage = page + 1;
      setPage(nextPage);
      fetchDishes(userId, nextPage);
    }
  };

  const handlePrev = () => {
    if (page > 0) {
      const prevPage = page - 1;
      setPage(prevPage);
      fetchDishes(userId, prevPage);
    }
  };

  return (
    <div className="App">
      <h1 className="title">Bhogi Dish Viewer</h1>
      <p className="quote">"A dish is a story – let’s discover yours."</p>

      <div className="controls">
        <input
          type="number"
          placeholder="Enter User ID"
          value={userId}
          onChange={(e) => setUserId(e.target.value)}
        />
        <button onClick={handleFetch}>Fetch Dishes</button>
      </div>

      {dishes.length > 0 && (
        <>
          <h2 className="page-label">Page: {page + 1}</h2>
          <table className="dish-table">
            <thead>
              <tr>
                <th>S.No</th>
                <th>Dish Name</th>
              </tr>
            </thead>
            <tbody>
              {dishes.map((dish, index) => (
                <tr key={index}>
                  <td>{page * 5 + index + 1}</td>
                  <td>{dish}</td>
                </tr>
              ))}
            </tbody>
          </table>

          <div className="pagination">
            <button onClick={handlePrev} disabled={page === 0}>Prev</button>
            <button onClick={handleNext} disabled={page === 4}>Next</button>
          </div>
        </>
      )}
    </div>
  );
}

export default App;
