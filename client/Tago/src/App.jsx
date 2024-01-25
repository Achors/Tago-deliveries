import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';
import { useState } from 'react';
import ExplorePage from './Components/Products';
import CartPage from './Components/cartPage';
import Login from './Components/Login';

function App() {
  const [cart, setCart] = useState([]);

  const addToCart = (product) => {
    setCart((prevCart) => [...prevCart, product]);
  };

  return (
    <Router>
      <div id="home">
        <div></div>
        <div id='nav'>
          <div>
            <img src='' alt='logo' />
          </div>
          <div>
            <span className="logo">TAGO - Del</span>
          </div>
          <div className='nav-list'>
            <div id='log-list'>
              <Link to="/login">Login</Link>
            </div>
            <div>
              <Link to="/">Explore</Link>
            </div>
            <div>
              <Link to="/cart">Cart ({cart.length})</Link>
            </div>
          </div>
        </div>
        <hr />
        <div></div>

        <Routes>
          <Route path="/" element={<ExplorePage addToCart={addToCart} />} />
          <Route path="/cart" element={<CartPage cart={cart} />} />
          <Route path="/login" element={<Login />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
