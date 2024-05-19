import { useState } from "react";
import HttpClient from "../HttpClient";

export default function SignUp({ toggleSignUp }) {
  const [username, setUserName] = useState("");
  // const [fullname, setFullName] = useState("");
  const [address, setAddress] = useState("");
  const [email, setEmail] = useState("");
  const [phonenumber, setPhonenumber] = useState("");
  const [password, setPassword] = useState("");
  const [confirmPassword, setConfirmPassword] = useState("");
  const [department, setDepartment] = useState("");
  const [role, setRole] = useState("");

  const handleRegister = async (e) => {
    e.preventDefault();
    if (password !== confirmPassword) {
      alert("Passwords do not match");
      return;
    }
    try {
      const response = await HttpClient.post(
        "api/staff/register",
        {
          username: username,
          address: address,
          email: email,
          phonenumber: phonenumber,
          department: department,
          password: password,
          role: role
        }
      );
      console.log(response); // Assuming the response contains a 'data' field
    } catch (error) {
      console.error(error);
    }
  };

  return (
    <div className="container h-full overflow-auto">
      <div className="brand-logo"></div>
      <div className="brand-title text-center">Create an account</div>
      <form className="inputs" onSubmit={handleRegister}>
        <div className="grid grid-cols-2 gap-2">
          <div className="col-span-1 ">
            <label>Role</label>
            <input
              type="text"
              value={role}
              onChange={(e) => setRole(e.target.value)}
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
          </div>

          <div className="col-span-1 ">
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
          </div>
        </div>

        <button type="submit">Create account</button>
      </form>
      <p className="text-center">
        Already have an account?
        <a href="#" onClick={toggleSignUp}>
          Login
        </a>
      </p>
    </div>
  );
}
