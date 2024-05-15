import React, { useEffect } from "react";
import HttpClient from "../HttpClient";

const LogoutContent = ({setIsLoggedIn}) => {
  useEffect(() => {
    const logOut = async () => {
      try {
        const response = await HttpClient.post("http://127.0.0.1:5000/logout", {
          withCredentials: true,
        });
        console.log(response); // Assuming the response contains a 'data' field
        setIsLoggedIn(false);
      } catch (error) {
        console.error(error);
      }
    };
    logOut();
  }, []);

  return <div>Logging out</div>;
};

export default LogoutContent;
