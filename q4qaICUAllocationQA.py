import pytest
from ICUAllocation import ICUAllocation

def test_critical_patient():
    icu = ICUAllocation(available_beds=1)
    res = icu.admit_patient("P1", 45, 60, 140, 120, ["Severe"])
    assert "CRITICAL" in res

def test_duplicate_patient():
    icu = ICUAllocation(available_beds=2)
    icu.admit_patient("P2", 30, 90, 80, 110, [])
    with pytest.raises(ValueError, match="Duplicate patient ID"):
        icu.admit_patient("P2", 30, 90, 80, 110, [])
