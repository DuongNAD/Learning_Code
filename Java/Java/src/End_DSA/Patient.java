package End_DSA;
import java.util.Date;

public class Patient {
    private String patientId;
    private String name;
    private Date admissionDate;
    private String diagnosis;

    public Patient(String patientId, String name, String diagnosis) {
        this.patientId = patientId;
        this.name = name;
        this.admissionDate = new Date();
        this.diagnosis = diagnosis;
    }

    public String getPatientId() {
        return patientId;
    }

    public String getName() {
        return name;
    }

    public Date getAdmissionDate() {
        return admissionDate;
    }

    public String getDiagnosis() {
        return diagnosis;
    }

    public void setDiagnosis(String diagnosis) {
        this.diagnosis = diagnosis;
    }

    @Override
    public String toString() {
        return "Patient [ID=" + patientId + ", Tên=" + name + ", Chẩn đoán=" + diagnosis + "]";
    }
}