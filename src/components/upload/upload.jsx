import React from "react";

import "./upload.scss";
import Button from "../button";

class Upload extends React.Component {
  constructor(props) {
    super(props);
    this.handleAddImage = this.handleAddImage.bind(this);
    this.handleUploadImage = this.handleUploadImage.bind(this);
    this.handleDragOver = this.handleDragOver.bind(this);
    this.handleDragEnter = this.handleDragEnter.bind(this);
    this.handleDragLeave = this.handleDragLeave.bind(this);
    this.handleDrop = this.handleDrop.bind(this);
    this.handleCancelUpload = this.handleCancelUpload.bind(this);
    this.state = {
      file: null,
      dragOver: false,
      errorNoficication: null,
    };
  }

  handleDragEnter(e) {
    e.preventDefault();
  }
  handleDragOver(e) {
    e.preventDefault();
    if (!this.state.dragOver) {
      this.setState({
        dragOver: true,
      });
    }
  }
  handleDragLeave(e) {
    e.preventDefault();
    this.setState({
      dragOver: false,
    });
  }
  handleDrop(e) {
    e.preventDefault();
    let file = e.dataTransfer.files[0];
    console.log(e.dataTransfer.files[0]);
    this.props.onUpload(e.dataTransfer.files[0]);

    let fileType = file.type.split("/")[0];
    if (fileType !== "image") {
      console.log("Not an image file");
      this.setState({
        file: null,
        errorNotification: "Not an image File",
        dragOver: false,
      });
      return setTimeout(() => {
        this.setState({
          errorNotification: null,
        });
      }, 3000);
    }
    document.getElementById("upload-image-input").fileList =
      e.dataTransfer.files[0];

    this.setState({
      file,
      dragOver: false,
    });
  }
  handleAddImage(e) {
    e.preventDefault();
    let file = this.refs.image.files[0];
    console.log(this.refs.image.files[0]);
    this.props.onUpload(this.refs.image.files[0]);
    let fileType = this.refs.image.files[0].type.split("/")[0];
    if (fileType !== "image") {
      console.log("Not an image file");
      this.setState({
        file: null,
        errorNotification: "Not an image File",
        dragOverClass: "",
      });
      return setTimeout(() => {
        this.setState({
          errorNotification: null,
        });
      }, 3000);
    }

    this.setState({
      file,
    });
  }

  handleUploadImage(e) {
    e.preventDefault();
    if (this.refs.image.files[0]) {
      console.log("Uploading Image " + this.refs.image.files[0].name + "");
    }
  }
  handleCancelUpload(e) {
    e.preventDefault();
    this.setState({
      file: null,
    });
  }

  render() {
    let dragOverClass = this.state.dragOver
      ? `display-box drag-over`
      : `display-box`;

    let uploadText = this.state.file ? (
      <div>
        <h4>{this.state.file.name}</h4>
        <Button
          className="cancel-upload-button btn btn-warning"
          onClick={this.handleCancelUpload}
        >
          Remover
        </Button>
      </div>
    ) : (
      <div>
        <p>Clique ou arraste e solte o print da denuncia</p>
      </div>
    );

    let errorNotification = this.state.errorNotification ? (
      <div className="error-notification">
        <p>{this.state.errorNotification}</p>
      </div>
    ) : null;

    return (
      <div className="image-uploader-wrapper">
        <div className={dragOverClass}>
          <div className="icon-text-box">
            <div className="upload-text">{uploadText}</div>
            {errorNotification}
          </div>
          <div>
            <input
              type="file"
              ref="image"
              id="upload-image-input"
              className="upload-image-input"
              accept="image/*"
              onDrop={this.handleDrop}
              onDragEnter={this.handleDragEnter}
              onDragOver={this.handleDragOver}
              onDragLeave={this.handleDragLeave}
              onChange={this.handleAddImage}
            />
          </div>
        </div>
      </div>
    );
  }
}

export default Upload;
