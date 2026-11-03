
from fastapi import APIRouter, HTTPException

from schema import EnrollmentRequest, EnrollmentResponse
from services import (
    EnrollmentServices,
    DuplicateEnrollmentError,
    CourseNotFoundError
)
from logger_service import logger

router = APIRouter()
service = EnrollmentServices()


@router.get("/courses")
def get_courses():
    try:
        logger.info("Fetching all courses")

        result = service.get_all_courses()

        logger.info("Courses fetched successfully")
        return result

    except Exception:
        logger.exception("Failed to fetch courses")
        raise HTTPException(
            status_code=500,
            detail="Internal server error"
        )

@router.get("/enrollments")
def get_all_enrollments():
    try:
        logger.info("Fetching all enrollments")

        result = service.get_all_enrollments()

        logger.info("Enrollments fetched successfully")

        return result

    except Exception:
        logger.exception("Failed to fetch enrollments")

        raise HTTPException(
            status_code=500,
            detail="Internal server error"
        )


@router.post("/enrollments", response_model=EnrollmentResponse)
def enroll_student(request: EnrollmentRequest):
    try:
        logger.info("Enrollment request received")

        result = service.enroll_student(request)

        logger.info("Student enrolled successfully")
        return result

    except DuplicateEnrollmentError as e:
        logger.warning("Duplicate enrollment: %s", str(e))
        raise HTTPException(
            status_code=409,
            detail=str(e)
        )

    except CourseNotFoundError as e:
        logger.warning("Course not found: %s", str(e))
        raise HTTPException(
            status_code=404,
            detail=str(e)
        )

    except ValueError as e:
        logger.warning("Invalid enrollment request: %s", str(e))
        raise HTTPException(
            status_code=400,
            detail=str(e)
        )

    except Exception:
        logger.exception("Enrollment failed")
        raise HTTPException(
            status_code=500,
            detail="Internal server error"
        )

