import { useState } from "react";
import HttpClient from "../HttpClient";

export default function Login({ toggleSignUp, setIsLoggedIn }) {
  const [username, setUserName] = useState("");
  const [password, setPassword] = useState("");
  const handleLogin = async (e) => {
    e.preventDefault()
    try {
      const response = await HttpClient.post(
        "http://127.0.0.1:5000/user/login",
        {
          username: username,
          password: password,
        }
      );
      console.log(response.data);
      if (response.data.id) {
        setIsLoggedIn(true); // Update the logged-in state
      } else {
        setIsLoggedIn(false);
      }
      return;
    } catch (error) {
      console.error(error);
    }
  };
  return (
      <div className="container">
        <div className="brand-logo"></div>
        <div className="brand-title">Asset Ace</div>
        <div className="inputs">
          <label htmlFor="email">User Name</label>
          <div>
            <input
              id="username"
              name="username"
              type="text"
              onChange={(e) => setUserName(e.target.value)}
              required
            />
          </div>
        </div>

        <div>
          <div>
            <label htmlFor="password">Password</label>
            <div>
              <input
                id="password"
                name="password"
                type="password"
                onChange={(e) => setPassword(e.target.value)}
                required
              />
            </div>
          </div>
        </div>

        <div>
          <button type="submit" onClick={handleLogin}>
            Sign in
          </button>
        </div>
        <p>
          Not a member?
          <a href="#" onClick={toggleSignUp}>
            Create an account
          </a>
        </p>
      </div>
  );
}
