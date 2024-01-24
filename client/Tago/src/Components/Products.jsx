import { useState } from 'react';
import PropTypes from 'prop-types';
// import App from '../App';
import '../App.css'

const ExplorePage = ({ addToCart }) => {
  const [products, setProducts] = useState([
    { id: 1, name: 'Product 1', store: 'Store A', price: 20 },
    { id: 2, name: 'Product 2', store: 'Store B', price: 25 },
  ]);

  const handleOrder = (product) => {
    addToCart(product);
    setProducts((prevProducts) => prevProducts.filter((p) => p.id !== product.id));
  };

  return (
    <div id='explore-pg'>
      <h2>Explore Products</h2>
      {products.map((product) => (
        <div id='cards' key={product.id}>
          <h3>{product.name}</h3>
          <p>Store: {product.store}</p>
          <p>Price: ${product.price}</p>
          <button id="order-btn" onClick={() => handleOrder(product)}>Order</button>
        </div>
      ))}
    </div>
  );
};

ExplorePage.propTypes = {
  addToCart: PropTypes.func.isRequired,
};

export default ExplorePage;
