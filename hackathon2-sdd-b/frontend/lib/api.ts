const API_URL = process.env.NEXT_PUBLIC_API_URL || "http://localhost:8000";

const authHeaders = (token: string) => ({
  Authorization: `Bearer ${token}`,
  "Content-Type": "application/json",
});

export async function fetchTasks(token: string, userId: string) {
  const res = await fetch(`${API_URL}/api/${userId}/tasks`, {
    headers: authHeaders(token),
  });
  if (!res.ok) throw new Error("Failed to fetch tasks");
  return res.json();
}

export async function createTask(
  token: string,
  userId: string,
  data: { title: string; description?: string }
) {
  const res = await fetch(`${API_URL}/api/${userId}/tasks`, {
    method: "POST",
    headers: authHeaders(token),
    body: JSON.stringify(data),
  });
  if (!res.ok) throw new Error("Failed to create task");
  return res.json();
}

export async function updateTask(
  token: string,
  userId: string,
  taskId: string,
  data: { title: string; description?: string; completed: boolean }
) {
  const res = await fetch(`${API_URL}/api/${userId}/tasks/${taskId}`, {
    method: "PUT",
    headers: authHeaders(token),
    body: JSON.stringify(data),
  });
  if (!res.ok) throw new Error("Failed to update task");
  return res.json();
}

export async function deleteTask(token: string, userId: string, taskId: string) {
  const res = await fetch(`${API_URL}/api/${userId}/tasks/${taskId}`, {
    method: "DELETE",
    headers: authHeaders(token),
  });
  if (!res.ok) throw new Error("Failed to delete task");
  return true;
}

export async function completeTask(
  token: string,
  userId: string,
  taskId: string
) {
  const res = await fetch(`${API_URL}/api/${userId}/tasks/${taskId}/complete`, {
    method: "PATCH",
    headers: authHeaders(token),
  });
  if (!res.ok) throw new Error("Failed to complete task");
  return res.json();
}
