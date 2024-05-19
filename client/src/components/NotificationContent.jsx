import React from "react";
import Celebrate from "./Celebrate";
import { Collapse } from "antd";
const text = `
  A dog is a type of domesticated animal.
  Known for its loyalty and faithfulness,
  it can be found as a welcome guest in many households across the world.
`;
const items = [
  {
    key: "1",
    label: "This is panel header 1",
    children: <Celebrate />,
  },
  {
    key: "2",
    label: "This is panel header 2",
    children: <p>{text}</p>,
  },
  {
    key: "3",
    label: "This is panel header 3",
    children: <p>{text}</p>,
  },
];
const Message = () => {
  const onChange = (key) => {
    console.log(key);
  };
  return (
    <Collapse items={items} onChange={onChange} />
  );
};

const NotificationContent = () => {
  return (
    <div className="h-full overflow-auto">
      <div>Request approved, time to celebrate</div>
      <Message/>
    </div>
  );
};

export default NotificationContent;
