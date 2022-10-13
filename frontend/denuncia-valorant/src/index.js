import React from "react";
import ReactDOM from "react-dom/client";
import "./index.scss";

import { BrowserRouter, Routes, Route } from "react-router-dom";

import Main from "./pages/main";
import Form from "./pages/form";
import List from "./pages/list";

const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(
  <React.StrictMode>
    <BrowserRouter>
      <Routes>
        <Route path="/">
          <Route index element={<Main />} />
          <Route path="denuncia" element={<Form />} />
          <Route path="lista" element={<List />} />
        </Route>
      </Routes>
    </BrowserRouter>
  </React.StrictMode>
);
