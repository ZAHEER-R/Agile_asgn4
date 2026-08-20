class CourseRegistration:
    def __init__(self):
        self.course_catalog = {
            "DBMS": {"credits": 4, "prereq": "Programming", "capacity": 2},
            "AI": {"credits": 4, "prereq": "Data Structures", "capacity": 2}
        }
        self.student_records = {}

    def register_courses(self, student_id, completed_courses, selected_courses, max_credits=10):
        total_credits = 0
        for course in selected_courses:
            if course not in self.course_catalog:
                raise ValueError(f"Invalid course: {course}")
            details = self.course_catalog[course]
            if details["prereq"] and details["prereq"] not in completed_courses:
                raise ValueError(f"Missing prerequisite for {course}")
            total_credits += details["credits"]

        if total_credits > max_credits:
            raise ValueError("Credit-limit violation.")
        
        self.student_records[student_id] = selected_courses
        return total_credits
