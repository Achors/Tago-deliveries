import { useState } from 'react';
import PropTypes from 'prop-types';

const Login = ({ onSwitchToSignUp }) => {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');

  const handleLogin = (e) => {
    e.preventDefault();
    console.log('Login clicked');
    // login logic 
  };

  return (
    <div className="log-container">
      <h1>Login</h1>
      <form onSubmit={handleLogin}>
        <label htmlFor="username">Username:</label>
        <input
          type="text"
          id="username"
          value={username}
          onChange={(e) => setUsername(e.target.value)}
          required
        />
        <label htmlFor="password">Password:</label>
        <input
          type="password"
          id="password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          required
        />
        <button type="submit">Login</button>
        <button type="button" onClick={onSwitchToSignUp}>Sign Up</button>
      </form>
    </div>
  );
};

Login.propTypes = {
  onSwitchToSignUp: PropTypes.func.isRequired,
};

export default Login;
