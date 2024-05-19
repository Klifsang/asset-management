import React, { useEffect, useState } from "react";
import HttpClient from "../HttpClient";

const MyAssets = () => {
    const [assets, setAssets] = useState([]);

    useEffect(() => {
      async function getAssets() {
        const response = await HttpClient.get("api/assets/get");
        console.log(response.data);
        setAssets(response.data);
      }
      getAssets();
    }, []);
  
    return (
      <div className="container h-full overflow-auto">

      <button className="border border-solid mb-3 bg-teal-500 text-white font-bold uppercase text-xs outline-none focus:outline-none ease-linear transition-all duration-150">
        My Assets
      </button>
        <div className="grid grid-cols-4 gap-4">
        {assets.map((asset) => (
          <div className="col-span-1 ">
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
              <button>Report</button>
            </div>
          </div>
        ))}
      </div>
      </div>
    );
}

export default MyAssets