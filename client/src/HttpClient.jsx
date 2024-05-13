// httpClient.jsx
import axios from "axios";

const HttpClient = axios.create({
    withCredentials: true,
    baseURL: "http://127.0.0.1:5000" // Set base URL for all requests
});

export default HttpClient;
