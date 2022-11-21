import React from "react";

import "./main.scss";

import { Link } from "react-router-dom";

import Title from "../../components/title";
import Button from "../../components/button";

const Main = () => {
  return (
    <section id="main">
      <div className="content">
        <Title larger />
        <hr />
        <div className="description">
          <span>
            Valorant foi criado para que se possa divertir com seus amigos além
            de interagir e conhecer novos jogadores. Ao longo dos anos, se
            tornou comum a presença de jogadores Tóxicos em diversos jogos e foi
            inevitável a chegada dos mesmos ao valorant. Este portal foi criado
            por estudantes que visavam lutar contra as atitudes ofensivas de
            jogadores que acabam com o mento de lazer alheio além de afastar
            novos jogadores, afastados pela má fama que o jogo pode ter em
            decorrência de tais comportamentos.
          </span>
        </div>
        <br />
        <Link to="/denuncia">
          <Button style={{ marginTop: "15px" }}>Fazer Denúncia</Button>
        </Link>
        <Link to="/lista">
          <Button style={{ marginTop: "15px", marginLeft: "5px" }}>
            Lista Denunciados
          </Button>
        </Link>
      </div>
    </section>
  );
};

export default Main;
