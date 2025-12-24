import React from 'react';

// Component này chỉ có nhiệm vụ hiển thị, không cần state
function RentalDetails(props) {
  // Nhận dữ liệu từ props do component cha (RentalApp) truyền xuống
  const { brand, days, cost } = props;

  return (
    <div className="rental-details">
      <h2>Chi tiết thuê xe</h2>
      <p><strong>Hãng xe đã chọn:</strong> {brand}</p>
      <p><strong>Số ngày thuê:</strong> {days} ngày</p>
      <hr />
      <p className="total-cost">
        <strong>Tổng chi phí:</strong> ${cost}
      </p>
    </div>
  );
}

export default RentalDetails;