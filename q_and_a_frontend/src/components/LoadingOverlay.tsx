import React from "react";

type Props = { visible: boolean; note?: string };

export function LoadingOverlay({ visible, note }: Props) {
  if (!visible) return null;
  return (
    <div
      aria-busy="true"
      style={{
        position: "fixed",
        inset: 0,
        background: "rgba(255,255,255,0.6)",
        backdropFilter: "blur(2px)",
        display: "grid",
        placeItems: "center",
        zIndex: 1000
      }}
    >
      <div className="card" style={{ padding: 20, textAlign: "center" }}>
        <div className="spinner" style={{ marginBottom: 10 }}>
          <div style={{
            width: 36, height: 36, borderRadius: "50%",
            border: "4px solid rgba(37,99,235,0.25)",
            borderTopColor: "var(--primary)",
            animation: "spin 0.9s linear infinite"
          }} />
        </div>
        <div style={{ fontWeight: 600 }}>Thinking...</div>
        {note && <div style={{ fontSize: 12, opacity: 0.8, marginTop: 6 }}>{note}</div>}
      </div>
      <style>
        {`@keyframes spin { to { transform: rotate(360deg); } }`}
      </style>
    </div>
  );
}
