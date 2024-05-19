import React from "react";

const AddAsset = () => {
  const [assetname, setAssetname] = React.useState("");
  const [quantity, setQuantity] = React.useState(1);
  const [comments, setComments] = React.useState("")
  return (
    <div className="container text-center mr-10">
      <div className="brand-title">Add Asset</div>
      <div className="inputs">
        <label htmlFor="assetname">Asset Name</label>
        <div>
          <input
            id="assetname"
            name="assetname"
            type="text"
            onChange={(e) => setAssetname(e.target.value)}
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

      <div className="inputs">
        <label htmlFor="comments">Comments</label>
          <input
            id="comments"
            name="comments"
            type="comments"
            onChange={(e) => setComments(e.target.value)}
            required
          />
      </div>

      <div>
        <button type="submit">
          Add Asset
        </button>
      </div>
    </div>
  );
};

const DashboardContent = () => {
  return (
    <div class="grid grid-cols-3 gap-3 h-full overflow-auto">
      <div class="col-span-2">
        <h1>Dashboard</h1>
      </div>
      <div class="col-span-1">
        <AddAsset/>
      </div>
    </div>
  );
};

export default DashboardContent;
