export type AskRequest = {
  question: string;
  context?: string;
  use_mcp?: boolean;
};

export type AskResponse = {
  answer: string;
  source: "local" | "mcp" | string;
  meta?: Record<string, unknown>;
};

// PUBLIC_INTERFACE
export async function askQuestion(payload: AskRequest, signal?: AbortSignal): Promise<AskResponse> {
  /** Ask the backend Q&A endpoint for an answer.
   * Uses REACT_APP_API_BASE if provided, otherwise same origin.
   */
  const base = process.env.REACT_APP_API_BASE || window.location.origin;
  const url = `${base.replace(/\/$/, "")}/api/qa/ask/`;
  const res = await fetch(url, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(payload),
    signal,
  });
  if (!res.ok) {
    const text = await res.text().catch(() => "");
    throw new Error(text || `Request failed with status ${res.status}`);
  }
  return res.json();
}
