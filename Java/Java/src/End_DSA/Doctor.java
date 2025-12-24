package End_DSA;

public class Doctor {
    private String doctorId;
    private String name;
    private String specialty;
    private double salary;

    public Doctor(String doctorId, String name, String specialty, double salary) {
        this.doctorId = doctorId;
        this.name = name;
        this.specialty = specialty;
        this.salary = salary;
    }

    public String getDoctorId() {
        return doctorId;
    }

    public String getName() {
        return name;
    }

    public String getSpecialty() {
        return specialty;
    }

    public double getSalary() {
        return salary;
    }

    @Override
    public String toString() {
        return "Doctor [ID=" + doctorId + ", Tên=" + name + ", Lương=" + salary + "]";
    }
}