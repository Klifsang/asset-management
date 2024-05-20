import React from 'react';
import { Empty } from 'antd';
const EmptyList = ({message}) => (
  <Empty
    image="https://gw.alipayobjects.com/zos/antfincdn/ZHrcdLPrvN/empty.svg"
    imageStyle={{
      height: 60,
    }}
    description={
      <span>
        {message}
      </span>
    }
  >
  </Empty>
);
export default EmptyList;