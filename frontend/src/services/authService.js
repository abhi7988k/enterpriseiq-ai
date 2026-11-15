
const API_BASE_URL = import.meta.env.VITE_API_BASE_URL;

console.log("API BASE URL:", API_BASE_URL);


export async function registerUser(userData) {
  const response = await fetch(`${API_BASE_URL}/users`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      Accept: "application/json",
    },
    body: JSON.stringify(userData),
  });

  if (!response.ok) {
    if (response.status === 409 || response.status === 400) {
      throw new Error("Email already registered or invalid registration details.");
    }

    throw new Error(`Registration failed. Server returned status ${response.status}.`);
  }

  return response.json();
}


export async function loginUser(email, password) {
  const response = await fetch(`${API_BASE_URL}/auth/login`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      Accept: "application/json",
    },
    body: JSON.stringify({ email, password }),
  });

  if (!response.ok) {
    if (response.status === 401 || response.status === 400) {
      throw new Error("Invalid email or password.");
    }

    throw new Error(
      `Login failed. Server returned status ${response.status}.`
    );
  }

  const data = await response.json();

  if (!data.token) {
    throw new Error("Login succeeded, but no JWT token was returned.");
  }

  return data;
}
