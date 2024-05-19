import React, { useEffect, useState } from "react";
import HttpClient from "../HttpClient";

const SpecialRequest = () => {
  return (
    <div className="flex justify-center items-center w-full bg-gray-100">
      <div className="container w-auto text-center">
        <div className="brand-logo"></div>
        <div className="brand-title text-center">Special request</div>
        <div className="inputs">
          <label htmlFor="email">Asset Name</label>
          <div>
            <input
              id="username"
              name="username"
              type="text"
              onChange={(e) => setUserName(e.target.value)}
              required
            />
          </div>
        </div>
        <div className="inputs">
          <label htmlFor="authcode">Aythorization Code</label>
          <div>
            <input
              id="authcode"
              name="authcode"
              type="text"
              onChange={(e) => setAuthcode(e.target.value)}
              required
            />
          </div>
        </div>

        <div className="inputs">
          <label htmlFor="password">Password</label>
          <div>
            <input
              id="password"
              name="password"
              type="password"
              onChange={(e) => setPassword(e.target.value)}
              required
            />
          </div>
        </div>

        <div>
          <button type="submit">Submit Request</button>
        </div>
      </div>
    </div>
  );
};

const MyRequests = () => {
  const [requests, setRequests] = useState([]);

  useEffect(() => {
    async function getRequests() {
      const response = await HttpClient.get("api/myrequests/get");
      console.log(response.data);
      setRequests(response.data);
    }
    getRequests();
  }, []);
  const deleteRequest = async (id) => {
    const response = await HttpClient.delete(`api/requests/delete/${id}`);
    console.log(response.data);
  };
  return (
    <div className="-my-2 py-2 overflow-x-auto sm:-mx-6 sm:px-6 lg:-mx-8 pr-10 lg:px-8 h-full overflow-auto">
      <button
        className="max-w-24 text-teal-500 bg-transparent border border-solid border-teal-500 hover:bg-teal-500 hover:text-white active:bg-teal-600 font-bold text-xs rounded-full outline-none focus:outline-none ease-linear transition-all duration-150"
        type="button"
      >
        Add Special Request
      </button>

      <button className="border border-solid bg-teal-500 text-white font-bold uppercase text-xs outline-none focus:outline-none ease-linear transition-all duration-150">
        Requests
      </button>

      <div className="align-middle inline-block min-w-full shadow overflow-hidden bg-white shadow-dashboard px-8 pt-3 rounded-bl-lg rounded-br-lg">
        <table className="min-w-full">
          <thead>
            <tr>
              <th className="px-6 py-3 border-b-2 border-gray-300 text-left leading-4 text-blue-500 tracking-wider">
                ID
              </th>
              <th className="px-6 py-3 border-b-2 border-gray-300 text-left text-sm leading-4 text-blue-500 tracking-wider">
                Asset Name
              </th>
              <th className="px-6 py-3 border-b-2 border-gray-300 text-left text-sm leading-4 text-blue-500 tracking-wider">
                Priority
              </th>
              <th className="px-6 py-3 border-b-2 border-gray-300 text-left text-sm leading-4 text-blue-500 tracking-wider">
                Status
              </th>
              <th className="px-6 py-3 border-b-2 border-gray-300 text-left text-sm leading-4 text-blue-500 tracking-wider">
                Comments
              </th>
              <th className="px-6 py-3 border-b-2 border-gray-300 text-left text-sm leading-4 text-blue-500 tracking-wider">
                Created At
              </th>
              <th className="px-6 py-3 border-b-2 border-gray-300"></th>
            </tr>
          </thead>
          <tbody className="bg-white">
            {requests.map((request) => (
              <tr key={request.id}>
                <td className="px-6 py-4 whitespace-no-wrap border-b border-gray-500">
                  <div className="flex items-center">
                    <div className="text-sm leading-5 text-gray-800">
                      #{request.id}
                    </div>
                  </div>
                </td>
                <td className="px-6 py-4 whitespace-no-wrap border-b border-gray-500">
                  <div className="flex items-center">
                    <div className="w-10 h-10 flex-shrink-0 mr-2 sm:mr-3">
                      <img
                        className="rounded-full"
                        src="https://raw.githubusercontent.com/cruip/vuejs-admin-dashboard-template/main/src/images/user-36-05.jpg"
                        width="40"
                        height="40"
                        alt="Alex Shatov"
                      />
                    </div>
                    <div className="font-medium text-gray-800">
                      {request.assetname}
                    </div>
                  </div>
                </td>
                <td className="px-6 py-4 whitespace-no-wrap border-b text-blue-900 border-gray-500 text-sm leading-5">
                  {request.priority}
                </td>
                <td className="px-6 py-4 whitespace-no-wrap border-b text-blue-900 border-gray-500 text-sm leading-5">
                  {request.status}
                </td>
                <td className="px-6 py-4 whitespace-no-wrap border-b text-blue-900 border-gray-500 text-sm leading-5">
                  <span className="relative inline-block px-3 py-1 font-semibold text-green-900 leading-tight">
                    <span
                      aria-hidden
                      className="absolute inset-0 opacity-50 rounded-full"
                    ></span>
                    <span className="relative text-xs">{request.comments}</span>
                  </span>
                </td>
                <td className="px-6 py-4 whitespace-no-wrap border-b border-gray-500 text-blue-900 text-sm leading-5">
                  September 12
                </td>
                <td className="px-6 py-4 whitespace-no-wrap text-right border-b border-gray-500 text-sm leading-5">
                  <button
                    onClick={() => deleteRequest(request.id)}
                    className="text-teal-500 bg-transparent border border-solid border-teal-500 hover:bg-teal-500 hover:text-white active:bg-teal-600 font-bold uppercase text-xs rounded-full outline-none focus:outline-none ease-linear transition-all duration-150"
                    type="button"
                  >
                    Delete
                  </button>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
};

export default MyRequests;
