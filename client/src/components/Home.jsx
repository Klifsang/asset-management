import HttpClient from "../HttpClient";

export default function Home({setIsLoggedIn}){
    const logOut = async () => {
        try {
            const response = await HttpClient.post('http://127.0.0.1:5000/logout',{
                withCredentials: true
              });
            console.log(response); // Assuming the response contains a 'data' field
            setIsLoggedIn(false)
        } catch (error) {
            console.error(error);
        }
    };
    return(
        <>
        <h1 className="text-3xl font-bold underline">Home Page</h1>
        <button onClick={logOut}>Log out</button>
        </>
    )
}