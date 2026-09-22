package Day1;

import java.util.Random;

public class BubbleSort {
    
    // Hàm in mảng
    public static void displayArray(String msg, int[] arr) {
        System.out.print(msg);
        for (int i = 0; i < arr.length; i++) {
            System.out.print(arr[i]);
            if (i < arr.length - 1) {
                System.out.print(" ");
            }
        }
        System.out.println("\n");
    }

    // Thuật toán Bubble Sort.
    // Hoạt động bằng cách liên tục lặp qua mảng cần sắp xếp,
    // so sánh từng cặp phần tử kề nhau (i và j (i+1)) và hoán đổi vị trí của chúng nếu phần tử trước lớn hơn phần tử sau.
    // Qua mỗi vòng lặp, phần tử lớn nhất sẽ bị đẩy lên cuối mảng.
    
    public static void bubbleSort(int[] arr) {
        int n = arr.length;
        
        for (int i = 0; i < n; i++) {
            boolean swapped = false; 

            for (int j = 0; j < n - i - 1; j++) {
                if (arr[j] > arr[j + 1]) {
                    int temp = arr[j];
                    arr[j] = arr[j + 1];
                    arr[j + 1] = temp;
                    
                    swapped = true;
                }
            }
            if (swapped == false) {
                break;
            }
        }
    }

    public static void main(String[] args) {
        System.out.print("Enter number of array: ");
        int number = Validation.checkInputInt();

        int[] arr = new int[number];
        Random random = new Random();

        for (int i = 0; i < number; i++) {
            arr[i] = random.nextInt(number);
        }

        displayArray("Unsorted array: ", arr);  
        bubbleSort(arr);
        displayArray("Sorted array: ", arr);
    }
}
