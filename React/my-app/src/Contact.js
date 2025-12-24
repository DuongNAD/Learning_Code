import React, { useState } from "react";

const Contact = () => {
    const [formData, setFormData] = useState({
        name: '',
        email: '',
        message: '',
    });

    const handleChange = (e) => {
        const { name, value } = e.target;
        setFormData({
            ...formData,
            [name]: value,
        });
    };

    const handleSubmit = (e) => {
        e.preventDefault();
        alert(`Cảm ơn, ${formData.name}! Chúng tôi sẽ liên hệ với bạn qua email: ${formData.email}`);
        setFormData({
            name: '',
            email: '',
            message: '',
        });
    };

    return (
        <div>
            <h1>Liên hệ</h1>
            <form onSubmit={handleSubmit}>
                <div style={{ marginBottom: '10px' }}>
                    <label>Tên:</label>
                    <input
                        type="text"
                        name="name"
                        value={formData.name}
                        onChange={handleChange}
                        style={{ width: '100%', padding: '5px', marginBottom: '5px' }}
                        required
                    />
                </div>

                <div style={{ marginBottom: '10px' }}>
                    <label>Email:</label>
                    <input
                        type="email"
                        name="email"
                        value={formData.email}
                        onChange={handleChange}
                        style={{ width: '100%', padding: '5px', marginBottom: '5px' }}>
                    </input>
                </div>

                <div style={{ marginBottom: '10px' }}>
                    <label>Tin nhắn:</label>
                    <textarea
                        name="message"
                        value={formData.message}
                        onChange={handleChange}
                        style={{ width: '100%', height: '100px', padding: '5px', marginBottom: '5px' }}
                        required
                    ></textarea>
                </div>

                <div>
                    <button type="submit" style={{ padding: '10px 20px', backgroundColor: '#4CAF50', color: '#fff', border: 'none', cursor: 'pointer' }}>Gửi</button>
                </div>
            </form>
        </div>
    );
};

export default Contact;