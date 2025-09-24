import React, { useState } from "react";
import { Toggle } from "./Toggle";

export type QuestionValues = {
  question: string;
  context?: string;
  use_mcp: boolean;
};

type Props = {
  onSubmit: (values: QuestionValues) => void;
  disabled?: boolean;
};

export function QuestionForm({ onSubmit, disabled }: Props) {
  const [question, setQuestion] = useState("");
  const [context, setContext] = useState("");
  const [useMcp, setUseMcp] = useState(false);

  const canSubmit = question.trim().length > 0 && !disabled;

  return (
    <form
      className="card"
      style={{ padding: 20, display: "grid", gap: 12, background: "var(--surface)" }}
      onSubmit={(e) => {
        e.preventDefault();
        if (!canSubmit) return;
        onSubmit({ question: question.trim(), context: context.trim() || undefined, use_mcp: useMcp });
      }}
    >
      <label style={{ display: "grid", gap: 6 }}>
        <span style={{ fontWeight: 600 }}>Your question</span>
        <input
          className="input"
          placeholder="Ask your question..."
          value={question}
          onChange={(e) => setQuestion(e.target.value)}
          required
        />
      </label>

      <label style={{ display: "grid", gap: 6 }}>
        <span style={{ fontWeight: 600 }}>Optional context</span>
        <textarea
          className="textarea"
          placeholder="Provide any additional context to guide the answer."
          rows={4}
          value={context}
          onChange={(e) => setContext(e.target.value)}
        />
      </label>

      <div style={{ display: "flex", alignItems: "center", justifyContent: "space-between", gap: 12 }}>
        <Toggle checked={useMcp} onChange={setUseMcp} label="Use MCP" />
        <button className="button" type="submit" disabled={!canSubmit}>
          Ask
        </button>
      </div>
    </form>
  );
}
