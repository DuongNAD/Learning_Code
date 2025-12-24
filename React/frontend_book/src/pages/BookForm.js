import React, { useState } from 'react';

function BookForm({ onSubmit, initialData, onCancel }) {
  const [formData, setFormData] = useState({
    id: initialData.id || '',
    title: initialData.title || '',
    author: initialData.author || '',
    price: initialData.price || '',
  });

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setFormData({ ...formData, [name]: value });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    if (formData.title && formData.author && formData.price) {
      onSubmit({
        id: formData.id,
        title: formData.title,
        author: formData.author,
        price: parseFloat(formData.price),
      });
    } else {
      alert('Vui lòng điền đầy đủ thông tin!');
    }
  };

  return (
    <div style={{ marginBottom: '20px', border: '1px solid #ccc', padding: '10px' }}>
      <h3>{initialData.id ? 'Chỉnh sửa sách' : 'Thêm sách mới'}</h3>
      <div>
        <input type="text" name="title" value={formData.title}
          onChange={handleInputChange} placeholder="Nhập tiêu đề"
          style={{ marginRight: '10px', padding: '5px' }}
        />
        <input type="text" name="author" value={formData.author}
          onChange={handleInputChange} placeholder="Nhập tác giả"
          style={{ marginRight: '10px', padding: '5px' }}
        />
        <input type="number" name="price" value={formData.price} 
          onChange={handleInputChange} placeholder="Nhập giá"
          style={{ marginRight: '10px', padding: '5px' }}
        />
        <button onClick={handleSubmit} 
          style={{ padding: '5px 10px', marginRight: '10px' }}>
          {initialData.id ? 'Cập nhật' : 'Thêm'}
        </button>
        <button onClick={onCancel}
          style={{ padding: '5px 10px', background: '#ff4d4f', color: 'white' }}
        > Hủy </button>
      </div>
    </div>
  );
}

export default BookForm;