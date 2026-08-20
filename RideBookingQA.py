from RideBooking import RideBookingSystem

def run_tests():
    print("--- RUNNING RIDE BOOKING QA TESTS ---")
    sys = RideBookingSystem()

    # 1. Normal Booking
    res = sys.process_booking("C1", "A", "B", 10, 2, "Sedan", 12, True)
    print(f"[Test 1 Normal] Status: {res['status']} | Fare: {res.get('final_fare')}")

    # 2. Peak Hour Booking
    res_peak = sys.process_booking("C2", "A", "B", 10, 2, "Sedan", 9, True)
    print(f"[Test 2 Peak Hour] Status: {res_peak['status']} | Fare: {res_peak.get('final_fare')}")

    # 3. Night Booking
    res_night = sys.process_booking("C3", "A", "B", 10, 2, "Sedan", 23, True)
    print(f"[Test 3 Night Booking] Status: {res_night['status']} | Fare: {res_night.get('final_fare')}")

    # 4. Invalid Distance
    res = sys.process_booking("C4", "A", "B", 0, 1, "Bike", 12, True)
    print(f"[Test 4 Zero Distance] Status: {res['status']} | Reason: {res.get('reason')}")

    # 5. Invalid Passenger Count
    res = sys.process_booking("C5", "A", "B", 10, 3, "Bike", 12, True)
    print(f"[Test 5 Passenger Overflow] Status: {res['status']} | Reason: {res.get('reason')}")

    # 6. Unavailable Driver
    res = sys.process_booking("C6", "A", "B", 10, 1, "Sedan", 12, False)
    print(f"[Test 6 No Driver] Status: {res['status']} | Reason: {res.get('reason')}")

if __name__ == "__main__":
    run_tests()
