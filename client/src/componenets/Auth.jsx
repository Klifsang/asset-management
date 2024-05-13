import React, { useState } from 'react';

const AuthForm = () => {
  const [isLogin, setIsLogin] = useState(true);

  const toggleForm = () => {
    setIsLogin(prevState => !prevState);
  };

  return (
    <div>
      {isLogin ? (
        <LoginForm toggleForm={toggleForm} />
      ) : (
        <SignupForm toggleForm={toggleForm} />
      )}
    </div>
  );
};

const LoginForm = ({ toggleForm }) => {
  return (
    <div>
      <h2>Login Form</h2>
      <button onClick={toggleForm}>Switch to Signup</button>
      {/* Add your login form elements here */}
    </div>
  );
};

const SignupForm = ({ toggleForm }) => {
  return (
    <div>
      <h2>Signup Form</h2>
      <button onClick={toggleForm}>Switch to Login</button>
      {/* Add your signup form elements here */}
    </div>
  );
};

export default AuthForm;
