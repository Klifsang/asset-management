// App.jsx
import { useEffect, useState } from "react";
import "./App.css";
// import Home from "./components/Home";
import AdminDashboard from "./components/AdminDashboard";
import Login from "./components/Login";
import SignUp from './components/Signup'
import HttpClient from "./HttpClient";

function App() {
  const [loggedIn, setIsLoggedIn] = useState(false);
  const [showSignUp, setShowSignUp] = useState(false);
  useEffect(() => {
    async function checkUser() {
      const response = await HttpClient.post(
        "http://127.0.0.1:5000/checksession"
      );
      console.log(response.data.id); // Assuming the response contains a 'data' field
      if (response.data.id) {
        setIsLoggedIn(true);
      } else {
        setIsLoggedIn(false);
      }
    }
    checkUser();
  }, []);

    // Function to toggle between SignUp and Login
    const toggleSignUp = () => {
      setShowSignUp(!showSignUp);
    };
  
  return (
    <>
      {loggedIn ? (
        <AdminDashboard setIsLoggedIn={setIsLoggedIn}/>
      ) : (
        <>
          {showSignUp ? (
            <SignUp toggleSignUp={toggleSignUp} />
          ) : (
            <Login toggleSignUp={toggleSignUp} setIsLoggedIn={setIsLoggedIn}/>
          )}
        </>
      )}
    </>
  );
}

export default App;
