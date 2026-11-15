
import { useState } from "react";
import "./App.css";
import Login from "./pages/Login";
import Register from "./pages/Register";
import Chatbot from "./pages/Chatbot";

function App() {
  const [token, setToken] = useState(
    () => localStorage.getItem("token")
  );

  const [showRegister, setShowRegister] = useState(false);

  const [user, setUser] = useState(() => {
    try {
      return JSON.parse(localStorage.getItem("user")) || null;
    } catch {
      return null;
    }
  });

  function handleLogin(data) {
    localStorage.setItem("token", data.token);

    const userData = {
      id: data.id,
      name: data.name,
      email: data.email,
      role: data.role,
    };

    localStorage.setItem("user", JSON.stringify(userData));

    setToken(data.token);
    setUser(userData);
  }

  function handleLogout() {
    localStorage.removeItem("token");
    localStorage.removeItem("user");

    setToken(null);
    setUser(null);
    setShowRegister(false);
  }

  return (
    <div className="app">
      {token ? (
        <Chatbot user={user} onLogout={handleLogout} />
      ) : showRegister ? (
        <Register
          onLogin={() => setShowRegister(false)}
          onRegister={() => setShowRegister(false)}
        />
      ) : (
        <Login
          onLogin={handleLogin}
          onRegister={() => setShowRegister(true)}
        />
      )}
    </div>
  );
}

export default App;
