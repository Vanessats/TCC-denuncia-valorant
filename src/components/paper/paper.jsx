import React from "react";

import "./paper.scss";

const Button = ({ children }) => {
  return (
    <div id="paper-container">
      <div className="paper">
        <div className="lines">
          <div className="text">{children}</div>
        </div>
        <div className="holes hole-top"></div>
        <div className="holes hole-middle"></div>
        <div className="holes hole-bottom"></div>
      </div>
    </div>
  );
};

export default Button;
