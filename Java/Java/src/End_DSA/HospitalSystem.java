package End_DSA;

import java.util.*;

public class HospitalSystem {

    private DepartmentTree organizationTree;
    private LinkedList<Patient> receptionQueue;
    private HashMap<String, Patient> patientDatabase;
    private ArrayList<Doctor> doctorList;

    public HospitalSystem() {
        organizationTree = new DepartmentTree();
        receptionQueue = new LinkedList<>();
        patientDatabase = new HashMap<>();
        doctorList = new ArrayList<>();
    }

    public void demoOrganizationTree() {
        System.out.println("--- CÂY TỔ CHỨC ---");
        organizationTree.buildOrganizationTree();

        System.out.println("\n[Duyệt Pre-order]:");
        organizationTree.printPreOrder(organizationTree.getRoot());

        System.out.println("\n\n[Duyệt Post-order]:");
        organizationTree.printPostOrder(organizationTree.getRoot());

        System.out.println("\n\n[Duyệt Level-order (BFS)]:");
        organizationTree.printLevelOrder();

        System.out.println("\n\n[Tính tổng doanh thu (Đệ quy)]:");
        double totalRevenue = organizationTree.calculateTotalRevenue(organizationTree.getRoot());
        System.out.println("Tổng doanh thu: " + totalRevenue);
    }

    public void demoReceptionQueue() {
        System.out.println("\n--- HÀNG ĐỢI (QUEUE) ---");
        receptionQueue.clear();
        receptionQueue.add(new Patient("P001", "Bệnh nhân An", "Cảm cúm"));
        receptionQueue.add(new Patient("P002", "Bệnh nhân Bình", "Đau đầu"));
        receptionQueue.add(new Patient("P003", "Bệnh nhân Cường", "Sổ mũi"));
        System.out.println("Hiện có " + receptionQueue.size() + " bệnh nhân đang chờ.");

        while (!receptionQueue.isEmpty()) {
            Patient p = receptionQueue.removeFirst();
            System.out.println("Đang xử lý cho: " + p.getName());
        }
        System.out.println("Đã xử lý hết bệnh nhân.");
    }

    public void addPatient(Scanner scanner) {
        System.out.println("\n--- NHẬP BỆNH NHÂN (HASHMAP) ---");
        String luaChon = "";
        do {
            System.out.print("Nhập ID Bệnh nhân (ví dụ: BN101): ");
            String id = scanner.nextLine();

            if (patientDatabase.containsKey(id)) {
                System.out.println("Lỗi: ID này đã tồn tại.");
                continue;
            }

            System.out.print("Nhập Tên Bệnh nhân: ");
            String name = scanner.nextLine();
            System.out.print("Nhập Chẩn đoán: ");
            String diagnosis = scanner.nextLine();

            Patient p = new Patient(id, name, diagnosis);
            patientDatabase.put(p.getPatientId(), p);

            System.out.println("==> Đã thêm thành công: " + p);
            System.out.print("Bạn có muốn nhập tiếp? (y/n): ");
            luaChon = scanner.nextLine();

        } while (luaChon.equalsIgnoreCase("y"));
    }

    public void searchPatientHashMap(Scanner scanner) {
        System.out.println("\n--- TÌM KIẾM NHANH (HASHMAP) ---");
        if (patientDatabase.isEmpty()) {
            System.out.println("Lỗi: CSDL Bệnh nhân rỗng. Vui lòng nhập bệnh nhân trước (chức năng 3).");
            return;
        }

        System.out.print("Nhập ID Bệnh nhân cần tìm: ");
        String searchId = scanner.nextLine();

        Patient foundPatient = patientDatabase.get(searchId);

        if (foundPatient != null) {
            System.out.println("Tìm thấy: " + foundPatient);
        } else {
            System.out.println("Không tìm thấy bệnh nhân.");
        }
    }

    public void searchPatientBinary(Scanner scanner) {
        System.out.println("\n--- TÌM KIẾM (BINARY SEARCH) ---");
        if (patientDatabase.isEmpty()) {
            System.out.println("Lỗi: CSDL Bệnh nhân rỗng. Vui lòng nhập bệnh nhân trước (chức năng 3).");
            return;
        }

        ArrayList<Patient> patientList = new ArrayList<>(patientDatabase.values());
        bubbleSortPatientsById(patientList);

        System.out.println("Danh sách bệnh nhân (đã sắp xếp tự động để tìm kiếm):");
        for(Patient p : patientList) {
            System.out.println(" - " + p.getPatientId() + ": " + p.getName());
        }

        System.out.print("\nNhập ID Bệnh nhân cần tìm (Binary Search): ");
        String searchIdBinary = scanner.nextLine();

        Patient result = binarySearchPatient(patientList, searchIdBinary);
        if (result != null) {
            System.out.println("Kết quả: " + result);
        } else {
            System.out.println("Không tìm thấy bệnh nhân trong danh sách đã sắp xếp.");
        }
    }

