from CourseRegistration import CourseRegistrationSystem

def run_tests():
    print("--- RUNNING COURSE REGISTRATION QA TESTS ---")
    sys = CourseRegistrationSystem(max_credits=10)

    # 1. Valid Registration
    res = sys.register("S1", ["Programming", "Statistics"], ["DBMS", "ML"])
    print(f"[Test 1 Valid Reg] Status: {res['status']} | Total Credits: {res.get('total_credits')}")

    # 2. Missing Prerequisite
    res = sys.register("S2", [], ["DBMS"])
    print(f"[Test 2 Missing Prereq] Status: {res['status']} | Reason: {res.get('reason')}")

    # 3. Credit Limit Violation
    res = sys.register("S3", ["Programming", "Statistics", "Networking"], ["DBMS", "ML", "Cloud"]) # 4+3+3 = 10 (valid), adding more fails
    print(f"[Test 3 Credit Limit Check] Status: {res['status']}")

    # 4. Timetable Conflict
    res = sys.register("S4", ["Programming", "Data Structures"], ["DBMS", "AI"]) # Both MON_9AM
    print(f"[Test 4 Timetable Clash] Status: {res['status']} | Reason: {res.get('reason')}")

if __name__ == "__main__":
    run_tests()
