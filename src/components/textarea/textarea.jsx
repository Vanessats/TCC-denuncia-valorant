import React from "react";

import "./textarea.scss";

function TextArea(props) {
  return (
    <div className="customInput">
      <textarea
        id="spent"
        placeholder={props.placeholder}
        rows="5"
        cols="50"
        onChange={(e) => props.onChange(e)}
        value={props.value}
        {...props}
      />
    </div>
  );
}

export default TextArea;