    private void bubbleSortPatientsById(List<Patient> list) {
        int n = list.size();
        for (int i = 0; i < n - 1; i++) {
            for (int j = 0; j < n - 1 - i; j++) {
                if (list.get(j).getPatientId().compareTo(list.get(j + 1).getPatientId()) > 0) {
                    Patient temp = list.get(j);
                    list.set(j, list.get(j + 1));
                    list.set(j + 1, temp);
                }
            }
        }
    }

    private Patient binarySearchPatient(List<Patient> sortedList, String targetId) {
        int left = 0;
        int right = sortedList.size() - 1;

        while (left <= right) {
            int mid = left + (right - left) / 2;
            String midId = sortedList.get(mid).getPatientId();

            int comparison = midId.compareTo(targetId);

            if (comparison == 0) {
                return sortedList.get(mid);
            }

            if (comparison < 0) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        return null;
    }

    public void demoSortDoctors() {
        System.out.println("\n--- SẮP XẾP BÁC SĨ (BUBBLE SORT) ---");
        doctorList.clear();
        doctorList.add(new Doctor("BS01", "Bác sĩ Xoan", "Tim Mạch", 3000));
        doctorList.add(new Doctor("BS02", "Bác sĩ Yến", "Thần Kinh", 5000));
        doctorList.add(new Doctor("BS03", "Bác sĩ Tuấn", "Nội trú", 2500));
        doctorList.add(new Doctor("BS04", "Bác sĩ Vỹ", "Phẫu thuật", 4500));

        System.out.println("Danh sách (trước khi sắp xếp):");
        for (Doctor d : doctorList) {
            System.out.println(d);
        }

        bubbleSortDoctorsBySalaryDesc(doctorList);

        System.out.println("\nDanh sách (sau khi sắp xếp lương giảm dần):");
        for (Doctor d : doctorList) {
            System.out.println(d);
        }
    }

    private void bubbleSortDoctorsBySalaryDesc(List<Doctor> list) {
        int n = list.size();
        for (int i = 0; i < n - 1; i++) {
            for (int j = 0; j < n - 1 - i; j++) {
                if (list.get(j).getSalary() < list.get(j + 1).getSalary()) {
                    Doctor temp = list.get(j);
                    list.set(j, list.get(j + 1));
                    list.set(j + 1, temp);
                }
            }
        }
    }

    public void demoReverseString() {
        System.out.println("\n--- ĐẢO NGƯỢC CHUỖI (STACK) ---");
        String original = "HOSPITAL";

        Stack<Character> stack = new Stack<>();

        for (int i = 0; i < original.length(); i++) {
            stack.push(original.charAt(i));
        }

        String reversed = "";
        while (!stack.isEmpty()) {
            reversed = reversed + stack.pop();
        }

        System.out.println("Chuỗi gốc: " + original);
        System.out.println("Chuỗi đảo ngược (thành LATIPSOH): " + reversed);
    }

    public static void main(String[] args) {
        HospitalSystem hms = new HospitalSystem();
        Scanner scanner = new Scanner(System.in);
        int luaChon = 0;

        do {
            System.out.println("\n-----------------------------------------");
            System.out.println("=== HỆ THỐNG QUẢN LÝ BỆNH VIỆN ===");
            System.out.println("-----------------------------------------");
            System.out.println("1. Cây tổ chức");
            System.out.println("2. Hàng đợi tiếp nhận");
            System.out.println("3. Nhập Bệnh nhân");
            System.out.println("4. Tìm kiếm (HashMap)");
            System.out.println("5. Tìm kiếm (Binary Search)");
            System.out.println("6. Sắp xếp Bác sĩ");
            System.out.println("7. Đảo ngược chuỗi");
            System.out.println("0. Thoát");
            System.out.println("-----------------------------------------");
            System.out.print(">>> Mời chọn chức năng: ");

            try {
                luaChon = Integer.parseInt(scanner.nextLine());
            } catch (NumberFormatException e) {
                System.out.println("Lỗi: Vui lòng nhập một số hợp lệ.");
                continue;
            }

            switch (luaChon) {
                case 1:
                    hms.demoOrganizationTree();
                    break;
                case 2:
                    hms.demoReceptionQueue();
                    break;
                case 3:
                    hms.addPatient(scanner);
                    break;
                case 4:
                    hms.searchPatientHashMap(scanner);
                    break;
                case 5:
                    hms.searchPatientBinary(scanner);
                    break;
                case 6:
                    hms.demoSortDoctors();
                    break;
                case 7:
                    hms.demoReverseString();
                    break;
                case 0:
                    System.out.println("Cảm ơn đã sử dụng hệ thống. Tạm biệt!");
                    break;
                default:
                    System.out.println("Lỗi: Chức năng không tồn tại. Vui lòng chọn lại.");
            }

        } while (luaChon != 0);

        scanner.close();
    }
}