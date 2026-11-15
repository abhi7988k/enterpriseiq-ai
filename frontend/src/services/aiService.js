
const API_URL = import.meta.env.VITE_AI_API_URL;

console.log("AI API URL:", API_URL);

// Create one session ID for this browser conversation
let sessionId = localStorage.getItem("chat_session_id");

if (!sessionId) {
  sessionId = crypto.randomUUID();
  localStorage.setItem("chat_session_id", sessionId);
}

export async function sendMessage(prompt) {
  if (!API_URL) {
    throw new Error("VITE_AI_API_URL is not defined.");
  }

  const token = localStorage.getItem("token");

  const response = await fetch(API_URL, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      ...(token ? { Authorization: `Bearer ${token}` } : {}),
    },
    body: JSON.stringify({
      prompt,
      session_id: sessionId,
    }),
  });

  if (!response.ok) {
    const error = await response.text();
    throw new Error(`Request failed: ${response.status} - ${error}`);
  }

  return response.json();
}
