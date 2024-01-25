import { useEffect, useState } from 'react';
import PropTypes from 'prop-types';
import { fetchProducts } from '../Services/api';
import '../App.css';

const ExplorePage = ({ addToCart }) => {
  const [products, setProducts] = useState([]);

  useEffect(() => {
    fetchProducts()
      .then(response => {
        setProducts(response.data);
      })
      .catch(error => {
        console.error('Error fetching products:', error);
      });
  }, []);

  const handleOrder = (product) => {
    addToCart(product);
    setProducts((prevProducts) => prevProducts.filter((p) => p.id !== product.id));
  };

  return (
    <div id='explore-pg'>
      <div>
        <h2>Explore Products</h2>
      </div>
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
