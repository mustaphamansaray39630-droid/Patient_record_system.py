# Patient Record System (Health)

A Python OOP program that manages anonymous patient records for a small community clinic.
Built for the Limkokwing University Sierra Leone Python assignment (Semester 03, Sep 2026 to Feb 2027).

## How to run

```
python patient_record_system.py
```
Type `demo` for an automatic demonstration, or press Enter for the interactive menu.

## Features and how they meet the tasks

- **Task 1 (OOP basics):** Two classes, `Patient` (attributes: patient_id, age, gender, condition, vaccinations) and `HealthClinic`. Objects interact: the clinic finds a patient, then the patient updates itself.
- **Task 2 (data structure):** One dictionary in `HealthClinic.patients` stores Patient objects with the patient ID as the key. `add_patient()` and `display_all()` add and display records. A tuple is also used for vaccinations (optional extra marks).
- **Task 3 (methods):**
  - Instance methods: `update_record()`, `add_vaccination()`, `display_info()`
  - Class methods: `from_string()`, `get_total_patients()`
  - Static method: `is_valid_age()`

## DPG standards

- **Open-source:** Hosted publicly on GitHub, plain Python with no paid dependencies.
- **Inclusive and accessible:** Simple numbered text menu, clear prompts and error messages, runs on low-end computers and offline.
- **Privacy-respecting:** No names, contacts, addresses or national IDs are stored, only an anonymous ID, age, gender and a general condition.
- **Modular and reusable:** `Patient` and `HealthClinic` are separate classes that can be reused in other health tools (e.g. a vaccination tracker).

## Sample output (demo mode)

```
Patient P001 added to Freetown Community Clinic.
Patient P002 added to Freetown Community Clinic.
Patient P003 added to Freetown Community Clinic.
Invalid age for P004. Not added.
Record updated for P001.
Measles recorded for P002 on 2026-09-15.
Polio recorded for P002 on 2026-10-01.

=== Records at Freetown Community Clinic ===

Patient ID : P001
Age        : 28
Gender     : Female
Condition  : Recovered
Vaccinations: none recorded

Patient ID : P002
Age        : 5
Gender     : Male
Condition  : Healthy
Vaccinations:
  - Measles (2026-09-15)
  - Polio (2026-10-01)

Patient ID : P003
Age        : 61
Gender     : Female
Condition  : Hypertension
Vaccinations: none recorded

Total Patient objects created: 4
Is age 45 valid? True
```

## Author

Mustapha Mansaray BBIT1101

## License

MIT License (open-source).
