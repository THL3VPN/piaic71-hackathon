import { useState } from "react";

type TaskFormProps = {
  initial?: { title: string; description?: string; completed?: boolean };
  onSubmit: (data: { title: string; description?: string; completed?: boolean }) => void;
};

export function TaskForm({ initial, onSubmit }: TaskFormProps) {
  const [title, setTitle] = useState(initial?.title ?? "");
  const [description, setDescription] = useState(initial?.description ?? "");
  const [completed, setCompleted] = useState(initial?.completed ?? false);

  return (
    <form
      onSubmit={(e) => {
        e.preventDefault();
        onSubmit({ title, description, completed });
      }}
      className="flex flex-col gap-2"
    >
      <input
        className="border p-2"
        placeholder="Title"
        value={title}
        onChange={(e) => setTitle(e.target.value)}
      />
      <textarea
        className="border p-2"
        placeholder="Description"
        value={description}
        onChange={(e) => setDescription(e.target.value)}
      />
      <label className="flex items-center gap-2">
        <input
            type="checkbox"
            checked={completed}
            onChange={(e) => setCompleted(e.target.checked)}
        />
        Completed
      </label>
      <button type="submit" className="bg-blue-600 text-white px-4 py-2">
        Save
      </button>
    </form>
  );
}
