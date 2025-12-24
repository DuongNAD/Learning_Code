import React, {useState, useEffect} from "react";

const SearchBook_with_Img = () => {
    const [allBooks, setAllBooks] = useState ({
        'Kinh dị': ['It', 'The Shining', 'Dracula'],
        'Phiêu lưu': ['The Hobbit', 'Treasure Island', 'Robinson Crusoe'],
        'Lãng mạn': ['Pride and Prejudice', 'The Notebook', 'Me Before You'],
        'Khoa học viễn tưởng': ['Dune', '1984', 'Fahrenheit 451']
    });

    const [book, setBook] = useState({
        category: '',
        title: '',
        searchQuery: '',
    });

    const[newBookTitle, setNewBookTitle] = useState('');
    const [newBookCategory, setNewBookCategory] = useState('');


    const [searchError, setSearchError] = useState(false);
    const [images, setImages] = useState([]);
    const [loading, setLoading] = useState(false);
    const [apiError, setApiError] = useState('');

    

    useEffect(()=>{
        if (book.category && book.title) {
            setLoading(true);
            setApiError('');
            const query = `${book.category} ${book.title}`.replace(/\s+/g, '+');
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
    }, [book.category, book.title]);

    const handleSearchChange = (e) => {
        setBook((prev) => ({
            ...prev,
            searchQuery: e.target.value,
        }));
    };

    const searchCategory = () => {
        const normalizedQuery =
            book.searchQuery.trim().charAt(0).toUpperCase() +
            book.searchQuery.trim().slice(1).toLowerCase();
        if (bookCategories[normalizedQuery]) { 
            setBook((prev) => ({
                ...prev,
                category: normalizedQuery,
                title: bookCategories[normalizedQuery][0],
            }));
            setSearchError(false);
        }
        else {
            setBook((prev) => ({
                ...prev,
                category: '',
                title: '',
            }));
            setSearchError(true);
            setImages([]);
        }
    };

    const changeTitle = (title) => {
        setBook((prev) => ({
            ...prev,
            title,
        }));
    };

    const handleKeyPress = (e) => {
        if (e.key === 'Enter') {
            searchCategory();
        }
    };

    const titles = bookCategories[book.category] || [];
    return (
        <div className="book-container">
            <h2>Thông tin sách</h2>
            <div className="search-section">
                <div className="search-group">
                    <label>Tìm kiếm thể loại</label>
                    <input
                        type="text"
                        value={book.searchQuery}
                        onChange={handleSearchChange}
                        onKeyPress={handleKeyPress} 
                        placeholder="Nhập tên thể loại"
                        size={50}
                    />
                </div>
                <button onClick={searchCategory}>Tìm kiếm</button>
            </div>
            {searchError && <p className="error-message">Không tìm thấy thể loại "{book.searchQuery}"</p>}

            {book.category && (
                <>
                    <div className="title-selector">
                        <h3>Chọn tên sách</h3>
                        <div className="title-buttons">
                            {titles.map((t) => (
                                <button
                                    key={t}
                                    onClick={() => changeTitle(t)}
                                    className={t === book.title ? 'active' : ''}
                                >
                                    {t}
                                </button>
                            ))}
                        </div>
                    </div>
                    <div className="book-info">
                        <p>Thể loại: {book.category}</p>
                        <p>Tiêu đề: {book.title}</p>
                        <div className="book-image-section">
                            <h3>Hình ảnh sách:</h3>
                            {loading && <p>Đang tải ảnh...</p>}
                            {apiError && <p className="error-message">{apiError}</p>}
                            {!loading && !apiError && images.length === 0 && book.category && (
                                <p>Không tìm thấy ảnh cho {book.category} {book.title}</p>
                            )}
                            <div className="image-grid">
                                {images.map((url, index) => (
                                    <img
                                        key={index}
                                        src={url}
                                        alt={`${book.category} ${book.title}`}
                                        className="book-image"
                                    />
                                ))}
                            </div>
                        </div>
                    </div>
                </>
            )}
        </div>
    );
};

export default SearchBook_with_Img;