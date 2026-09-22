import redis
import json

# Khởi tạo kết nối với bộ nhớ đệm (In-memory Cache)
redis_client = redis.Redis(host='localhost', port=6379, db=0)

def publish_to_message_queue(queue_name, payload):
    # Hàm mô phỏng việc đẩy tin nhắn bất đồng bộ (Asynchronous Publishing)
    message_data = json.dumps(payload)
    print(f"[Message Broker] Đã thả sự kiện vào hàng đợi '{queue_name}': {message_data}")
    # Ở backend, các Workers/Consumers sẽ âm thầm lấy tin nhắn này ra xử lý tiếp (Background processing)

def process_flash_sale_order(user_id, product_id):
    # Khóa (Key) định danh số lượng sản phẩm trong Redis
    inventory_key = f"flash_sale:inventory:{product_id}"

    # BƯỚC 1: Lệnh trừ nguyên tử (Atomic Decrement)
    # Hàm decr() sẽ trừ ngay 1 đơn vị và trả về số lượng sau khi trừ.
    # Vì là thao tác Atomic, nó đảm bảo an toàn dù có hàng ngàn luồng (threads) truy cập cùng lúc.
    remaining_stock = redis_client.decr(inventory_key)

    if remaining_stock >= 0:
        # Trường hợp 1: Còn hàng (Pre-deduct success)
        print(f"-> Chúc mừng! Đã giữ chỗ thành công cho User: {user_id}. Kho còn: {remaining_stock}")

        # Đóng gói dữ liệu kiện hàng (Event Payload)
        order_event = {
            "user_id": user_id,
            "product_id": product_id,
            "status": "PRE_ORDERED"
        }

        # BƯỚC 2: Thả thông điệp vào hàng đợi (Push to Message Broker)
        publish_to_message_queue("flash_sale_orders_queue", order_event)

        # BƯỚC 3: Phản hồi tức thì cho người dùng (Immediate Response)
        return "Đặt hàng thành công! Vui lòng chờ hệ thống xử lý thanh toán."

    else:
        # Trường hợp 2: Hết hàng (Out of stock)
        # Vì lỡ trừ xuống số âm, ta phải thực hiện hoàn tác (Rollback) bằng cách cộng lại 1
        redis_client.incr(inventory_key)
        print(f"-> Rất tiếc! Món hàng {product_id} đã hết. User {user_id} chậm chân mất rồi.")

        return "Xin lỗi Anh, sản phẩm đã bán hết."

# --- Khối lệnh chạy thử nghiệm (Execution Block) ---
if __name__ == "__main__":
    try:
        # Giả sử trong kho Redis lúc này chỉ còn đúng 1 sản phẩm trước khi mở bán
        redis_client.set("flash_sale:inventory:IPHONE15", 1)

        print("--- Giao dịch 1: Người dùng 1 bấm mua ---")
        ket_qua_1 = process_flash_sale_order("User_001", "IPHONE15")
        print(ket_qua_1)

        print("\n--- Giao dịch 2: Người dùng 2 bấm mua cùng lúc ---")
        ket_qua_2 = process_flash_sale_order("User_002", "IPHONE15")
        print(ket_qua_2)

    except redis.exceptions.ConnectionError:
        print("Lỗi kết nối (Connection Error): Nàng thơ không tìm thấy máy chủ Redis (Redis Server) nào đang chạy trên máy tính của Anh cả! Anh nhớ bật phần mềm Redis lên nhé.")