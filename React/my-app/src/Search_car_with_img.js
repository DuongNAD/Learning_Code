import React, { useState, useEffect } from "react";

const SearchCar_with_Img = () => {
    const [car, setCar] = useState({
        brand: '',
        model: '',
        color: '',
        searchQuery: '',
    });

    const [searchError, setSearchError] = useState(false);
    const [images, setImages] = useState([]);
    const [loading, setLoading] = useState(false);
    const [apiError, setApiError] = useState('');
    const carBrands = {
        Toyota: ['Camry', 'Corolla', 'Rav4'],
        Audi: ['A4', 'A6', 'A8'],
        Lexus: ['RX', 'ES', 'GX'],
        Porsche: ['911', 'Cayenne', 'Panamera'],
        Mercedes: ['C-Class', 'E-Class', 'S-Class'],
    }

    useEffect(() => {
        if (car.brand && car.model) {
            setLoading(true);
            setApiError('');
            const query = `${car.brand} ${car.model}`.replace(/\s+/g, '+');
            fetch(
                `https://api.unsplash.com/search/photos?query=${query}&per_page=3&client_id=foCpbkzB8LhvRrHDNiPdzt7jtTLg3ZBR42VKr5pucqE&&fm=jpg&w=400&fit=max&h=300`
            )

                .then((Response) => {
                    if (!Response.ok) {
                        throw new Error('Khong the lay anh tu Unsplash');
                    }

                    return Response.json();
                })
                .then((data) => {
                    setImages(data.results.map((photo) => photo.urls.regular));
                    setLoading(false);
                })
                .catch((error) => {
                    setApiError('Loi khi tai anh: ' + error.message);
                    setImages([]);
                    setLoading(false);
                });
        }
        else {
            setImages([]);
        }
    }, [car.brand, car.model]);

    const handleSearchChange = (e) => {
        setCar((prev) => ({
            ...prev,
            searchQuery: e.target.value,
        }));
    };

    const searchBrand = () => {
        const normalizedQuery =
            car.searchQuery.trim().charAt(0).toUpperCase() +
            car.searchQuery.trim().slice(1).toLowerCase();
        if (carBrands[normalizedQuery]) {
            setCar((prev) => ({
                ...prev,
                brand: normalizedQuery,
                model: carBrands[normalizedQuery][0],
            }));
            setSearchError(false);
        }
        else {
            setCar((prev) => ({
                ...prev,
                brand: '',
                model: '',
            }));
            setSearchError(true);
            setImages([]);
        }
    };

    const changeModel = (model) => {
        setCar((prev) => ({
            ...prev,
            model,
        }));
    };

    const changeColor = () => {
        setCar((prev) => ({
            ...prev,
            color: prev.color === 'red' ? 'blue' : 'red',
        }));
    };

    const handleKeyPress = (e) => {
        if (e.key === 'Enter') {
            searchBrand();
        }
    };

    const models = carBrands[car.brand] || [];
    return (
        <div className="car-container">
            <h2>Thông tin xe</h2>
            <div className="search-section">
                <div className="search-group">
                    <label>Tìm kiếm hãng xe</label>
                    <input
                        type="text"
                        value={car.searchQuery}
                        onChange={handleSearchChange}
                        onKeyPress={handleKeyPress}
                        placeholder="Nhập tên hãng xe"
                        size={50}
                    />
                </div>
                <button onClick={searchBrand}>Tìm kiếm</button>
            </div>
            {searchError && <p className="error-message">Không tìm thấy hãng xe "{car.searchQuery}"</p>}

            {car.brand && (
                <>
                    <div className="model-selector">
                        <h3>Chọn mẫu xe</h3>
                        <div className="model-buttons">
                            {models.map((m) => (
                                <button
                                    key={m}
                                    onClick={() => changeModel(m)}
                                    className={m === car.model ? 'active' : ''}
                                >
                                    {m}
                                </button>
                            ))}
                        </div>
                    </div>
                    <div className="car-info">
                        <p>Thương hiệu: {car.brand}</p>
                        <p>Model: {car.model}</p>
                        <p>Màu sắc: {car.color || 'Chưa chọn'}</p>
                        <div className="car-display" style={{ backgroundColor: car.color }}>
                            <span>Xe màu {car.color}</span>
                        </div>
                        <button onClick={changeColor}>Đổi màu</button>
                    </div>
                    <div className="car-image-section">
                        <h3>Hình ảnh xe:</h3>
                        {loading && <p>Đang tải ảnh...</p>}
                        {apiError && <p className="error-message">{apiError}</p>}
                        
                        {!loading && !apiError && images.length === 0 && car.brand && (
                            <p>Không tìm thấy ảnh cho {car.brand} {car.model}</p>
                        )}
                        
                        <div className="image-grid">
                            {images.map((url, index) => (
                                <img
                                    key={index}
                                    src={url}
                                    alt={`${car.brand} ${car.model}`}
                                    className="car-image"
                                />
                            ))}
                        </div>
                    </div>
                </>
            )}
        </div>
    );
};

export default SearchCar_with_Img;