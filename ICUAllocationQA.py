from ICUAllocation import ICUManager

def run_tests():
    print("--- RUNNING ICU ALLOCATION QA TESTS ---")
    icu = ICUManager(available_beds=1)

    # 1. Critical Patient Allocation
    res, msg = icu.allocate_bed("P1", 70, 85, 130, "140/90", 98.6, ["Diabetes"])
    print(f"[Test 1 Critical Patient] Success: {res} | Output: {msg}")

    # 2. Bed Capacity Exceeded (Waiting List)
    res, msg = icu.allocate_bed("P2", 30, 98, 72, "120/80", 98.6, [])
    print(f"[Test 2 No Beds Available] Success: {res} | Output: {msg}")

    # 3. Duplicate Patient ID
    res, msg = icu.allocate_bed("P1", 25, 99, 70, "120/80", 98.6, [])
    print(f"[Test 3 Duplicate ID] Success: {res} | Output: {msg}")

    # 4. Invalid Vitals
    res, msg = icu.allocate_bed("P3", 40, -10, 70, "120/80", 98.6, [])
    print(f"[Test 4 Invalid Vitals] Success: {res} | Output: {msg}")

if __name__ == "__main__":
    run_tests()
