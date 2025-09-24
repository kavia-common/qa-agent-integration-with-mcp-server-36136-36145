import React from "react";
import { theme } from "../theme";

export function Header() {
  return (
    <header
      className="header-gradient"
      style={{
        borderBottom: "1px solid rgba(17,24,39,0.08)",
      }}
    >
      <div className="container" style={{ display: "flex", alignItems: "center", justifyContent: "space-between", paddingTop: 18, paddingBottom: 18 }}>
        <div style={{ display: "flex", alignItems: "center", gap: 12 }}>
          <div
            style={{
              width: 40,
              height: 40,
              borderRadius: 10,
              background: theme.primary,
              display: "grid",
              placeItems: "center",
              color: "#fff",
              fontWeight: 800,
            }}
            aria-label="App logo"
            title="Ocean Professional"
          >
            Q
          </div>
          <div>
            <div style={{ fontWeight: 700 }}>Q&amp;A Agent</div>
            <div className="badge" title="Theme">
              <span style={{ width: 8, height: 8, background: theme.secondary, borderRadius: "50%" }} />
              Ocean Professional
            </div>
          </div>
        </div>
        <nav>
          <a className="link" href="/docs" target="_blank" rel="noreferrer">API Docs</a>
        </nav>
      </div>
    </header>
  );
}
