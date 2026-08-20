class RideBookingSystem:
    RATES = {"Bike": 5, "Sedan": 10, "SUV": 15, "Premium": 25}
    CAPACITY = {"Bike": 1, "Sedan": 4, "SUV": 6, "Premium": 4}

    def process_booking(self, customer_id, pickup, drop, distance, passengers, vehicle_type, booking_hour, driver_available, promo_discount=0):
        if distance <= 0:
            return {"status": "REJECTED", "reason": "Invalid distance"}
        if vehicle_type not in self.RATES:
            return {"status": "REJECTED", "reason": "Invalid vehicle type"}
        if passengers <= 0 or passengers > self.CAPACITY[vehicle_type]:
            return {"status": "REJECTED", "reason": f"Passenger limit exceeded for {vehicle_type}"}
        if not (0 <= booking_hour <= 23):
            return {"status": "REJECTED", "reason": "Invalid booking time"}
        if not driver_available:
            return {"status": "REJECTED", "reason": "No driver available"}

        base_fare = 50.0
        distance_fare = distance * self.RATES[vehicle_type]
        
        # Surcharges
        peak_surcharge = (distance_fare * 0.25) if (8 <= booking_hour <= 10 or 17 <= booking_hour <= 20) else 0.0
        night_surcharge = (distance_fare * 0.20) if (22 <= booking_hour or booking_hour <= 5) else 0.0
        passenger_surcharge = 30.0 if passengers > 2 else 0.0

        total = base_fare + distance_fare + peak_surcharge + night_surcharge + passenger_surcharge
        discount = min(promo_discount, total * 0.5) # Max 50% discount capped
        final_fare = max(0.0, total - discount)

        return {
            "status": "ACCEPTED",
            "customer_id": customer_id,
            "vehicle": vehicle_type,
            "final_fare": round(final_fare, 2),
            "driver_assigned": "Driver_Allocated_#101"
        }

if __name__ == "__main__":
    system = RideBookingSystem()
    print(system.process_booking("C100", "A", "B", 12.5, 2, "Sedan", 18, True, 20))
