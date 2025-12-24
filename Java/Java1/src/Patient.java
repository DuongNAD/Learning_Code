
public class Patient {
    private String patientId;
    private String name;
    private int age;
    private String diagnosis;

    // Constructor
    public Patient(String patientId, String name, int age, String diagnosis) {
        this.patientId = patientId;
        this.name = name;
        this.age = age;
        this.diagnosis = diagnosis;
    }

    // Getters
    public String getPatientId() {
        return patientId;
    }

    public String getName() {
        return name;
    }

    public int getAge() {
        return age;
    }

    public String getDiagnosis() {
        return diagnosis;
    }

    // Setters (Nếu Anh cần thay đổi thông tin)
    public void setDiagnosis(String diagnosis) {
        this.diagnosis = diagnosis;
    }

    // Phương thức toString() để in thông tin cho dễ
    @Override
    public String toString() {
        return "Patient{" +
                "id='" + patientId + '\'' +
                ", name='" + name + '\'' +
                ", age=" + age +
                ", diagnosis='" + diagnosis + '\'' +
                '}';
    }
}