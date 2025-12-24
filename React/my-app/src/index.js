import React from 'react';
import ReactDOM from 'react-dom/client'; // Quan trọng: import từ 'react-dom/client'
import './index.css';
import App from './App'; // Import component App từ file App.js

// Tạo root cho ứng dụng
const root = ReactDOM.createRoot(document.getElementById('root'));

// Render ứng dụng
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);