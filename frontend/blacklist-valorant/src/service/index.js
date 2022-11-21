import axios from "axios";

export const existElement = (list, name) => {
  console.log("existe", list);
  let result = false;
  list.forEach((element) => {
    console.log(element.riotid, "é igual a", name, element.riotid === name);
    if (element.riotid === name) result = true;
  });
  return result;
};

export const getDenunciados = async () => {
  try {
    const results = await axios.get("http://localhost:5000/add", {
      headers: { "Content-Type": "application/json" },
    });

    const arry = [];
    const resultFormated = results.data.map((item) => JSON.parse(item));
    resultFormated.forEach((item) => {
      const inclui = existElement(arry, item.riotid);
      if (!inclui) arry.push({ ...item, qtd: 1 });
      else {
        const idx = arry.findIndex(
          (denunciado) => denunciado.riotid === item.riotid
        );
        if (idx !== -1) arry[idx].qtd += 1;
      }
    });
    return arry.sort((a, b) => b.qtd - a.qtd);
  } catch (error) {
    console.log(error);
  }
  return [];
};

export const postDenuncia = async (nome, tag, text, texto) => {
  try {
    const results = await axios.post(
      "http://localhost:5000/add",
      { riotid: tag, desc: text, nome: nome, texto: texto },
      {
        headers: { "Content-Type": "application/json" },
      }
    );
    return results.data.ofensivo;
  } catch (error) {
    console.log(error);
  }
  return false;
};

export const postExtrairTexto = async (formData) => {
  try {
    const results = await axios.post(
      "http://localhost:5000/extrair",
      formData,
      {
        headers: {
          "Content-Type": "multipart/form-data",
        },
      }
    );
    return results.data.texto;
  } catch (error) {
    console.log(error);
  }
  return "";
};
