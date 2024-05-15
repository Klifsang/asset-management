import { useState } from "react";
import HttpClient from "../HttpClient";

export default function SignUp({ toggleSignUp }) {
  const [username, setUserName] = useState("");
  const [fullname, setFullName] = useState("");
  const [address, setAddress] = useState("");
  const [email, setEmail] = useState("");
  const [phonenumber, setPhonenumber] = useState("");
  const [password, setPassword] = useState("");
  const [confirmPassword, setConfirmPassword] = useState("");
  const [department, setDepartment] = useState("");

  const handleRegister = async (e) => {
    e.preventDefault();
    if (password !== confirmPassword) {
      alert("Passwords do not match");
      return;
    }
    try {
      const response = await HttpClient.post(
        "http://127.0.0.1:5000/user/register",
        {
          username: username,
          address: address,
          email: email,
          phonenumber: phonenumber,
          department: department,
          password: password,
        }
      );
      console.log(response); // Assuming the response contains a 'data' field
    } catch (error) {
      console.error(error);
    }
  };

  return (
    <div className="container">
      <div className="brand-logo"></div>
      <div className="brand-title">Create an account</div>
      <form className="inputs" onSubmit={handleRegister}>
        <label>Full Name</label>
        <input
          type="text"
          value={fullname}
          onChange={(e) => setFullName(e.target.value)}
          required
        />
        <label>User Name</label>
        <input
          type="text"
          value={username}
          onChange={(e) => setUserName(e.target.value)}
          required
        />
        <label>Email</label>
        <input
          type="email"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          required
        />
        <label>Phone Number</label>
        <input
          type="text"
          value={phonenumber}
          onChange={(e) => setPhonenumber(e.target.value)}
          required
        />
        <label>Department</label>
        <input
          type="text"
          value={department}
          onChange={(e) => setDepartment(e.target.value)}
          required
        />
        <label>Address</label>
        <input
          type="text"
          value={address}
          onChange={(e) => setAddress(e.target.value)}
          required
        />
        <label>Password</label>
        <input
          type="password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          required
        />
        <label>Confirm Password</label>
        <input
          type="password"
          value={confirmPassword}
          onChange={(e) => setConfirmPassword(e.target.value)}
          required
        />
        <button type="submit">Create account</button>
      </form>
      <p>
        Already have an account?
        <a href="#" onClick={toggleSignUp}>
          Login
        </a>
      </p>
    </div>
  );
}
