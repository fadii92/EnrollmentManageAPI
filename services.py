
from Dao import EnrollmentDAO


class DuplicateEnrollmentError(Exception):
    pass


class CourseNotFoundError(Exception):
    pass


class EnrollmentServices:

    def __init__(self):
        self.dao = EnrollmentDAO()

    def get_all_courses(self):
        return self.dao.get_all_courses()

    def enroll_student(self, request):
        student_name = request.student_name.strip()
        course_id = request.course_id

        if not student_name:
            raise ValueError("Student name cannot be empty")

        course = self.dao.find_course(course_id)

        if course is None:
            raise CourseNotFoundError("Course Not Found")

        existing = self.dao.find_enrollment(
            student_name,
            course_id
        )

        if existing:
            raise DuplicateEnrollmentError(
                "Already enrolled in this course."
            )
        enrollment = self.dao.save(
            student_name,
            course_id
        )

        return {
            "enrollment_id": enrollment["enrollment_id"],
            "student_name": enrollment["student_name"],
            "course_name": course["name"],
            "message": "Enrollment Successful"
        }

    def get_all_enrollments(self):
        return self.dao.get_all_enrollments()
