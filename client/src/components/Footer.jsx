import React from "react";

const Footer = () => {
  return (
      <div className="frame">
        <a href="#" className="btn">
          <i className="fab fa-facebook-f" style={{ color: '#3b5998' }}></i>
        </a>
        <a href="#" className="btn">
          <i className="fab fa-twitter" style={{ color: '#00acee' }}></i>
        </a>
        <a href="#" className="btn">
          <i className="fab fa-dribbble" style={{ color: '#ea4c89' }}></i>
        </a>
        <a href="#" className="btn">
          <i className="fab fa-linkedin-in" style={{ color: '#0e76a8' }}></i>
        </a>
        <a href="#" className="btn">
          <i className="fab fa-get-pocket" style={{ color: '#ee4056' }}></i>
        </a>
        <a href="#" className="btn">
          <i className="far fa-envelope"></i>
        </a>
      </div>
  );
};

export default Footer;
