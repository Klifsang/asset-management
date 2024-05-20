// httpClient.jsx
import axios from "axios";
const HttpClient = axios.create({
    withCredentials: true,
    baseURL: "http://127.0.0.1:5000"
});

// HttpClient.interceptors.response.use(
//     response => response,
//     error => {
//         if (error.response.status === 401) {
//             console.log("not authenticated")
//             // window.location.replace("/login");
//         }
//         // Return the error so it can be handled further
//         return Promise.reject(error);
//     }
// );

export default HttpClient;
