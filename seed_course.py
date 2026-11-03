
from database import courses_collection

initial_courses = [
    {"id": 103, "name": "Python Course"},
    {"id": 104, "name": "Java Course"}
]

for course in initial_courses:
    courses_collection.update_one(
        {"id": course["id"]},
        {"$setOnInsert": course},
        upsert=True
    )

print("Courses initialized successfully.")

for course in courses_collection.find({}, {"_id": 0}):
    print(course)
