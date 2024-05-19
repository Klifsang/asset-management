import { useState } from "react";
import HttpClient from "../HttpClient";

export default function Login({ toggleSignUp, setIsLoggedIn }) {
  const [username, setUserName] = useState("");
  const [password, setPassword] = useState("");
  const [authcode, setAuthcode] = useState("");
  const handleLogin = async (e) => {
    e.preventDefault()
    try {
      const response = await HttpClient.post(
        "api/user/login",
        {
          username: username,
          authcode: authcode,
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
      <div className="container h-full overflow-auto">
        <div className="brand-logo"></div>
        <div className="brand-title text-center">Asset Ace</div>
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
        <div className="inputs">
          <label htmlFor="authcode">Aythorization Code</label>
          <div>
            <input
              id="authcode"
              name="authcode"
              type="text"
              onChange={(e) => setAuthcode(e.target.value)}
              required
            />
          </div>
        </div>

          <div className="inputs">
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
