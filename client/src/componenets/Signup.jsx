import { useState } from "react";
import HttpClient from "../HttpClient";

export default function SignUp({toggleSignUp}){
    const[username, setUserName] = useState('')
    const[address, setAddress] = useState('')
    const[email, setEmail] =useState('')
    const[phonenumber, setPhonenumber] = useState('')
    const[password, setPassword] =useState('')
    const[department, setDepartment] = useState('')

    const handleRegister = async () => {
        try {
            const response = await HttpClient.post('http://127.0.0.1:5000/user/register', {
                username: username,
                address: address,
                email: email,
                phonenumber: phonenumber,
                department: department,
                password: password,
            });
            console.log(response); // Assuming the response contains a 'data' field
        } catch (error) {
            console.error(error);
        }
    };
    
    return(
        <>
        <h1>Sign Up</h1>
        <div>
            <label>Username</label>
            <input type="text" onChange={(e)=>setUserName(e.target.value)}/><br />
            <label>Address</label>
            <input type="text" onChange={(e)=>setAddress(e.target.value)}/><br />
            <label>Email</label>
            <input type="email" onChange={(e)=>setEmail(e.target.value)}/><br />
            <label>Phone</label>
            <input type="text" onChange={(e)=>setPhonenumber(e.target.value)}/><br />
            <label>Department</label>
            <input type="text" onChange={(e)=>setDepartment(e.target.value)}/><br />
            <label>Password</label>
            <input type="password" onChange={(e)=>setPassword(e.target.value)}/><br />
            <button onClick={handleRegister}>Register</button>
        </div>
        <p>Already have an account? <button onClick={toggleSignUp}>Login</button></p>
        </>
    )
}

// username = data.get('username')
// department = data.get('department')
// address = data.get('address')
// email = data.get('email')
// phonenumber = data.get('phonenumber')
// password = data.get('password')