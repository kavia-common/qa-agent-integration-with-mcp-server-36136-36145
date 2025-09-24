import React, { useCallback, useRef, useState } from "react";
import { QuestionForm, QuestionValues } from "../components/QuestionForm";
import { askQuestion, AskResponse } from "../services/api";
import { ErrorBanner } from "../components/ErrorBanner";
import { LoadingOverlay } from "../components/LoadingOverlay";
import { AnswerCard } from "../components/AnswerCard";

function Home() {
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string>("");
  const [answer, setAnswer] = useState<AskResponse | null>(null);
  const abortRef = useRef<AbortController | null>(null);

  const onSubmit = useCallback(async (values: QuestionValues) => {
    setError("");
    setAnswer(null);
    setLoading(true);

    if (abortRef.current) {
      try { abortRef.current.abort(); } catch {}
    }
    const controller = new AbortController();
    abortRef.current = controller;

    try {
      const res = await askQuestion(
        { question: values.question, context: values.context, use_mcp: values.use_mcp },
        controller.signal
      );
      setAnswer(res);
    } catch (e: any) {
      setError(e?.message || "Something went wrong");
    } finally {
      setLoading(false);
      abortRef.current = null;
    }
  }, []);

  return (
    <div style={{ display: "grid", gap: 16 }}>
      <section className="card" style={{ padding: 20, background: "var(--gradient)" as any }}>
        <h2 style={{ margin: 0 }}>Ask the Q&amp;A Agent</h2>
        <p style={{ marginTop: 8, opacity: 0.8 }}>
          Modern, responsive UI with Ocean Professional theme.
        </p>
      </section>

      {error && <ErrorBanner message={error} />}

      <QuestionForm onSubmit={onSubmit} disabled={loading} />

      {answer && (
        <AnswerCard answer={answer.answer} source={answer.source} meta={answer.meta} />
      )}

      <LoadingOverlay visible={loading} note="Contacting the backend API..." />
    </div>
  );
}

export default Home;
