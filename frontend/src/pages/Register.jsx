
import { useState } from "react";
import { registerUser } from "../services/authService";

function Register({ onLogin, onRegister }) {
  const [formData, setFormData] = useState({
    name: "",
    email: "",
    password: "",
    confirmPassword: "",
  });

  const [error, setError] = useState("");
  const [loading, setLoading] = useState(false);
  const [success, setSuccess] = useState("");

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value,
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError("");
    setSuccess("");

    if (formData.password !== formData.confirmPassword) {
      setError("Passwords do not match.");
      return;
    }

    if (formData.password.length < 6) {
      setError("Password must contain at least 6 characters.");
      return;
    }

    try {
      setLoading(true);

      await registerUser({
        name: formData.name.trim(),
        email: formData.email.trim(),
        password: formData.password,
      });

      setSuccess("Account created successfully! Please log in.");

      setFormData({
        name: "",
        email: "",
        password: "",
        confirmPassword: "",
      });

      if (onRegister) {
        onRegister();
      }
    } catch (err) {
      setError(err.message || "Registration failed. Please try again.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div style={styles.page}>
      <div style={styles.card}>
        <div style={styles.logo}>EnterpriseIQ</div>

        <h1 style={styles.heading}>Create your account</h1>
        <p style={styles.subtitle}>
          Get started with your EnterpriseIQ account.
        </p>

        {error && <div style={styles.error}>{error}</div>}
        {success && <div style={styles.success}>{success}</div>}

        <form onSubmit={handleSubmit}>
          <label style={styles.label}>Full Name</label>
          <input
            type="text"
            name="name"
            placeholder="Enter your full name"
            value={formData.name}
            onChange={handleChange}
            required
            style={styles.input}
          />

          <label style={styles.label}>Email Address</label>
          <input
            type="email"
            name="email"
            placeholder="Enter your email"
            value={formData.email}
            onChange={handleChange}
            required
            style={styles.input}
          />

          <label style={styles.label}>Password</label>
          <input
            type="password"
            name="password"
            placeholder="Create a password"
            value={formData.password}
            onChange={handleChange}
            required
            minLength={6}
            style={styles.input}
          />

          <label style={styles.label}>Confirm Password</label>
          <input
            type="password"
            name="confirmPassword"
            placeholder="Confirm your password"
            value={formData.confirmPassword}
            onChange={handleChange}
            required
            style={styles.input}
          />

          <button
            type="submit"
            disabled={loading}
            style={{
              ...styles.button,
              opacity: loading ? 0.7 : 1,
              cursor: loading ? "not-allowed" : "pointer",
            }}
          >
            {loading ? "Creating Account..." : "Create Account"}
          </button>
        </form>

        <p style={styles.footer}>
          Already have an account?{" "}
          <button type="button" onClick={onLogin} style={styles.link}>
            Sign in
          </button>
        </p>
      </div>
    </div>
  );
}

const styles = {
  page: {
    minHeight: "100vh",
    display: "flex",
    justifyContent: "center",
    alignItems: "center",
    background: "#f3f4f6",
    padding: "24px",
    fontFamily: "Arial, sans-serif",
  },
  card: {
    width: "100%",
    maxWidth: "420px",
    background: "#ffffff",
    padding: "36px",
    borderRadius: "14px",
    boxShadow: "0 8px 30px rgba(0,0,0,0.08)",
  },
  logo: {
    color: "#2563eb",
    fontSize: "24px",
    fontWeight: "bold",
    textAlign: "center",
    marginBottom: "24px",
  },
  heading: {
    fontSize: "25px",
    color: "#111827",
    textAlign: "center",
    marginBottom: "8px",
  },
  subtitle: {
    color: "#6b7280",
    textAlign: "center",
    fontSize: "14px",
    marginBottom: "24px",
  },
  label: {
    display: "block",
    color: "#374151",
    fontSize: "14px",
    fontWeight: "600",
    marginBottom: "7px",
  },
  input: {
    width: "100%",
    boxSizing: "border-box",
    padding: "12px",
    border: "1px solid #d1d5db",
    borderRadius: "7px",
    marginBottom: "18px",
    fontSize: "14px",
    outline: "none",
  },
  button: {
    width: "100%",
    padding: "13px",
    border: "none",
    borderRadius: "7px",
    background: "#2563eb",
    color: "#ffffff",
    fontSize: "15px",
    fontWeight: "600",
    marginTop: "5px",
  },
  footer: {
    textAlign: "center",
    color: "#6b7280",
    fontSize: "14px",
    marginTop: "24px",
  },
  link: {
    border: "none",
    background: "none",
    color: "#2563eb",
    fontWeight: "600",
    cursor: "pointer",
  },
  error: {
    background: "#fee2e2",
    color: "#b91c1c",
    padding: "10px",
    borderRadius: "6px",
    fontSize: "13px",
    marginBottom: "16px",
  },
  success: {
    background: "#dcfce7",
    color: "#166534",
    padding: "10px",
    borderRadius: "6px",
    fontSize: "13px",
    marginBottom: "16px",
  },
};

export default Register;
