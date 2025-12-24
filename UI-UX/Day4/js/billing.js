document.addEventListener('DOMContentLoaded', function() {
    // Lấy tất cả các nút "Pay"
    const payButtons = document.querySelectorAll('.btn.btn--pay');
    
    // Thêm sự kiện click cho mỗi nút
    payButtons.forEach(button => {
        button.addEventListener('click', function() {
            // Kiểm tra nếu nút đã được nhấn (đã có màu xanh) thì trở về trạng thái ban đầu
            if (this.classList.contains('active')) {
                this.classList.remove('active');
                this.style.backgroundColor = 'rgb(231,234,238)';
                this.style.color = 'rgb(100,116,139)';
                this.style.border = '2px solid rgb(231,234,238)';
            } else {
                // Nếu chưa thì chuyển sang màu xanh
                this.classList.add('active');
                this.style.backgroundColor = 'rgb(4, 120, 87)';
                this.style.color = 'white';
                this.style.border = '2px solid rgb(4, 120, 87)';
            }
        });
    });
});