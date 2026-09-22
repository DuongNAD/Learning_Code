# PRACTICAL EXAM – INTRODUCTION TO SOFTWARE ENGINEERING (SWE202c – Mock Exam 2026)

**Topic:** Smart Health Clinic Management System (SHCMS)  
**Time:** 120 minutes  
**Tools:** MS Word, Draw.io, MS Visio, Astah, Visual Paradigm, StarUML  
**Note:** Open book. Students are NOT allowed to use the Internet.

---

## I. CASE STUDY

MediCare Plus is a modern multi-specialty clinic with 15 departments and over 100 doctors. Currently, appointment scheduling and patient record management are handled manually via phone calls and paper files, leading to long waiting times, lost data, and difficulties in tracking long-term patient history. The administration has decided to commission a **Smart Health Clinic Management System (SHCMS)**, available on both Web and Mobile platforms.

The SHCMS is expected to serve four main user groups. **Patients** need to register accounts, search for doctors by specialty, book appointments in available time slots, receive email reminders, and view lab results/prescriptions online. If a time slot is full, patients can join a "Priority Waitlist"; if a booking is canceled, the system automatically promotes the first person on the list. **Doctors** need to view their daily appointment schedule, update electronic medical records (diagnoses, symptoms), issue e-prescriptions, and order laboratory tests. **Medical Staff (Receptionists)** are responsible for confirming appointments, performing patient check-ins, managing doctor shift schedules, and generating invoices. Finally, a **System Administrator** manages user accounts, configures system parameters, and ensures secure data backups.

From a technical standpoint, the clinic imposes several constraints. The system must remain responsive—handling at least **500 simultaneous booking requests** with a response time under **2 seconds**. Because medical data is highly sensitive, all stored data must use **AES-256 encryption** and communication must use **TLS 1.3**. The system must implement **Multi-Factor Authentication (MFA)** for doctors and admins. The platform must maintain **99.9% availability** (High Availability). The architecture should use **Microservices** to allow for horizontal scaling and easy integration of future modules (e.g., insurance claim processing).

---

## II. QUESTIONS

> Answer ALL questions based on the SHCMS case study. Use standard UML notation where required.

---

### Question 1: Software Development Model (2.0 points)

- Identify and justify the most appropriate software development model (SDLC) for the SHCMS project. Address: **(1.0 points)**
  - Stability of medical requirements and healthcare regulations.
  - The need for continuous feedback from doctors and clinical staff.
  - Specific risk factors (e.g., medical data privacy, system availability).
- Select ONE alternative SDLC model and compare it with your chosen model. Include at least two advantages and two disadvantages for each model in the context of this clinic system. **(1.0 points)**

---

### Question 2: UC Modeling (1.5 points)

- Identify ALL actors in the SHCMS. For each, state their primary goal and whether they are a primary or secondary actor. **(0.3 points)**
- List at least EIGHT use cases for the SHCMS. State the initiating actor(s) and a one-sentence goal for each. **(0.4 points)**
- Draw a complete UML Use Case Diagram for the SHCMS, including: **(0.8 points)**
  - System boundary, all identified actors, and major use cases.
  - At least ONE `<<include>>` relationship (provide rationale).
  - At least ONE `<<extend>>` relationship (provide rationale).

---

### Question 3: UC Specification (1.5 points)

Write a complete Use Case Specification for the use case **'Book Appointment'**. Fill in every field: Pre-condition, Post-condition, Basic Flow, Alternative Flow, and Exception Flow.

---

### Question 4: Non-Functional Requirements (1.0 points)

- Identify and classify at least FOUR NFRs from the case study into quality categories (Performance, Security, Availability, Scalability). Write one measurable acceptance criterion for each. **(0.6 points)**
- Identify TWO NFRs that may conflict with each other. Explain the conflict and propose a concrete trade-off strategy. **(0.4 points)**

---

### Question 5: Class Diagram (1.5 points)

- Identify at least SIX key domain classes for the SHCMS. Specify at least three attributes (with data types) and two methods for each. **(0.6 points)**
- Draw a complete UML Class Diagram including: **(0.9 points)**
  - Inheritance (Generalization) relationship (e.g., User as a base class).
  - At least TWO association relationships with multiplicity labels.
  - At least ONE aggregation OR composition relationship (with written justification).
  - At least ONE dependency relationship.

---

### Question 6: AI in Coding (1.0 points)

#### Scenario A — AppointmentService.java (0.5 points)

The following Java method is intended to book an appointment. It contains **THREE** logical or business logic bugs.

```java
public class AppointmentService {
    public boolean bookAppointment(Patient patient, Doctor doctor, Slot slot) {
        // 1. Check if doctor is already booked in this slot
        if (doctor.getSchedule().contains(slot)) { 
            return false; // Bug 1: Logic is inverted or incorrect
        }
        
        // 2. Check if patient already has another appointment in the same slot
        if (patient.getAppointments().stream().anyMatch(a -> a.getSlot().equals(slot))) {
            System.out.println("Patient busy");
            // Bug 2: Missing logical exit or incorrect return
        }

        // 3. Save appointment
        Appointment appt = new Appointment(patient, doctor, slot);
        appointmentRepo.save(appt); 
        // Bug 3: Missing state update for associated entities
        return true;
    }
}
```

**Tasks:**
- Write an AI Prompt for Code Review.
- Identify the 3 bugs based on logic.
- Write an AI Prompt to fix the bugs.

#### Scenario B — PatientDataService.java (0.5 points)

This method fetches medical history. It contains **TWO** logical bugs and **ONE** critical security vulnerability.

```java
public class PatientDataService {
    public List<Record> getMedicalHistory(String patientId, String authToken) {
        // Query database
        String sql = "SELECT * FROM records WHERE patient_id = " + patientId; // Security Bug
        List<Record> history = db.executeNativeQuery(sql);

        // Guard: Authorization token must be validated
        if (authToken == null) { // Logical Bug 1: Inverted logic
            return history; 
        }

        // Guard: Logic to check if history exists
        if (!history.isEmpty()) { // Logical Bug 2: Incorrect condition for returning data
            return null;
        }

        return history;
    }
}
```

**Tasks:**
- Write an AI Prompt for Security/Logic Review.
- Identify all 3 issues (naming the security vulnerability).
- Write an AI Prompt to fix the code using Parameterized Queries.

---

### Question 7: Testing (1.5 points)

- Map the four testing stages (Unit, Integration, System, Acceptance) to the SHCMS. State: What is tested, Who is responsible, and the Testing Type (Black-box/White-box). **(0.5 points)**
- Write THREE test cases for the **'View Lab Results'** use case, covering: **(1.0 points)**
  - Happy-path scenario.
  - Boundary / edge-case scenario.
  - Negative / error scenario (e.g., unauthorized access).

---

**END OF EXAM**
