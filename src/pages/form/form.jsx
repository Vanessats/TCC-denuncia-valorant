import React, { useState } from "react";
import "./form.scss";

import Title from "../../components/title";
import Input from "../../components/input";
import Upload from "../../components/upload";
import TextArea from "../../components/textarea";
import Button from "../../components/button";

import { ToastContainer, toast } from "react-toastify";

import axios from "axios";

import { postDenuncia } from "../../service/index";

const Form = () => {
  const notifySucess = () =>
    toast.success("Sucesso! denúncia registrada com sucesso.", {
      position: "top-right",
      autoClose: 5000,
      hideProgressBar: false,
      closeOnClick: true,
      pauseOnHover: true,
      draggable: true,
      progress: undefined,
      theme: "colored",
    });

  const notifyError = () =>
    toast.error("Sua denúncia é inválida, verifique as informações inseridas", {
      position: "top-right",
      autoClose: 5000,
      hideProgressBar: false,
      closeOnClick: true,
      pauseOnHover: true,
      draggable: true,
      progress: undefined,
      theme: "colored",
    });

  const fetchExtract = async () => {
    const formData = new FormData();
    formData.append("imagem", file);
    try {
      const response = await axios({
        method: "post",
        url: "http://localhost:5000/extrair",
        data: formData,
        headers: { "Content-Type": "multipart/form-data" },
      });
      console.log(response.data.texto);
      return response.data.texto;
    } catch (error) {
      console.log(error);
    }
    return "";
  };

  const handleSubmit = async () => {
    const texto = await fetchExtract();
    const resposta = await postDenuncia(
      nome,
      tag,
      text,
      texto.replace(/\n/g, " ")
    );
    resposta ? notifySucess() : notifyError();
  };

  const [file, setFile] = useState();
  const [nome, setNome] = useState();
  const [tag, setTag] = useState();
  const [text, setText] = useState();

  return (
    <div>
      <div id="form">
        <Title />
        <Upload onUpload={(file) => setFile(file)} eraseFile />
        <div className="container">
          <Input
            placeholder="Nome"
            onChange={(event) => setNome(event.target.value)}
            maxLength="16"
          />
          <Input
            placeholder="TAG"
            onChange={(event) => setTag(event.target.value)}
            maxLength="4"
          />
        </div>
        <br />
        <br />
        <TextArea
          placeholder="Insira aqui o text referente ao acontecimento..."
          onChange={(event) => setText(event.target.value)}
          maxLength="512"
        />
        <br />
        <Button
          onClick={() => handleSubmit()}
          disabled={!nome || !tag || !text | !file?.name}
        >
          Enviar Denúncia
        </Button>
      </div>
      <ToastContainer
        position="top-right"
        autoClose={5000}
        hideProgressBar={false}
        newestOnTop={false}
        closeOnClick
        rtl={false}
        pauseOnFocusLoss
        draggable
        pauseOnHover
        theme="colored"
      />
    </div>
  );
};

export default Form;
