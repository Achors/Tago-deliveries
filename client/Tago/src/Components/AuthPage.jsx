import { useState } from 'react';
import Login from './Login';
import SignupForm from './SignupForm'; 

const AuthPage = () => {
  const [isLoginView, setLoginView] = useState(true);

  const switchView = () => {
    setLoginView(!isLoginView);
  };

  return (
    <div>
      {isLoginView ? (
        <Login onSwitchToSignUp={switchView} />
      ) : (
        <SignupForm />
      )}

      <p>
        {isLoginView
          ? "Don't have an account? Click here to"
          : 'Already have an account? Click here to'}
        <span onClick={switchView}>
          {isLoginView ? ' Sign Up' : ' Log In'}
        </span>
      </p>
    </div>
  );
};

export default AuthPage;
