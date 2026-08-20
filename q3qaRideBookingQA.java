import pytest
from RideBooking import RideBooking

def test_normal_booking():
    rb = RideBooking()
    res = rb.book_ride("C001", 10, 2, "Sedan", 14, True)
    assert res["final_fare"] > 0
    assert res["assigned_driver"] is not None

def test_peak_hour_booking():
    rb = RideBooking()
    res_peak = rb.book_ride("C002", 10, 1, "Sedan", 9, True) # 9 AM peak hours
    res_normal = rb.book_ride("C003", 10, 1, "Sedan", 14, True) # 2 PM normal hours
    assert res_peak["final_fare"] > res_normal["final_fare"]

def test_night_booking():
    rb = RideBooking()
    res_night = rb.book_ride("C004", 10, 1, "Sedan", 23, True) # 11 PM night surcharge
    assert res_night["final_fare"] > 50

def test_invalid_distance():
    rb = RideBooking()
    with pytest.raises(ValueError, match="Zero or negative distance"):
        rb.book_ride("C005", 0, 1, "Sedan", 12, True)

def test_invalid_passenger_count():
    rb = RideBooking()
    with pytest.raises(ValueError, match="Excessive passengers"):
        rb.book_ride("C006", 5, 5, "Bike", 12, True)

def test_unavailable_driver():
    rb = RideBooking()
    with pytest.raises(ValueError, match="Unavailable vehicle/driver"):
        rb.book_ride("C007", 10, 1, "Sedan", 12, False)

def test_maximum_discount():
    rb = RideBooking()
    res = rb.book_ride("C008", 25, 2, "Sedan", 12, True) # Distance > 20 triggers discount
    assert res["final_fare"] > 0

def test_multiple_vehicle_types():
    rb = RideBooking()
    for vtype in ["Bike", "Sedan", "SUV", "Premium"]:
        res = rb.book_ride("C009", 10, 1, vtype, 12, True)
        assert res["final_fare"] > 0

def test_boundary_fare_values():
    rb = RideBooking()
    res = rb.book_ride("C010", 0.5, 1, "Bike", 12, True)
    assert res["final_fare"] > 0

def test_driver_allocation_logic():
    rb = RideBooking()
    res = rb.book_ride("C011", 12, 2, "SUV", 15, True)
    assert res["assigned_driver"] == "Driver_Verified_01"
