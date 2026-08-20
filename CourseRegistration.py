class CourseRegistrationSystem:
    COURSES = {
        "DBMS": {"credits": 4, "prereq": "Programming", "slot": "MON_9AM"},
        "AI": {"credits": 4, "prereq": "Data Structures", "slot": "MON_9AM"}, # Conflict with DBMS
        "ML": {"credits": 3, "prereq": "Statistics", "slot": "TUE_11AM"},
        "Cloud": {"credits": 3, "prereq": "Networking", "slot": "WED_2PM"}
    }

    def __init__(self, max_credits=10):
        self.max_credits = max_credits

    def register(self, student_id, completed_prereqs, course_list):
        registered_courses = []
        total_credits = 0
        occupied_slots = set()

        if len(course_list) != len(set(course_list)):
            return {"status": "FAILED", "reason": "Duplicate courses in request"}

        for course in course_list:
            if course not in self.COURSES:
                return {"status": "FAILED", "reason": f"Invalid course: {course}"}

            cdata = self.COURSES[course]

            # Prerequisite Check
            if cdata["prereq"] and cdata["prereq"] not in completed_prereqs:
                return {"status": "FAILED", "reason": f"Missing Prerequisite '{cdata['prereq']}' for {course}"}

            # Credit Limit Check
            if total_credits + cdata["credits"] > self.max_credits:
                return {"status": "FAILED", "reason": f"Credit limit exceeded when adding {course}"}

            # Timetable Conflict Check
            if cdata["slot"] in occupied_slots:
                return {"status": "FAILED", "reason": f"Timetable clash detected for {course} at {cdata['slot']}"}

            occupied_slots.add(cdata["slot"])
            total_credits += cdata["credits"]
            registered_courses.append(course)

        return {
            "status": "SUCCESS",
            "student_id": student_id,
            "registered_courses": registered_courses,
            "total_credits": total_credits
        }

if __name__ == "__main__":
    reg = CourseRegistrationSystem()
    print(reg.register("ST101", ["Programming", "Statistics"], ["DBMS", "ML"]))
