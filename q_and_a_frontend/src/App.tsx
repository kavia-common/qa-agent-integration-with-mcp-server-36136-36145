import React from "react";
import { Header } from "./components/Header";
import { Footer } from "./components/Footer";
import Home from "./pages/Home";
import { theme } from "./theme";

function App() {
  return (
    <div
      style={{
        minHeight: "100%",
        display: "flex",
        flexDirection: "column",
        background: theme.background,
      }}
    >
      <Header />
      <main className="container" style={{ flex: 1 }}>
        <Home />
      </main>
      <Footer />
    </div>
  );
}

export default App;
