import React from "react";
import Menu from "./components/Menu";
import "./styles.css";

export default function App() {
  return (
    <div className="app">
      <header className="header">
        <h1>Kafe Menu</h1>
      </header>
      <main>
        <Menu />
      </main>
    </div>
  );
}
