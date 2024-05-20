import React, { useEffect, useState } from "react";
import HttpClient from "../HttpClient";
import { useParams } from "react-router-dom";

const ProfileContent = () => {
  let { id } = useParams();
  id = id || '1'; // Default to '1' if id is not provided

  console.log(id);
  
  const [profile, setProfile] = useState({
    username: "",
    fullname: "",
    address: "",
    email: "",
    phonenumber: "",
    role: "",
    status: "",
    department: "",
  });

  const [isDisabled, setIsDisabled] = useState(true);

  useEffect(() => {
    async function getAssets() {
      const response = await HttpClient.get("api/staff/getstaff", {
        id: id,
      });
      setProfile(response.data);
    }
    getAssets();
  }, []);

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setProfile((prevProfile) => ({
      ...prevProfile,
      [name]: value,
    }));
  };

  const handleToggleDisable = () => {
    setIsDisabled((prevState) => !prevState);
  };

  const { username, fullname, address, email, phonenumber, role, status, department } = profile;

  return (
    <div className="flex justify-center items-center h-full overflow-auto w-full bg-gray-100">
      <div className="container w-auto text-center">
        <div className="brand-logo"></div>
        <div className="brand-title text-center">User Details</div>
        <div className="grid grid-cols-2 gap-2">
          <div className="col-span-1">
            <label>Full Name</label>
            <input
              disabled={isDisabled}
              type="text"
              name="fullname"
              value={fullname}
              onChange={handleInputChange}
              required
            />
            <label>User Name</label>
            <input
              disabled={isDisabled}
              type="text"
              name="username"
              value={username}
              onChange={handleInputChange}
              required
            />
            <label>Email</label>
            <input
              disabled={isDisabled}
              type="email"
              name="email"
              value={email}
              onChange={handleInputChange}
              required
            />
            <label>Phone Number</label>
            <input
              disabled={isDisabled}
              type="text"
              name="phonenumber"
              value={phonenumber}
              onChange={handleInputChange}
              required
            />
          </div>

          <div className="col-span-1">
            <label>Department</label>
            <input
              disabled={isDisabled}
              type="text"
              name="department"
              value={department}
              onChange={handleInputChange}
              required
            />
            <label>Address</label>
            <input
              disabled={isDisabled}
              type="text"
              name="address"
              value={address}
              onChange={handleInputChange}
              required
            />
            <label>Role</label>
            <input
              disabled={isDisabled}
              type="text"
              name="role"
              value={role}
              onChange={handleInputChange}
              required
            />
            <label>Status</label>
            <input
              disabled
              type="text"
              name="status"
              value={status}
              onChange={handleInputChange}
            />
          </div>
        </div>
        <button onClick={handleToggleDisable}>Edit account</button>
      </div>
    </div>
  );
};

export default ProfileContent;
