import react from "react";
import TaskItem from "./TaskItem";


function TaskList({ tasks, onEdit, onDelete, onAddNew, onSort, sortOrder }) {
    return (
        <div className="task-list">
            <h2>Task Manager</h2>
            <p className="summary">Total Task: {tasks.length}</p>
            <div className="toolbar">
                <button onClick={onAddNew} className="btn btn-primary">Add New</button>
                <button onClick={onSort} className="btn btn-secondary">Sort by Due Date  ({sortOrder === 'asc' ? 'Ascending' : 'Descending'})</button>
            </div>


            <table>
                <thead>
                    <tr>
                        <th>Title</th>
                        <th>Priority</th>
                        <th>Due Date</th>
                        <th className="actions-header">Actions</th>
                    </tr>
                </thead>
                <tbody>
                    {tasks.map((task) => (
                        <TaskItem key={task.id} task={task} onEdit={onEdit} onDelete={onDelete} />
                    ))}
                </tbody>
            </table>
        </div>
    );
}

export default TaskList;