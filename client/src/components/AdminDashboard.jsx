import { useState } from "react";
import DashboardContent from "./DashboardContent"
import UsersContent from "./UsersContent"
import SettingsContent from "./SettingsContent"
import LogoutContent from "./LogoutContent";

const navItems = [
  { id: "dashboard", label: "Dashboard", component: DashboardContent },
  { id: "users", label: "Users", component: UsersContent },
  { id: "settings", label: "Settings", component: SettingsContent },
  { id: "logout", label: "Logout", component: LogoutContent },
];


export default function AdminDashboard({ setIsLoggedIn }) {
  const [selectedNavItem, setSelectedNavItem] = useState("dashboard");

  const handleNavItemClick = (item) => {
    setSelectedNavItem(item);
  };

  const ContentComponent = navItems.find((item) => item.id === selectedNavItem)
    ?.component;

    return (
      <div className="flex h-screen w-screen">
        <div className="sidebar w-1/6 bg-gray-200">
          <div className="brand-logo h-16 bg-gray-400"></div>
          <ul className="nav-items">
            {navItems.map((item) => (
              <li
                key={item.id}
                className={`nav-item ${selectedNavItem === item.id ? "active" : ""}`}
                onClick={() => handleNavItemClick(item.id)}
              >
                {item.label}
              </li>
            ))}
          </ul>
        </div>
        <div className="content-area flex-1">
          {ContentComponent && <ContentComponent />}
        </div>
      </div>
    );
}


