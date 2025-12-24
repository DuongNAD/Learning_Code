import React, { useState, useEffect } from 'react';
import BookCard from './pages/BookCard';
import BookForm from './pages/BookForm';
import axios from 'axios';
import './App.css'; // Import file CSS


const API_BASE_URL = 'http://localhost/demo/PHP/backend_books';

function App() {
  const [books, setBooks] = useState([]);
  const [showForm, setShowForm] = useState(false);
  const [editingBook, setEditingBook] = useState(null);

  // Hàm lấy danh sách sách từ backend
  const fetchBooks = async () => {
    try {
      // Gọi đến file readBook.php
      const response = await axios.get(`${API_BASE_URL}/readBook.php`);
      // axios sẽ tự động parse JSON, response.data chính là mảng books
      setBooks(response.data); 
    } catch (error) {
      console.error('Error fetching books:', error);
      // Nếu backend trả về lỗi dạng JSON, bạn có thể hiển thị nó
      if (error.response && error.response.data.error) {
        alert(`Lỗi từ server: ${error.response.data.error}`);
      }
    }
  };

  // Sử dụng useEffect để gọi fetchBooks một lần khi component mount
  useEffect(() => {
    fetchBooks();
  }, []);

  // Hàm xử lý thêm hoặc cập nhật sách
  const handleFormSubmit = async (bookData) => {
    // Nếu có editingBook, nghĩa là đang ở chế độ cập nhật
    if (editingBook) {
      await updateBook({ ...bookData, id: editingBook.id });
    } else { // Ngược lại là thêm mới
      await addBook(bookData);
    }
  };

  // Thêm sách mới
  const addBook = async (book) => {
    try {
      // Giả sử bạn có file createBook.php
      await axios.post(`${API_BASE_URL}/createBook.php`, book);
      fetchBooks(); // Tải lại danh sách sách
      setShowForm(false);
    } catch (error) {
      console.error('Error adding book:', error);
    }
  };

  // Cập nhật sách
  const updateBook = async (book) => {
    try {
      await axios.post(`${API_BASE_URL}/updateBook.php`, book);
      fetchBooks(); // Tải lại danh sách sách
      setShowForm(false);
      setEditingBook(null);
    } catch (error) {
      console.error('Error updating book:', error);
    }
  };

  // Xóa sách
  const deleteBook = async (id) => {
    // Hỏi xác nhận trước khi xóa
    if (window.confirm('Bạn có chắc chắn muốn xóa sách này không?')) {
      try {
        await axios.post(`${API_BASE_URL}/deleteBook.php`, { id });
        fetchBooks(); // Tải lại danh sách sách
      } catch (error) {
        console.error('Error deleting book:', error);
      }
    }
  };

  // Hiển thị form thêm mới
  const handleShowAddForm = () => {
    setEditingBook(null);
    setShowForm(true);
  };

  // Hiển thị form chỉnh sửa
  const handleEditBook = (book) => {
    setEditingBook(book);
    setShowForm(true);
  };

  // Hủy form
  const handleCancel = () => {
    setShowForm(false);
    setEditingBook(null);
  };

  return (
    <div className="container">
      <h1>Quản lý sách</h1>

      {/* Nút "Thêm sách mới" chỉ hiện khi form đang ẩn */}
      {!showForm && (
        <button onClick={handleShowAddForm} className="btn btn-primary">
          Thêm sách mới
        </button>
      )}

      {/* Form chỉ hiện khi showForm là true */}
      {showForm && (
        <BookForm 
          onSubmit={handleFormSubmit}
          initialData={editingBook || { title: '', author: '', price: '' }}
          onCancel={handleCancel}
        />
      )}

      {/* Hiển thị danh sách sách */}
      <div className="book-list">
        {books.length === 0 && !showForm ? (
          <p>Chưa có sách nào.</p>
        ) : (
          books.map((book) => (
            <BookCard 
              key={book.id} 
              book={book}
              onEdit={() => handleEditBook(book)} // Sửa lại để truyền cả book
              onDelete={() => deleteBook(book.id)} // Sửa lại để truyền id
            />
          ))
        )}
      </div>
    </div>
  );
}

export default App;