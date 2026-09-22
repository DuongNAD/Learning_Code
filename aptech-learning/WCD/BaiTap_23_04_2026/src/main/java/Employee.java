public class Employee {
    private int empId;
    private String fullName;
    private String department;
    private double baseSalary;
    private int yearsOfExperience;

    // Default Constructor
    public Employee() {
    }

    // Constructor có tham số
    public Employee(int empId, String fullName, String department, double baseSalary, int yearsOfExperience) {
        this.empId = empId;
        this.fullName = fullName;
        this.department = department;
        this.baseSalary = baseSalary;
        this.yearsOfExperience = yearsOfExperience;
    }

    // Getters và Setters
    public int getEmpId() {
        return empId;
    }

    public void setEmpId(int empId) {
        this.empId = empId;
    }

    public String getFullName() {
        return fullName;
    }

    public void setFullName(String fullName) {
        this.fullName = fullName;
    }

    public String getDepartment() {
        return department;
    }

    public void setDepartment(String department) {
        this.department = department;
    }

    public double getBaseSalary() {
        return baseSalary;
    }

    public void setBaseSalary(double baseSalary) {
        this.baseSalary = baseSalary;
    }

    public int getYearsOfExperience() {
        return yearsOfExperience;
    }

    public void setYearsOfExperience(int yearsOfExperience) {
        this.yearsOfExperience = yearsOfExperience;
    }
}
