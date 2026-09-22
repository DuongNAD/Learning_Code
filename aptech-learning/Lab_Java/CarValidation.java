import java.util.Collections;

/**
 * CarValidation.java
 * Class xử lý logic kiểm tra điều kiện mua xe của khách hàng.
 */
public class CarValidation {

    public static Car checkCar(Car car, Color color, Day day, String price) throws ExceptionCar {
        
        // 1. Kiểm tra tồn tại dòng xe
        if (car == null) throw new ExceptionCar("Can't sell Car: Car break");

        // 2. Kiểm tra định dạng giá tiền (không được chứa chữ cái/ký tự đặc biệt)
        int parsedPrice;
        try {
            parsedPrice = Integer.parseInt(price.trim());
        } catch (Exception e) { // Bắt luôn cả trường hợp price bị null
            throw new ExceptionCar("Can't sell Car: Price is digit");
        }

        // 3. Kiểm tra tiền phải lớn hơn 0
        if (parsedPrice <= 0) throw new ExceptionCar("Can't sell Car: Price greater than zero");

        // 4. Kiểm tra ngày bán có khớp lịch hãng xe không
        if (day == null || !car.getDaySells().contains(day)) {
            throw new ExceptionCar("Can't sell Car: Car can't sell today");
        }

        // 5. Kiểm tra màu sắc (NO_COLOR luôn được phép mua)
        if (color == null || (color != Color.NO_COLOR && !car.getColors().contains(color))) {
            throw new ExceptionCar("Can't sell Car: color car does not exist");
        }

        // 6. Tính giá trị thực tế của chiếc xe mà khách chọn
        int actualPrice = 0;
        
        if (color == Color.NO_COLOR) {
            // Nếu không sơn (NO_COLOR) -> Lấy giá mẫu xe rẻ nhất trừ đi $100
            actualPrice = Collections.min(car.getPrices()) - 100;
        } else {
            // Nếu có màu -> Lấy giá đúng theo màu khách chọn
            int colorIndex = car.getColors().indexOf(color);
            actualPrice = car.getPrices().get(colorIndex);
        }

        // Kiểm tra tiền khách trả có đủ không
        if (parsedPrice < actualPrice) {
            throw new ExceptionCar("Can't sell Car: Not enough money (Need $" + actualPrice + ")");
        }

        return car;
    }
}
