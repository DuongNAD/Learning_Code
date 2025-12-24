package BTVN_Java2.OnTap;

public class Student {
    private String id;
    private String name;
    private String email;
    private String enrolledCourse;
    private boolean paymentStatus;
    public Student(String id, String name, String email, String enrolledCourse, boolean paymentStatus) {
        this.id = id;
        this.name = name;
        this.email = email;
        this.enrolledCourse = enrolledCourse;
        this.paymentStatus = paymentStatus;
    }
    public String getId() {
        return id;
    }
    public void setId(String id) {
        this.id = id;
    }
    public String getName() {
        return name;
    }
    public void setName(String name) {
        this.name = name;
    }
    public String getEmail() {
        return email;
    }
    public void setEmail(String email) {
        this.email = email;
    }
    public String getEnrolledCourse() {
        return enrolledCourse;
    }
    public void setEnrolledCourse(String enrolledCourse) {
        this.enrolledCourse = enrolledCourse;
    }
    public boolean isPaymentStatus() {
        return paymentStatus;
    }
    public void setPaymentStatus(boolean paymentStatus) {
        this.paymentStatus = paymentStatus;
    }

    public Student(){

    }

    public String toString(){
        return id+ " - " + name + " - " + email + " - " + enrolledCourse + " - " + paymentStatus;
    }
}
