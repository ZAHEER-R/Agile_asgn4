class ICUAllocation:
    def __init__(self, available_beds):
        self.available_beds = available_beds
        self.patients = {}
        self.waiting_list = []

    def admit_patient(self, patient_id, age, oxygen_level, heart_rate, bp_systolic, conditions, is_emergency=False):
        if patient_id in self.patients:
            raise ValueError("Duplicate patient ID rejected.")
        if oxygen_level < 50 or oxygen_level > 100:
            raise ValueError("Invalid oxygen level.")
        if heart_rate < 30 or heart_rate > 200:
            raise ValueError("Invalid heart rate.")

        # Calculate Priority Score
        score = (100 - oxygen_level) * 2 + abs(75 - heart_rate)
        if "Severe" in conditions:
            score += 50

        # Classification
        if score > 80 or is_emergency:
            category = "CRITICAL"
        elif score > 50:
            category = "HIGH"
        elif score > 30:
            category = "MEDIUM"
        else:
            category = "LOW"

        self.patients[patient_id] = {"score": score, "category": category, "emergency": is_emergency}

        if is_emergency or self.available_beds > 0:
            if not is_emergency and self.available_beds > 0:
                self.available_beds -= 1
            return f"Admitted as {category}"
        else:
            self.waiting_list.append(patient_id)
            return "Placed on waiting list"
