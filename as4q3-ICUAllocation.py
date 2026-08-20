import pytest

# --- Development Module ---
class ICUAllocation:
    def __init__(self, available_beds):
        self.available_beds = available_beds
        self.patients = {}

    def admit_patient(self, patient_id, oxygen_level, heart_rate, is_emergency=False):
        if patient_id in self.patients: raise ValueError("Duplicate patient ID.")
        if not (50 <= oxygen_level <= 100): raise ValueError("Invalid oxygen level.")
        
        score = (100 - oxygen_level) * 2 + abs(75 - heart_rate)
        category = "CRITICAL" if score > 80 or is_emergency else ("HIGH" if score > 50 else "NORMAL")
        
        self.patients[patient_id] = {"category": category, "score": score}
        if is_emergency or self.available_beds > 0:
            if not is_emergency: self.available_beds -= 1
            return f"Admitted: {category}"
        return "Waiting List"

# --- QA Test Suite ---
def test_icu_allocation():
    icu = ICUAllocation(available_beds=1)
    res = icu.admit_patient("P001", 55, 130)
    assert "CRITICAL" in res
    with pytest.raises(ValueError, match="Duplicate patient ID"):
        icu.admit_patient("P001", 55, 130)
    with pytest.raises(ValueError, match="Invalid oxygen level"):
        icu.admit_patient("P002", 20, 80)
