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
            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam
            imperdiet erat quis mollis mattis. Proin sit amet urna consectetur,
            ultrices quam a, accumsan justo. Vivamus sed maximus nunc. Quisque
            convallis euismod pharetra. Aliquam lacinia ut tellus non
            ullamcorper. Quisque massa nisl, vehicula nec euismod quis, viverra
            vel leo. Donec quis tellus ut felis vulputate porta. Suspendisse sit
            amet suscipit turpis, sit amet egestas ante. Orci varius natoque
            penatibus et magnis dis parturient montes, nascetur ridiculus mus.
            Nullam condimentum dictum lectus at venenatis. Vivamus a viverra mi,
            ut tristique ante. Nulla a erat id purus efficitur aliquet. Duis
            posuere nulla quis ex sodales, condimentum lobortis augue ultricies.
            Curabitur ullamcorper sem non venenatis sagittis. Curabitur eget
            nibh id felis vehicula tempor. Nam sed tristique mi.
          </span>
        </div>
        <br />
        <Link to="/denuncia">
          <Button style={{ marginTop: "15px" }}>Fazer Denuncia</Button>
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
