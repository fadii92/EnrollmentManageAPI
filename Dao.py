
import re

from database import courses_collection, enrollments_collection


class EnrollmentDAO:

    def get_all_courses(self):
        return list(
            courses_collection.find({}, {"_id": 0})
        )

    def find_course(self, course_id: int):
        return courses_collection.find_one({
            "id": course_id
        })

    def add_course(self, course_id: int, name: str):
        course = {
            "id": course_id,
            "name": name
        }

        courses_collection.insert_one(course)
        return course

    def get_all_enrollments(self):
        enrollments = enrollments_collection.find()
        result = []

        for enrollment in enrollments:
            result.append({
                "enrollment_id": str(enrollment["_id"]),
                "student_name": enrollment["student_name"],
                "course_id": enrollment["course_id"]
            })

        return result

    def find_enrollment(self, student_name, course_id):
        return enrollments_collection.find_one({
            "student_name": {
                "$regex": "^" + re.escape(student_name.strip()) + "$",
                "$options": "i"
            },
            "course_id": course_id
        })

    def save(self, student_name, course_id):
        enrollment = {
            "student_name": student_name,
            "course_id": course_id
        }

        result = enrollments_collection.insert_one(enrollment)

        enrollment["enrollment_id"] = str(result.inserted_id)

        return enrollment
