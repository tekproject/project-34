import * as React from "react";
import { Routes, Route, BrowserRouter } from "react-router-dom";
import Game from "./Game";
import Home from "./Home";


const AppRoutes = () => {
  return (
    <div>
      <BrowserRouter>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/game" element={<Game />} />
        </Routes>
      </BrowserRouter>

    </div>
  );
};

export default AppRoutes;
