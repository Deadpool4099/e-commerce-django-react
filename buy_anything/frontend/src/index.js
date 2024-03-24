import React from "react";
import { render } from "react-dom";
import ReactDOM from 'react-dom/client';
import App from "./components/App";

const appDiv = ReactDOM.createRoot(document.getElementById('app'));
appDiv.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);

