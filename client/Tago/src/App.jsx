import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';
import { useState } from 'react';
import ExplorePage from './Components/Products';
import CartPage from './Components/cartPage';

function App() {
  const [cart, setCart] = useState([]);

  const addToCart = (product) => {
    setCart((prevCart) => [...prevCart, product]);
  };

  return (
    <Router>
      <div>
        <nav>
          <ul>
            <li>
              <Link to="/">Explore</Link>
            </li>
            <li>
              <Link to="/cart">Cart ({cart.length})</Link>
            </li>
          </ul>
        </nav>

        <hr />

        
        <Routes>
          <Route path="/" element={<ExplorePage addToCart={addToCart} />} />
          <Route path="/cart" element={<CartPage cart={cart} />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
