
import { useState } from "react";
import { sendMessage } from "../services/aiService";
import "../style/chatbot.css";

function Chatbot({ user, onLogout }) {
  const [messages, setMessages] = useState([
    {
      role: "assistant",
      content:
        "Hello! Welcome to EnterpriseIQ. I'm your AI assistant. How can I help you today?",
    },
  ]);

  const [input, setInput] = useState("");
  const [loading, setLoading] = useState(false);

  async function handleSubmit(e) {
    e.preventDefault();

    const question = input.trim();

    if (!question || loading) {
      return;
    }

    // Display the user's message immediately.
    setMessages((previous) => [
      ...previous,
      {
        role: "user",
        content: question,
      },
    ]);

    setInput("");
    setLoading(true);

    try {
      // Call Spring Boot, which forwards the request to FastAPI.
      const data = await sendMessage(question);

      // Display the actual AI response.
      setMessages((previous) => [
        ...previous,
        {
          role: "assistant",
          content:
            data.answer ||
            "The AI service returned an empty response.",
        },
      ]);
    } catch (error) {
      console.error("AI chat error:", error);

      setMessages((previous) => [
        ...previous,
        {
          role: "assistant",
          content:
            "Sorry, I couldn't connect to the AI service. Please try again.",
        },
      ]);
    } finally {
      setLoading(false);
    }
  }

  function handleNewChat() {
    if (loading) return;

    setMessages([
      {
        role: "assistant",
        content: "Hello! What would you like to explore today?",
      },
    ]);

    setInput("");
  }

  return (
    <div className="chat-layout">
      {/* Sidebar */}
      <aside className="chat-sidebar">
        <div className="brand">
          <div className="brand-icon">E</div>

          <div>
            <h2>EnterpriseIQ</h2>
            <span>Intelligence Platform</span>
          </div>
        </div>

        <button
          className="new-chat-btn"
          onClick={handleNewChat}
          disabled={loading}
        >
          + New conversation
        </button>

        <div className="sidebar-section">
          <p className="sidebar-label">WORKSPACE</p>

          <div className="sidebar-item active">
            ✦ AI Assistant
          </div>

          <div className="sidebar-item">
            ◷ Recent conversations
          </div>

          <div className="sidebar-item">
            ▤ Knowledge base
          </div>
        </div>

        <div className="sidebar-user">
          <div className="avatar">
            {(user?.name || "U").charAt(0).toUpperCase()}
          </div>

          <div className="user-info">
            <strong>{user?.name || "User"}</strong>
            <span>{user?.email || ""}</span>
          </div>

          <button
            className="logout-btn"
            onClick={onLogout}
            title="Logout"
          >
            ↗
          </button>
        </div>
      </aside>

      {/* Main chat area */}
      <main className="chat-main">
        <header className="chat-header">
          <div>
            <h3>AI Assistant</h3>

            <span className="online-status">
              <span className="status-dot" />
              EnterpriseIQ workspace
            </span>
          </div>

          <div className="header-badge">✦ GenAI</div>
        </header>

        <section className="chat-content">
          <div className="welcome-heading">
            <div className="welcome-icon">✦</div>

            <h1>How can I help you today?</h1>

            <p>
              Ask questions, explore your documents, and get insights
              from your enterprise knowledge.
            </p>
          </div>

          {/* Messages */}
          <div className="messages">
            {messages.map((message, index) => (
              <div
                className={`message-row ${message.role}`}
                key={`${index}-${message.role}`}
              >
                <div className="message-avatar">
                  {message.role === "assistant" ? "✦" : "U"}
                </div>

                <div className="message-bubble">
                  <span className="message-author">
                    {message.role === "assistant"
                      ? "EnterpriseIQ AI"
                      : "You"}
                  </span>

                  <p>{message.content}</p>
                </div>
              </div>
            ))}

            {loading && (
              <div className="message-row assistant">
                <div className="message-avatar">✦</div>

                <div className="message-bubble">
                  <span className="message-author">
                    EnterpriseIQ AI
                  </span>

                  <p>Thinking... Please wait.</p>
                </div>
              </div>
            )}
          </div>

          {/* Input area */}
          <div className="chat-bottom">
            <div className="suggestions">
              {[
                "Summarize a document",
                "Explain a technical concept",
                "Find key insights",
              ].map((suggestion) => (
                <button
                  key={suggestion}
                  type="button"
                  disabled={loading}
                  onClick={() => setInput(suggestion)}
                >
                  {suggestion}
                </button>
              ))}
            </div>

            <form
              className="chat-input-form"
              onSubmit={handleSubmit}
            >
              <textarea
                value={input}
                onChange={(e) => setInput(e.target.value)}
                placeholder="Message EnterpriseIQ AI..."
                rows={2}
                disabled={loading}
                onKeyDown={(e) => {
                  if (
                    e.key === "Enter" &&
                    !e.shiftKey &&
                    !e.nativeEvent.isComposing
                  ) {
                    e.preventDefault();
                    e.currentTarget.form.requestSubmit();
                  }
                }}
              />

              <button
                type="submit"
                disabled={!input.trim() || loading}
                aria-label="Send message"
              >
                {loading ? "..." : "↑"}
              </button>
            </form>

            <p className="disclaimer">
              AI responses can be inaccurate. Verify important information.
            </p>
          </div>
        </section>
      </main>
    </div>
  );
}

export default Chatbot;
