
from pydantic import BaseModel, Field


class EnrollmentRequest(BaseModel):
    student_name: str = Field(
        min_length=1,
        max_length=100
    )

    course_id: int = Field(
        gt=0
    )


class EnrollmentResponse(BaseModel):
    enrollment_id: str
    student_name: str
    course_name: str
    message: str
