import React from "react";

export function Footer() {
  return (
    <footer style={{ borderTop: "1px solid rgba(17,24,39,0.08)", background: "rgba(255,255,255,0.6)" }}>
      <div className="container" style={{ display: "flex", alignItems: "center", justifyContent: "space-between", paddingTop: 18, paddingBottom: 18 }}>
        <span style={{ fontSize: 13, opacity: 0.8 }}>© {new Date().getFullYear()} Q&A Agent</span>
        <div style={{ display: "flex", gap: 16 }}>
          <a className="link" href="/redoc" target="_blank" rel="noreferrer">ReDoc</a>
          <a className="link" href="/swagger.json" target="_blank" rel="noreferrer">OpenAPI</a>
        </div>
      </div>
    </footer>
  );
}
