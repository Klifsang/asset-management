import React, { useEffect, useState } from "react";
import HttpClient from "../HttpClient";

import { Button, Modal } from "antd";
const AddAsset = () => {
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
        className="max-w-24 text-teal-500 bg-transparent border border-solid border-teal-500 hover:bg-teal-500 hover:text-white active:bg-teal-600 font-bold text-xs rounded-full outline-none focus:outline-none ease-linear transition-all duration-150"
      >
        Add Asset
      </Button>

      <Modal
        title="Add Asset"
        open={isModalOpen}
        onOk={handleOk}
        onCancel={handleCancel}
      >
        <div className="modalcontainer text-center">
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

const AvailableAssets = () => {
  const [assets, setAssets] = useState([]);

  useEffect(() => {
    async function getAssets() {
      const response = await HttpClient.get("api/assets/get");
      console.log(response.data);
      setAssets(response.data);
    }
    getAssets();
  }, []);

  const requestAsset = async (id) => {
    const response = await HttpClient.post("api/requests/add", {
      assetId: id,
      userId: 1,
      comment: "urgent request",
      quantity: 1,
    });
    console.log(response.data);
  };

  return (
    <div className="container h-full overflow-auto">
      <AddAsset />

      <button className="border border-solid mb-3 bg-teal-500 text-white font-bold uppercase text-xs outline-none focus:outline-none ease-linear transition-all duration-150">
        Assets
      </button>
      <div className="grid grid-cols-4 gap-4">
        {assets.map((asset) => (
          <div className="col-span-1 " key={asset.id}>
            <div className="container">
              <div className="grid grid-cols-2">
                <div className="row-span-4 col-span-1">
                  <img
                    src="https://raw.githubusercontent.com/cruip/vuejs-admin-dashboard-template/main/src/images/user-36-05.jpg"
                    width="95%"
                    height="95%"
                    alt="Alex Shatov"
                  />
                </div>
                <div className="col-span-1 font-medium text-gray-800">
                  {asset.assetname}
                </div>
                <div className="col-span-1 font-medium text-gray-800">
                  {asset.availability}
                </div>
                <div className="col-span-1 font-medium text-gray-800">
                  {asset.condition}
                </div>
                <div className="col-span-1 font-medium text-gray-800">
                  {asset.description}
                </div>
              </div>
              <button onClick={() => requestAsset(asset.id)}>Request</button>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};

export default AvailableAssets;
