import React, { useEffect, useState } from "react";
import HttpClient from "../HttpClient";

import { Button, Modal } from "antd";
const AddSpecialRequest = () => {
  const [isModalOpen, setIsModalOpen] = useState(false);

  const [assetname, setAssetName] = useState("");
  const [description, setDescription] = useState("");
  const [quantity, setQuantity] = useState("");
  const [condition, setCondition] = useState("");
  const submitAsset = async () => {
    const response = await HttpClient.post("api/assets/add", {
      assetname: assetname,
      description: description,
      quantity: quantity,
      condition: condition,
    }).then((res) => {
      console.log(res);
    });
  };
  const showModal = () => {
    setIsModalOpen(true);
  };
  const handleOk = () => {
    submitAsset();
    setIsModalOpen(false);
  };
  const handleCancel = () => {
    setIsModalOpen(false);
  };
  return (
    <>
      <Button
        type="primary"
        onClick={showModal}
        className="max-w-48 text-teal-500 bg-transparent border border-solid border-teal-500 hover:bg-teal-500 hover:text-white active:bg-teal-600 font-bold text-xs rounded-full outline-none focus:outline-none ease-linear transition-all duration-150"
      >
        Add Special Request
      </Button>

      <Modal
        title="Add Asset"
        open={isModalOpen}
        okText="Submit Asset"
        cancelText="Cancel"
        closable={false}
        onOk={handleOk}
        onCancel={handleCancel}
      >
        <div className="container text-center">
          <div className="inputs">
            <label htmlFor="assetname">Asset Name</label>
            <div>
              <input
                id="assetname"
                name="assetname"
                type="text"
                onChange={(e) => setAssetName(e.target.value)}
                required
              />
            </div>
          </div>
          <div className="inputs">
            <label htmlFor="description">Description</label>
            <div>
              <input
                id="description"
                name="description"
                type="text"
                onChange={(e) => setDescription(e.target.value)}
                required
              />
            </div>
          </div>
          <div className="inputs">
            <label htmlFor="condition">Condition</label>
            <div>
              <input
                id="condition"
                name="condition"
                type="text"
                onChange={(e) => setCondition(e.target.value)}
                required
              />
            </div>
          </div>
          <div className="inputs">
            <label htmlFor="quantity">Quantity</label>
            <div>
              <input
                id="quantity"
                name="quantity"
                type="text"
                onChange={(e) => setQuantity(e.target.value)}
                required
              />
            </div>
          </div>
        </div>
      </Modal>
    </>
  );
};

const Requests = () => {
  const [requests, setRequests] = useState([]);

 const getRequests = async () => {
    const response = await HttpClient.get("api/requests/get");
    setRequests(response.data);
  }

  useEffect(() => {
    getRequests();
  }, []);


  const approve = async (id) => {
    const response = await HttpClient.patch("api/requests/update", {
      id: id,
      status: "Declined",
    });
    getRequests();
  };
  return (
    <div className="h-full overflow-auto -my-2 py-2 overflow-x-auto sm:-mx-6 sm:px-6 lg:-mx-8 pr-10 lg:px-8">
      <AddSpecialRequest />

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
                    onClick={() => approve(request.id)}
                    className="text-teal-500 bg-transparent border border-solid border-teal-500 hover:bg-teal-500 hover:text-white active:bg-teal-600 font-bold uppercase text-xs rounded-full outline-none focus:outline-none ease-linear transition-all duration-150"
                    type="button"
                  >
                    Approve
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

export default Requests;
