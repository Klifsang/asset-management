import { useState } from "react"
import HttpClient from "../HttpClient";


export default function Login({ toggleSignUp,setIsLoggedIn }){
    const[username, setUserName] =useState('')
    const[password, setPassword] =useState('')
    const handleLogin = async () => {
        try {
            const response = await HttpClient.post('http://127.0.0.1:5000/user/login', {
                username: username,
                password: password,
            });
            console.log(response.data);
            if (response.data.id) { 
                setIsLoggedIn(true); // Update the logged-in state
            } else { setIsLoggedIn(false); } return
        } catch (error) {
            console.error(error);
        }
    };
    return(
        <>
        <div>
            <label>Username</label>
            <input type="text" onChange={(e)=>setUserName(e.target.value)}/><br />
            <label>Password</label>
            <input type="password" onChange={(e)=>setPassword(e.target.value)}/><br />
            <button onClick={handleLogin}>Login</button>
        </div>
        <p>Don't have an account? <button onClick={toggleSignUp}>Sign Up</button></p>
        </>
    )
}