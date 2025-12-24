import react, { useState, useEffect } from "react";


function TaskForm({ onSave, onCancel, taskToEdit }) {
    const [task, setTask] = useState({
        title: '',
        priority: '',
        dueDate: ''
    })

    const [error, setError] = useState('');

    useEffect(() => {
        if (taskToEdit) {
            setTask(taskToEdit);
        }

        else {
            setTask({ title: '', priority: '', dueDate: '' });
        }
    }, [taskToEdit]);

    const handleChange = (e) => {
        const { name, value } = e.target;
        setTask(prevTask => ({
            ...prevTask,
            [name]: value
        }));
    };

    const handleSubmit = (e) => {
        e.preventDefault();

        if (!task.title.trim()) {
            setError('Title cannot be empty.');
            return;
        }
        const today = new Date().toISOString().split('T')[0];
        if (task.dueDate < today) {
            setError('Due date cannot be in the past.');
            return;
        }
        setError('');
        onSave(task);
    }
    return (
        <form onSubmit={handleSubmit} className="task-form">
            <h2>{taskToEdit ? 'Edit Task' : 'Add New Task'}</h2>
            {error && <p className='error-message'>{error}</p>}
            <div>
                <label htmlFor="title">Title:</label>
                <input
                    type="text"
                    id="title"
                    name="title"
                    value={task.title}
                    onChange={handleChange}
                    placeholder="Task list"
                />
            </div>

            <div>
                <label>Priority:</label>
                <select name="priority" value={task.priority} onChange={handleChange}>
                    <option value="Low">Low</option>
                    <option value="Medium">Medium</option>
                    <option value="High">High</option>
                </select>
            </div>

            <div className="due date">
                <label>Due Date:</label>
                <input
                    type="date"
                    id="dueDate"
                    name="dueDate"
                    value={task.dueDate}
                    onChange={handleChange}
                />
            </div>

            <div className="form-actions">
                <button type="submit" className="btn btn-primary">Save</button>
                <button type="button" onClick={onCancel} className="btn btn-secondary">Cancel</button>
            </div>
        </form>
    );
}

export default TaskForm;