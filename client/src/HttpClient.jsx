// httpClient.jsx
import axios from "axios";
const HttpClient = axios.create({
    withCredentials: true
});


export default HttpClient;
