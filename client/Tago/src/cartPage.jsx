

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

export default CartPage;
