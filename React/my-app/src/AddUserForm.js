import React, { useState } from 'react';

function AddUserForm({ onAddUser }) {
    const [formData, setFormData] = useState({ name: '', age: '', email: '' });

    const handleInputChange = (e) => {
        const { name, value } = e.target;
        setFormData({ ...formData, [name]: value });
    };

    const handleSubmit = (e) => {
        e.preventDefault();
        
        if (formData.name && formData.age && formData.email) {
            onAddUser({
                name: formData.name,
                age: parseInt(formData.age, 10),
                email: formData.email,
            });
            setFormData({ name: '', age: '', email: '' });
        } else {
            alert('Vui lòng điền đủ thông tin');
        }
    };

    return (
        <form onSubmit={handleSubmit} style={{ marginBottom: '20px' }}>
            <h3>Thêm người dùng mới</h3>
            <div>
                <input
                    type="text"
                    name="name"
                    value={formData.name}
                    onChange={handleInputChange}
                    placeholder="Nhập tên"
                    style={{ marginRight: '10px', padding: '5px' }}
                />

                <input
                    type="number" 
                    name="age"
                    value={formData.age}
                    onChange={handleInputChange}
                    placeholder="Nhập tuổi"
                    style={{ marginRight: '10px', padding: '5px' }}
                />

                <input
                    type="email" 
                    name="email"
                    value={formData.email}
                    onChange={handleInputChange}
                    placeholder="Nhập email"
                    style={{ marginRight: '10px', padding: '5px' }}
                />

                <button type="submit" style={{ padding: '5px 10px' }}>
                    Thêm người dùng
                </button>
            </div>
        </form>
    );
}

export default AddUserForm;