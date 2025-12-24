import React, { useState, useEffect } from "react";
import { Link } from "react-router-dom";

const Home = () => {
    const products = [
        { id: 1, name: 'Laptop', price: 1000, description: 'Laptop hiệu năng cao', category: 'Electronics' },
        { id: 2, name: 'Điện thoại', price: 700, description: 'Điện thoại thông minh', category: 'Electronics' },
        { id: 3, name: 'Tai nghe', price: 100, description: 'Tai nghe không dây', category: 'Electronics' },
        { id: 4, name: 'Máy ảnh', price: 1200, description: 'Máy ảnh chuyên nghiệp', category: 'Electronics' },
        { id: 5, name: 'Loa Bluetooth', price: 150, description: 'Loa không dây chất lượng', category: 'Electronics' },
        { id: 6, name: 'Máy tính bảng', price: 500, description: 'Máy tính bảng tiện lợi', category: 'Electronics' },
    ];

    // Khởi tạo state là một object rỗng
    const [images, setImages] = useState({});
    const [loading, setLoading] = useState(false);
    const [apiError, setApiError] = useState('');

    useEffect(() => {
        const fetchImages = async () => {
            setLoading(true);
            setApiError('');

            const imagePromises = products.map(async (product) => {
                try {
                    const query = encodeURIComponent(product.name);
                    // SỬA LỖI 1: Dùng dấu backtick (`) thay vì nháy đơn (')
                    const response = await fetch(`https://api.unsplash.com/search/photos?query=${query}&per_page=1&client_id=foCpbkzB8LhvRrHDNiPdzt7jtTLg3ZBR42VKr5pucqE&fm=jpg&w=400&fit=max&h=300`);
                    
                    if (!response.ok) {
                        throw new Error('Không thể lấy ảnh từ Unsplash');
                    }

                    const data = await response.json();
                    // Lấy URL ảnh, nếu không có kết quả thì trả về chuỗi rỗng
                    const imageUrl = data.results[0]?.urls?.regular || '';
                    return { id: product.id, url: imageUrl };

                } catch (error) {
                    // Không cần setApiError ở đây để tránh hiển thị nhiều lỗi
                    console.error('Lỗi khi tải ảnh cho:', product.name, error);
                    return { id: product.id, url: '' }; // Trả về url rỗng nếu có lỗi
                }
            });

            const imageResults = await Promise.all(imagePromises);
            
            const imageObject = imageResults.reduce((accumulator, current) => {
                accumulator[current.id] = current.url;
                return accumulator;
            }, {});

            setImages(imageObject);
            setLoading(false);
        };

        fetchImages();
    }, []); 

    return (
        <div className="home">
            <h2>Chào mừng bạn đến với trang chủ</h2>
            <p>Khám phá sản phẩm của chúng tôi:</p>
            {loading && <p>Đang tải ảnh...</p>}
            {apiError && <p className="error-message">{apiError}</p>}
            <div className="product-grid">
                {products.map((product) => (
                    <div key={product.id} className="product-card">
                        {/* Bây giờ images[product.id] sẽ hoạt động đúng */}
                        {images[product.id] ? (
                            <img src={images[product.id]} alt={product.name} className="product-image" />
                        ) : (
                            <div className="no-image">Không có ảnh</div>
                        )}
                        <h3>{product.name}</h3>
                        <p>Giá: {product.price}</p>
                        <Link to={`/products/${product.id}`}>Xem chi tiết</Link>
                    </div>
                ))}
            </div>
        </div>
    );
};

export default Home;