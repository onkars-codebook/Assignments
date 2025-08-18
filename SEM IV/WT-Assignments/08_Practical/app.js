import './App.css';

import React, { useState } from 'react';
function ProductList({ products, addToCart }) {
  return (
    <div>
      <h2>Products</h2>
      <ul>
        {products.map((product) => (
          <li key={product.id}>
            {product.name} - Rs{product.price}
            <button onClick={() => addToCart(product)}>Add to Cart</button>
          </li>
        ))}
      </ul>
    </div>
  );
}

function Cart({ cartItems, removeFromCart }) {
  return (
    <div>
      <h2>Cart</h2>
      {cartItems.length === 0 ? (
        <p>Your cart is empty.</p>
      ) : (
        <ul>
          {cartItems.map((item, index) => (
            <li key={index}>
              {item.name} - Rs{item.price}
              <button onClick={() => removeFromCart(index)}>Remove</button>
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}

function Checkout({ cartItems, handleCheckout }) {
  return (
    <div>
      <h2>Checkout</h2>
      {cartItems.length === 0 ? (
        <p>Add some products to the cart before checkout.</p>
      ) : (
        <button onClick={handleCheckout}>Process Order</button>
      )}
    </div>
  );
}

function App() {
  const products = [
    { id: 1, name: 'T-Shirt', price: 450 },
    { id: 2, name: 'Jeans', price: 900 },
    { id: 3, name: 'Sneakers', price: 1000 }
  ];

  const [cartItems, setCartItems] = useState([]);

  const addToCart = (product) => {
    setCartItems([...cartItems, product]);
  };

  const removeFromCart = (indexToRemove) => {
    setCartItems(cartItems.filter((item, index) => index !== indexToRemove));
  };

  const handleCheckout = () => {
    alert('Order processed successfully!');
    setCartItems([]); // Clear the cart after checkout.
  };

  return (
    <div>
      <h1>Online Shopping</h1>
      <ProductList products={products} addToCart={addToCart} />
      <Cart cartItems={cartItems} removeFromCart={removeFromCart} />
      <Checkout cartItems={cartItems} handleCheckout={handleCheckout} />
    </div>
  );
}

export default App; 
