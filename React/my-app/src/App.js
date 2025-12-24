import React from 'react';
import './App.css';
import { BrowserRouter as Router, Route, Routes, Link } from 'react-router-dom';
import Home from './B1/Home';
import About from './B1/About';
import Contact from './B1/Contact';


const App = () => {
  return (
    <Router>
      <div style={{ padding: '20px' }}>
        <nav style={{ marginBottom: '20px' }}>
          <Link to="/" style={{ marginRight: '10px' }}>Trang chủ</Link>
          <Link to="/about" style={{ marginRight: '10px' }}>Giới thiệu</Link>
          <Link to="/contact">Liên hệ</Link>
        </nav>


        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/about" element={<About />} />
          <Route path="/contact" element={<Contact />} />
        </Routes>
      </div>
    </Router>
  );
}
export default App;