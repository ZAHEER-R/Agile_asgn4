class RideBooking:
    def __init__(self):
        self.valid_vehicles = ["Bike", "Sedan", "SUV", "Premium"]
        self.base_fares = {"Bike": 30, "Sedan": 50, "SUV": 80, "Premium": 120}

    def book_ride(self, customer_id, distance, passengers, vehicle_type, booking_time, driver_available):
        if distance <= 0:
            raise ValueError("Zero or negative distance not allowed.")
        if vehicle_type not in self.valid_vehicles:
            raise ValueError("Invalid vehicle type.")
        if not driver_available:
            raise ValueError("Unavailable vehicle/driver.")
        if passengers > 4 and vehicle_type == "Bike":
            raise ValueError("Excessive passengers for vehicle type.")

        base = self.base_fares[vehicle_type]
        distance_fare = distance * 12.0
        
        # Surcharges
        peak_surcharge = 50 if 8 <= booking_time <= 10 or 17 <= booking_time <= 20 else 0
        night_surcharge = 40 if booking_time >= 22 or booking_time <= 5 else 0
        passenger_surcharge = 20 if passengers > 2 else 0

        subtotal = base + distance_fare + peak_surcharge + night_surcharge + passenger_surcharge
        discount = subtotal * 0.15 if distance > 20 else 0
        final_fare = subtotal - discount

        return {
            "customer_id": customer_id,
            "final_fare": round(final_fare, 2),
            "assigned_driver": "Driver_Verified_01"
        }
