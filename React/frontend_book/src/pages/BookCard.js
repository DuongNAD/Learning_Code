import React from 'react';

function BookCard({ book, onEdit, onDelete }) {
  return (
    <div style={{ border: '1px solid #ccc', padding: '10px', margin: '10px' }}>
      <h3>Tiêu đề: {book.title}</h3>
      <p>Tác giả: {book.author}</p>
      <p>Giá: {book.price}</p>
      <button onClick={() => onEdit(book)}
        style={{ padding: '5px 10px', marginRight: '10px' }}> Sửa
      </button>
      <button onClick={() => onDelete(book.id)}
        style={{ padding: '5px 10px', background: '#ff4d4f', color: 'white' }}
      > Xóa </button>
    </div>
  );
}

export default BookCard;