import React from "react";
import { Link } from "react-router-dom";

import "./list.scss";

import Paper from "../../components/paper";
import Title from "../../components/title";
import Button from "../../components/button";

const array = [
  "NoobMaster69 #6578 - 78 denuncias",
  "Pedrin69 #7654 - 35 denuncias",
  "Hunson #2232 - 25 denuncias",
  "JhonTravolta57 #9867 - 24 denuncias",
  "Xerox #1132 - 22 denuncias",
  "Tremdasonze67 #1237 - 21 denuncias",
  "Renanzin #8764 - 20 denuncias",
  "LukinhaReiDelas #9900 - 18 denuncias",
  "Sapateira #2324 - 17 denuncias",
  "Pedrao #5555 - 17 denuncias",
  "Tutu #1234 - 16 denuncias",
  "SantosDrugon #5490 - 15 denuncias",
  "Felipe #6668 - 14 denuncias",
  "Cebola #2341 - 12 denuncias",
  "gabrielfoda34 #7812 - 08 denuncias",
];

const List = () => {
  return (
    <div id="list">
      <Title />
      <Paper>
        {array.map((item) => (
          <>
            <span>{item}</span>
            <br />
          </>
        ))}
      </Paper>
    </div>
  );
};

export default List;
