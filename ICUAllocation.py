class ICUManager:
    def __init__(self, available_beds=2):
        self.available_beds = available_beds
        self.allocated = {}
        self.waiting_list = []
        self.seen_patient_ids = set()

    def calculate_priority(self, age, oxygen, heart_rate, bp, temp, existing_conditions):
        score = 0
        if oxygen < 90: score += 40
        elif oxygen < 94: score += 20
        
        if heart_rate > 120 or heart_rate < 50: score += 25
        if age > 65: score += 15
        if len(existing_conditions) > 0: score += 10
        
        if score >= 60: return score, "CRITICAL"
        elif score >= 40: return score, "HIGH"
        elif score >= 20: return score, "MEDIUM"
        return score, "LOW"

    def allocate_bed(self, patient_id, age, oxygen, heart_rate, bp, temp, conditions, is_emergency=False):
        if patient_id in self.seen_patient_ids:
            return False, "REJECTED: Duplicate Patient ID"
        if not (0 <= oxygen <= 100) or not (30 <= heart_rate <= 220):
            return False, "REJECTED: Invalid Vitals"

        self.seen_patient_ids.add(patient_id)
        score, category = self.calculate_priority(age, oxygen, heart_rate, bp, temp, conditions)

        patient_data = {"id": patient_id, "score": score, "category": category}

        if is_emergency:
            category = "CRITICAL"
            patient_data["category"] = "CRITICAL (EMERGENCY)"

        if self.available_beds > 0:
            self.available_beds -= 1
            self.allocated[patient_id] = patient_data
            return True, f"Allocated ICU Bed. Priority: {patient_data['category']}"
        else:
            self.waiting_list.append(patient_data)
            self.waiting_list.sort(key=lambda x: x['score'], reverse=True)
            return False, f"No Beds Available. Placed on Waiting List (Rank: {len(self.waiting_list)})"

if __name__ == "__main__":
    icu = ICUManager(available_beds=1)
    print(icu.allocate_bed("P001", 70, 85, 130, "140/90", 98.6, ["Diabetes"]))
