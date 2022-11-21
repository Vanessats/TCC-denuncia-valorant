import React, { useEffect, useState } from "react";

import "./list.scss";

import Paper from "../../components/paper";
import Title from "../../components/title";

import { getDenunciados } from "../../service/index";

const List = () => {
  const [denunciados, setDenunciados] = useState([]);

  const fetch = async () => {
    const response = await getDenunciados();
    setDenunciados(response);
  };

  useEffect(() => {
    fetch();
  }, []);

  return (
    <div id="list">
      <Title />
      <Paper>
        {denunciados.map((jogador) => (
          <React.Fragment key={jogador.riotid}>
            <span>
              {jogador.nome} #{jogador.riotid} - {jogador.qtd} denúncias.
            </span>
            <br />
          </React.Fragment>
        ))}
      </Paper>
    </div>
  );
};

export default List;
