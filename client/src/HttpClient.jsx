// httpClient.jsx
import axios from "axios";
const HttpClient = axios.create({
    withCredentials: true,
    baseURL: "https://asset-management-production.up.railway.app"
});


export default HttpClient;
