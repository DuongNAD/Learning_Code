import logo from './logo.svg';
import './App.css';
import React, {useState} from 'react';
import TaskForm from './TaskForm';
import TaskList from './TaskList';
import TaskItem from './TaskItem';

const initialTasks = [
    { id: 1, title: 'Task 1', priority: 'High', dueDate: '2023-06-15' },
    { id: 2, title: 'Task 2', priority: 'Medium', dueDate: '2023-06-20' },
    { id: 3, title: 'Task 3', priority: 'Low', dueDate: '2023-06-25' },
];

function App() {
  const[tasks,setTasks] = useState(initialTasks);
  const[isFormVisible,setIsFormVisible] = useState(false);
  const[taskToEdit, setTaskToEdit] = useState(null);
  const[sortOrder, setSortOrder] = useState('asc')

  const handleSaveTask = (taskData) => {
    if(taskToEdit){
      const updatedTasks = tasks.map(task => (task.id === taskToEdit.id ? taskData : task));  
      setTasks(updatedTasks);
  }
  else{
    const newTask = {
      ...taskData,
      id: Date.now()
    };
    setTasks([...tasks, newTask]);
  }
  setIsFormVisible(false);
  setTaskToEdit(null);
  }

  const handleEditTask = (task) => {
    setTaskToEdit(task);
    setIsFormVisible(true); 
  };

  const handleDeleteTask = (taskId) => {
    if(window.confirm('are you sure you want to delete this task?')){
      const updatedTasks = tasks.filter(t => t.id !== taskId);
      setTasks(updatedTasks);
    }
  };

  const handleAddNewTask = () => {
    setIsFormVisible(true);
    setTaskToEdit(null);
  };

  const handleCancel = () => {
    setIsFormVisible(false);
    setTaskToEdit(null);
  };

  const handleSort = () => {
    const newSortOrder = sortOrder === 'asc' ? 'desc' : 'asc';
    setSortOrder(newSortOrder);
    const sortedTasks = [...tasks].sort((a, b) => {
      const dateA = new Date(a.dueDate);
      const dateB = new Date(b.dueDate);
      if (newSortOrder === 'asc') {
        return dateA - dateB;
      } else {
        return dateB - dateA;
      }
    });
    setTasks(sortedTasks);
  };

  return (
    <div className="app-container">
      <h1>Task Manager</h1>
      {isFormVisible ? (
        <TaskForm onSave={handleSaveTask} onCancel={handleCancel} taskToEdit={taskToEdit} />
      ) : (
        <TaskList
          tasks={tasks}
          onEdit={handleEditTask}
          onDelete={handleDeleteTask}
          onAddNew={handleAddNewTask}
          onSort={handleSort}
          sortOrder={sortOrder}
        />)}
    </div>
  );
}
export default App;
