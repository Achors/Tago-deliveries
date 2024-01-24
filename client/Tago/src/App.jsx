// import React, { useState } from 'react';
import { BrowserRouter as Router, Route, Link } from 'react-router-dom';
import { useState } from 'react';
import ExplorePage from './Products';
import CartPage from './cartPage';

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

        <Route exact path="/" render={() => <ExplorePage addToCart={addToCart} />} />
        <Route path="/cart" render={() => <CartPage cart={cart} />} />
      </div>
    </Router>
  );
}

export default App;
