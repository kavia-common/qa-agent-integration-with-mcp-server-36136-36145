import React from "react";

type Props = { message: string };

export function ErrorBanner({ message }: Props) {
  if (!message) return null;
  return (
    <div
      className="card"
      role="alert"
      style={{
        padding: 12,
        borderLeft: "4px solid var(--error)",
        background: "rgba(239,68,68,0.05)",
        color: "var(--text)"
      }}
    >
      <strong style={{ color: "var(--error)" }}>Error:</strong> <span style={{ marginLeft: 6 }}>{message}</span>
    </div>
  );
}
