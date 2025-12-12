type TaskItemProps = {
  task: { id: string; title: string; description?: string; completed: boolean };
  onToggle: (id: string) => void;
  onDelete: (id: string) => void;
};

export function TaskItem({ task, onToggle, onDelete }: TaskItemProps) {
  return (
    <div className="flex items-start justify-between border p-2 rounded">
      <div>
        <div className="font-semibold">{task.title}</div>
        {task.description && (
          <div className="text-sm text-gray-600">{task.description}</div>
        )}
        <div className="text-xs text-gray-500">
          Status: {task.completed ? "Done" : "Pending"}
        </div>
      </div>
      <div className="flex gap-2">
        <button
          className="px-3 py-1 border rounded"
          onClick={() => onToggle(task.id)}
        >
          {task.completed ? "Reopen" : "Complete"}
        </button>
        <button
          className="px-3 py-1 border rounded text-red-600"
          onClick={() => onDelete(task.id)}
        >
          Delete
        </button>
      </div>
    </div>
  );
}
