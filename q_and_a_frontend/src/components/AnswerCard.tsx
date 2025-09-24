import React from "react";
import { theme } from "../theme";

type Props = {
  answer: string;
  source: string;
  meta?: Record<string, unknown>;
};

export function AnswerCard({ answer, source, meta }: Props) {
  return (
    <section className="card" style={{ padding: 20 }}>
      <div style={{ display: "flex", alignItems: "center", justifyContent: "space-between", marginBottom: 8 }}>
        <h3 style={{ margin: 0 }}>Answer</h3>
        <span className="badge" title="Answer Source">
          <span
            style={{
              width: 8, height: 8, borderRadius: "50%",
              background: source === "mcp" ? theme.secondary : theme.primary
            }}
          />
          {source === "mcp" ? "MCP" : "Local"}
        </span>
      </div>
      <p style={{ marginTop: 8, lineHeight: 1.6 }}>{answer}</p>

      {meta && (
        <details style={{ marginTop: 12 }}>
          <summary style={{ cursor: "pointer" }}>Details</summary>
          <pre style={{
            whiteSpace: "pre-wrap",
            overflowX: "auto",
            background: "rgba(0,0,0,0.03)",
            borderRadius: 8,
            padding: 12,
            border: "1px solid rgba(17,24,39,0.06)"
          }}>
{JSON.stringify(meta, null, 2)}
          </pre>
        </details>
      )}
    </section>
  );
}
