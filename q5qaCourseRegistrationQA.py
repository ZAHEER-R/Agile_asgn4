import pytest
from CourseRegistration import CourseRegistration

def test_valid_registration():
    reg = CourseRegistration()
    credits = reg.register_courses("S001", ["Programming"], ["DBMS"])
    assert credits == 4

def test_missing_prerequisite():
    reg = CourseRegistration()
    with pytest.raises(ValueError, match="Missing prerequisite"):
        reg.register_courses("S002", [], ["DBMS"])
