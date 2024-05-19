import { BrowserRouter as Router, Route, Routes, Link, Navigate } from "react-router-dom";
import UsersContent from "./UsersContent";
import MyAssets from "./MyAssets";
import AvailableAssets from "./AvailableAssets";
import Requests from "./Requests";
import NotificationContent from "./NotificationContent";
import LogoutContent from "./LogoutContent";
import ProfileContent from "./ProfileContent";
import MyRequests from "./MyRequests";

const navItems = [
  { id: "dashboard", label: "Dashboard", path: "/dashboard", component: AvailableAssets },
  { id: "users", label: "Users", path: "/users", component: UsersContent },
  { id: "myAssets", label: "My Assets", path: "/my-assets", component: MyAssets },
  { id: "requests", label: "All Requests", path: "/requests", component: Requests },
  { id: "myRequests", label: "My Requests", path: "/my-requests", component: MyRequests },
  { id: "profile", label: "My Profile", path: "/profile/:id", component: ProfileContent },
  { id: "notifications", label: "Notification", path: "/notification", component: NotificationContent },
  { id: "logout", label: "Logout", path: "/logout", component: LogoutContent },
];

export default function AdminDashboard({ setIsLoggedIn }) {
  return (
    <Router>
      <div className="flex h-screen w-screen ">
        <div className="sidebar w-1/6 bg-gray-200 text-center">
          <div className="brand-logo h-16 bg-gray-400"></div>
          <ul className="nav-items ml-10 text-left">
            {navItems.map((item) => (
              <li key={item.id} className="nav-item">
                <Link 
                  to={item.id === "profile" ? `/profile/1` : item.path} 
                  className="nav-link"
                >
                  {item.label}
                </Link>
              </li>
            ))}
          </ul>
        </div>
        <div className="content-area flex-1">
          <Routes>
            {navItems.map((item) => (
              <Route key={item.id} path={item.path} element={<item.component />} />
            ))}
            <Route path="*" element={<Navigate to="/" />} />
          </Routes>
        </div>
      </div>
    </Router>
  );
}
