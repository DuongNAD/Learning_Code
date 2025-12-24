import React from "react";
import { Link } from "react-router-dom";

const NotFound=  () =>{
    return (
        <div className="not-found">
            <h2>404 - Trang không tồn tại</h2>
            <p>Xin lỗi, trang bạn tìm kiếm không tồn tại.</p>
            <Link to="/">Trang chủ</Link>
        </div>
    );
};

export default NotFound;
