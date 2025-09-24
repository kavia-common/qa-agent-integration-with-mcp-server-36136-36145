# Q&A Frontend (Ocean Professional)

Modern React frontend to interact with the Q&A backend agent, using the "Ocean Professional" style (blue and amber accents, minimalist layout, subtle gradients, rounded corners).

Features:
- Ask questions and display answers via backend REST API.
- Loading, error, and success states.
- Responsive, modern UI with Ocean Professional theme.
- Extensible component structure (future: history, MCP interactions).
- Environment-based API base URL configuration.

Quick start:
1) Install dependencies:
   npm install

2) Configure environment:
   - Copy .env.example to .env
   - Adjust REACT_APP_API_BASE as needed (defaults to current origin)

3) Run development server:
   npm start

Build for production:
   npm run build

Project structure:
- src/
  - index.tsx: Entry point
  - App.tsx: App shell with layout & routes
  - theme.ts: Ocean Professional theme tokens
  - services/api.ts: API client for backend
  - components/
    - QuestionForm.tsx: Input form for Q&A
    - AnswerCard.tsx: Card to display the answer
    - LoadingOverlay.tsx: Fullscreen loading state
    - ErrorBanner.tsx: Error display
    - Header.tsx: App header with theme accents
    - Footer.tsx: Footer with links/info
    - Toggle.tsx: Small accessible toggle switch (for use_mcp)
  - pages/
    - Home.tsx: Main Q&A screen

Environment variables:
- REACT_APP_API_BASE: Base URL for the backend API (default: same origin). Do not include trailing slash.
  Example: https://your-backend-host.com

Backend endpoint:
- POST {REACT_APP_API_BASE}/api/qa/ask/

Payload:
{
  "question": "What is MCP?",
  "context": "Optional context",
  "use_mcp": true
}

Expected response:
{
  "answer": "text",
  "source": "local" | "mcp",
  "meta": { ... }
}

Notes:
- If deploying frontend separately from backend, make sure CORS is properly configured on backend. The provided backend defaults allow all origins (for dev).
- For MCP usage, the backend requires MCP envs (see backend README). Frontend only toggles use_mcp.

Future extensions (suggested):
- Conversation history panel
- MCP tool invocation UI
- Theming switch / dark mode
- Persisted sessions
