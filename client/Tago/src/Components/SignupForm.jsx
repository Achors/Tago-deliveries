import { useState } from 'react';
import axios from 'axios';
import PropTypes from 'prop-types';
import '../App.css';

const SignupForm = ({ onBackToLogin }) => {
  const [formData, setFormData] = useState({
    username: '',
    email: '',
    password: '',
    city: ''
  });

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      const response = await axios.post('http://127.0.0.1:5000/api/register', formData);
      console.log('User registered:', response.data);
    } catch (error) {
      console.error('Registration failed:', error.response.data);
    }
  };

  return (
    <div className="signup-form-container">
      <h2>Sign Up</h2>
      <form onSubmit={handleSubmit} className="signup-form">
      <label htmlFor="username">Username:</label>
        <input type="text" id="username" name="username" value={formData.username} onChange={handleChange} required />

        <label htmlFor="email">Email:</label>
        <input type="email" id="email" name="email" value={formData.email} onChange={handleChange} required />

        <label htmlFor="password">Password:</label>
        <input type="password" id="password" name="password" value={formData.password} onChange={handleChange} required />

        <label htmlFor="city">City:</label>
        <input type="text" id="city" name="city" value={formData.city} onChange={handleChange} />

        <button type="submit">Sign Up</button>
        <button type="button" onClick={onBackToLogin}>Back to Login</button>
      </form>
    </div>
  );
};

SignupForm.propTypes = {
  onBackToLogin: PropTypes.func.isRequired,
};

export default SignupForm;
