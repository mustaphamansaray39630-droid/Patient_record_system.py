"""
Patient Record System (Health domain)
Digital Public Good (DPG) aligned: open-source, inclusive, privacy-respecting, modular.

Privacy note: NO names, phone numbers, addresses or national IDs are stored.
Each patient is identified only by an anonymous ID (e.g. P001).
"""


class Patient:
    """Task 1 (Lecture 1): a class with attributes and methods."""

    total_patients = 0  # class attribute shared by all Patient objects

    def __init__(self, patient_id, age, gender, condition="None recorded"):
        self.patient_id = patient_id
        self.age = age
        self.gender = gender
        self.condition = condition
        # Tuple (extra marks): immutable record of (vaccine, date) pairs
        self.vaccinations = ()
        Patient.total_patients += 1

    # ---------- Instance methods (Task 3) ----------
    def update_record(self, condition):
        """Update the patient's recorded health condition."""
        self.condition = condition
        print(f"Record updated for {self.patient_id}.")

    def add_vaccination(self, vaccine, date):
        """Add a vaccination as a (vaccine, date) tuple."""
        self.vaccinations += ((vaccine, date),)
        print(f"{vaccine} recorded for {self.patient_id} on {date}.")

    def display_info(self):
        """Print the patient's information in a simple, readable way."""
        print(f"\nPatient ID : {self.patient_id}")
        print(f"Age        : {self.age}")
        print(f"Gender     : {self.gender}")
        print(f"Condition  : {self.condition}")
        if self.vaccinations:
            print("Vaccinations:")
            for vaccine, date in self.vaccinations:
                print(f"  - {vaccine} ({date})")
        else:
            print("Vaccinations: none recorded")

    # ---------- Class method (Task 3) ----------
    @classmethod
    def from_string(cls, data):
        """Create a Patient from text like 'P010,34,Female,Malaria'."""
        patient_id, age, gender, condition = data.split(",")
        return cls(patient_id.strip(), int(age), gender.strip(), condition.strip())

    @classmethod
    def get_total_patients(cls):
        return cls.total_patients

    # ---------- Static method (Task 3) ----------
    @staticmethod
    def is_valid_age(age):
        """Check that an age is realistic (no object data needed)."""
        return isinstance(age, int) and 0 <= age <= 120


class HealthClinic:
    """
    Second class. Uses ONE data structure (a dictionary) to store many
    Patient objects, with the patient ID as the key (Task 2).
    """

    def __init__(self, name):
        self.name = name
        self.patients = {}  # {patient_id: Patient object}

    def add_patient(self, patient):
        """Add a Patient object to the dictionary."""
        if not Patient.is_valid_age(patient.age):
            print(f"Invalid age for {patient.patient_id}. Not added.")
            return
        if patient.patient_id in self.patients:
            print(f"ID {patient.patient_id} already exists. Not added.")
            return
        self.patients[patient.patient_id] = patient
        print(f"Patient {patient.patient_id} added to {self.name}.")

    def find_patient(self, patient_id):
        return self.patients.get(patient_id)

    def display_all(self):
        """Loop through the dictionary and display every record."""
        print(f"\n=== Records at {self.name} ===")
        if not self.patients:
            print("No records yet.")
        for patient in self.patients.values():
            patient.display_info()


def demo():
    """Automatic demonstration of all features (object creation + interaction)."""
    clinic = HealthClinic("Freetown Community Clinic")

    p1 = Patient("P001", 28, "Female", "Malaria")
    p2 = Patient("P002", 5, "Male", "Healthy")
    p3 = Patient.from_string("P003,61,Female,Hypertension")  # class method
    p4 = Patient("P004", 150, "Male")  # invalid age on purpose

    for p in (p1, p2, p3, p4):
        clinic.add_patient(p)

    # Interaction between objects: clinic finds a patient, then the patient updates itself
    clinic.find_patient("P001").update_record("Recovered")
    clinic.find_patient("P002").add_vaccination("Measles", "2026-09-15")
    clinic.find_patient("P002").add_vaccination("Polio", "2026-10-01")

    clinic.display_all()
    print(f"\nTotal Patient objects created: {Patient.get_total_patients()}")
    print(f"Is age 45 valid? {Patient.is_valid_age(45)}")


def menu():
    """Simple text menu (clear prompts for accessibility)."""
    clinic = HealthClinic("Community Clinic")
    while True:
        print("\n1. Add patient  2. Display all  3. Update condition  4. Add vaccination  5. Exit")
        choice = input("Choose an option (1-5): ").strip()
        if choice == "1":
            try:
                pid = input("Anonymous ID (e.g. P001): ").strip()
                age = int(input("Age: "))
                gender = input("Gender: ").strip()
                condition = input("Condition: ").strip() or "None recorded"
                clinic.add_patient(Patient(pid, age, gender, condition))
            except ValueError:
                print("Please enter a number for age.")
        elif choice == "2":
            clinic.display_all()
        elif choice in ("3", "4"):
            patient = clinic.find_patient(input("Patient ID: ").strip())
            if not patient:
                print("Patient not found.")
            elif choice == "3":
                patient.update_record(input("New condition: ").strip())
            else:
                patient.add_vaccination(input("Vaccine: ").strip(), input("Date (YYYY-MM-DD): ").strip())
        elif choice == "5":
            print("Goodbye.")
            break
        else:
            print("Invalid option. Please choose 1 to 5.")


if __name__ == "__main__":
    mode = input("Type 'demo' for the demonstration or press Enter for the menu: ").strip().lower()
    demo() if mode == "demo" else menu()
