import { useState } from 'react';
import { useNavigate, Link } from 'react-router-dom';
import '../App.css';


const Login = () => {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const navigate = useNavigate();

  const login = () => {
    // authentication logic
    console.log('Username:', username);
    console.log('Password:', password);

    navigate('/Products');
  };

  return (
    <div className="login-container">
      <h1>Login</h1>
      <form onSubmit={login}>
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

        <Link to="/authpage/signup">
          <button type="button">Sign Up</button>
        </Link>
      </form>
    </div>
  );
};

export default Login;
