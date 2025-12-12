import { TaskItem } from "./TaskItem";

type Task = { id: string; title: string; description?: string; completed: boolean };

type TaskListProps = {
  tasks: Task[];
  onToggle: (id: string) => void;
  onDelete: (id: string) => void;
};

export function TaskList({ tasks, onToggle, onDelete }: TaskListProps) {
  if (!tasks.length) {
    return <div className="text-gray-600">No tasks yet.</div>;
  }
  return (
    <div className="flex flex-col gap-2">
      {tasks.map((task) => (
        <TaskItem key={task.id} task={task} onToggle={onToggle} onDelete={onDelete} />
      ))}
    </div>
  );
}
