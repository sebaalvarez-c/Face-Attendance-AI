const API_URL = "http://127.0.0.1:8000";

async function apiPost(path, payload) {
  const response = await fetch(`${API_URL}${path}`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(payload)
  });

  const data = await response.json();

  if (!response.ok) {
    throw new Error(data.detail || "Error en la petición");
  }

  return data;
}

async function apiGet(path) {
  const response = await fetch(`${API_URL}${path}`);
  const data = await response.json();

  if (!response.ok) {
    throw new Error(data.detail || "Error en la petición");
  }

  return data;
}
