// httpClient.jsx
import axios from "axios";
const HttpClient = axios.create({
    withCredentials: true,
    baseURL: "http://127.0.0.1:5000"
});


export default HttpClient;
