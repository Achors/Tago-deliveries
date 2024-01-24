import PropTypes from 'prop-types';

const CartPage = ({ cart }) => {
  return (
    <div>
      <h2>Cart</h2>
      {cart.map((product) => (
        <div key={product.id}>
          <h3>{product.name}</h3>
          <p>Store: {product.store}</p>
          <p>Price: ${product.price}</p>
        </div>
      ))}
    </div>
  );
};


CartPage.propTypes = {
  cart: PropTypes.arrayOf(
    PropTypes.shape({
      id: PropTypes.number.isRequired,
      name: PropTypes.string.isRequired,
      store: PropTypes.string.isRequired,
      price: PropTypes.number.isRequired,
    })
  ).isRequired,
};

export default CartPage;
