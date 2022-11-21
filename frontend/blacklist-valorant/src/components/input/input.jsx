import React from "react";

import "./input.scss";

function Input(props) {
  return (
    <div className="customInput">
      <input
        id="spent"
        placeholder={props.placeholder}
        mask={props.mask}
        onChange={(e) => props.onChange(e)}
        value={props.value}
        {...props}
      />
    </div>
  );
}

export default Input;
