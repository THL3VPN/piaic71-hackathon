"use client";

import { useEffect, useState } from "react";
import { TaskForm } from "../../components/TaskForm";
import { TaskList } from "../../components/TaskList";
import {
  fetchTasks,
  createTask,
  deleteTask,
  completeTask,
  updateTask,
} from "../../lib/api";
import { getSession } from "../../lib/auth";

type Task = { id: string; title: string; description?: string; completed: boolean };

export default function TasksPage() {
  const [tasks, setTasks] = useState<Task[]>([]);
  const session = getSession();
  const token = session?.token ?? "";
  const userId = session?.userId ?? "";

  useEffect(() => {
    if (!token || !userId) return;
    fetchTasks(token, userId)
      .then((data) => setTasks(data.items || []))
      .catch((err) => console.error(err));
  }, [token, userId]);

  const handleCreate = async (data: { title: string; description?: string }) => {
    if (!token || !userId) return;
    const task = await createTask(token, userId, data);
    setTasks((prev) => [task, ...prev]);
  };

  const handleToggle = async (id: string) => {
    if (!token || !userId) return;
    const updated = await completeTask(token, userId, id);
    setTasks((prev) => prev.map((t) => (t.id === id ? updated : t)));
  };

  const handleDelete = async (id: string) => {
    if (!token || !userId) return;
    await deleteTask(token, userId, id);
    setTasks((prev) => prev.filter((t) => t.id !== id));
  };

  const handleUpdate = async (taskId: string, data: Task) => {
    if (!token || !userId) return;
    const updated = await updateTask(token, userId, taskId, data);
    setTasks((prev) => prev.map((t) => (t.id === taskId ? updated : t)));
  };

  return (
    <main className="p-6 max-w-2xl mx-auto">
      <h1 className="text-2xl font-bold mb-4">Tasks</h1>
      <TaskForm onSubmit={handleCreate} />
      <div className="mt-4">
        <TaskList tasks={tasks} onToggle={handleToggle} onDelete={handleDelete} />
      </div>
    </main>
  );
}
