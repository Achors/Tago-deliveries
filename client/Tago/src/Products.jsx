import { useState } from 'react';

const ExplorePage = ({ addToCart }) => {
  const [products, setProducts] = useState([
    { id: 1, name: 'Product 1', store: 'Store A', price: 20 },
    { id: 2, name: 'Product 2', store: 'Store B', price: 25 },
    // Add more products as needed
  ]);

  const handleOrder = (product) => {
    addToCart(product);
    setProducts((prevProducts) => prevProducts.filter((p) => p.id !== product.id));
  };

  return (
    <div>
      <h2>Explore Products</h2>
      {products.map((product) => (
        <div key={product.id}>
          <h3>{product.name}</h3>
          <p>Store: {product.store}</p>
          <p>Price: ${product.price}</p>
          <button onClick={() => handleOrder(product)}>Order</button>
        </div>
      ))}
    </div>
  );
};

export default ExplorePage;
