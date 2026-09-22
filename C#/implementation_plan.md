# Nâng Cấp Hệ Thống Trí Nhớ Tiến Hóa (LearningLog)

Hệ thống VectorDB rút kinh nghiệm hiện tại đang hoạt động tốt về mặt cơ học, nhưng có hai lỗ hổng cực kỳ nghiêm trọng về mặt "Logic Huấn luyện" và "Tối ưu dung lượng" cần phải xử lý ngay.

## User Review Required

> [!IMPORTANT]
> Lỗi Logic Trầm Trọng: Trong code hiện tại của `LearningLog.ts`, khi tìm thấy một ký ức "THÀNH CÔNG" trong VectorDB, Prompt RAG lại đặt nó dưới tiêu đề *"Tuyệt đối không lặp lại nguyên nhân từ các thất bại dưới đây"*. 
> => Điều này khiến AI hiểu nhầm THÀNH CÔNG thành TỘI ĐỒ và liên tục né tránh những cách làm đúng đắn trong quá khứ! 

Xin ý kiến của bạn về việc phê duyệt các thay đổi dưới đây để vá lỗi và tối ưu hóa hệ thống học tập của LIVA.

## Proposed Changes

### Thay Đổi Cơ Chế Phân Loại Ký Ức (Axioms Separation)

#### [MODIFY] [LearningLog.ts](file:///e:/Project/LIVA/openclaw-gateway/src/evolution/LearningLog.ts)
- Viết lại hàm `getRelevantAxioms()`.
- Tách kết quả query từ LanceDB làm 2 danh sách phân biệt rạch ròi:
  - **<best_practices>** (Các pattern dẫn đến "Thành Công"): Hướng dẫn AI học hỏi và kế thừa.
  - **<anti_patterns>** (Các pattern "Thất Bại"): Nghiêm cấm LLM giẫm lại vết xe đổ.
- Tránh tình trạng gộp chung làm AI bị tiêm prompt mâu thuẫn.

### Tối Ưu Hóa Dung Lượng Bằng Cơ Chế Khử Trùng Lặp (Vector Deduplication)

#### [MODIFY] [LearningLog.ts](file:///e:/Project/LIVA/openclaw-gateway/src/evolution/LearningLog.ts)
- Sửa đổi hàm `recordAttempt()`: Trước khi chèn một bản ghi mới (Ví dụ: Thêm 1 lỗi Syntax gõ sai biến), hệ thống sẽ ném Vector đó đi so sánh (Search) với các log cũ.
- Áp dụng **Cosine Similarity Threshold (ngưỡng 0.95)**: Nếu lỗi mới giống lỗi cũ > 95% (Ví dụ: Lặp lại cùng một lỗi `TS2304: Cannot find name` nhiều lần), hệ thống sẽ từ chối lưu vào DB để không làm khối Context của RAG Rác thêm.
- Giúp LanceMemory luôn nhỏ gọn, sạch sẽ, chỉ lưu giữ những sai lầm mới ("Novel Errors").

## Verification Plan

### Automated Tests
- Reset tạm file tiến hoá ảo hoặc đọc lại LanceDB thông qua script Scratch. Kiểm tra xem các dòng Log mới có bị trùng lặp không.
- Mock một kết quả giả "Thành Công" vào log rồi gọi hàm `getRelevantAxioms` xem Text sinh ra có xếp nó vào vùng `<best_practices>` hay không.
