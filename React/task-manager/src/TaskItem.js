import react from "react";

function TaskItem ({ task, onEdit, onDelete }) {
    return (
        <tr>
            <td>{task.title}</td>
            <td>{task.priority}</td>
            <td>{task.dueDate}</td>
            <td>
                <button onClick={() => onEdit(task)} className="fas fa-edit">Edit</button>
                <button onClick={() => onDelete(task.id)} className="fas fa-trash-alt">Delete</button>
            </td>
            
        </tr>
    )
}

export default TaskItem;