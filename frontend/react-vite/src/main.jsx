import React from "react";
import { createRoot } from "react-dom/client";
import "./styles.css";

function App() {
  return <main className="shell"><h1>React + Vite listo</h1><p>Campuslands Docker Stack</p></main>;
}

createRoot(document.getElementById("root")).render(<App />);
