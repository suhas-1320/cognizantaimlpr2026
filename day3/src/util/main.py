import sys
import os

# ---------- Project Root ----------
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))
sys.path.append(project_root)

from src.models.person import Person
from conf.logger_configuration import setup_logger

# ---------- Logger ----------
logger = setup_logger("main.log")

# ---------- Create Person ----------
def create_person() -> Person:
    """Create and return a Person instance"""
    person = Person(
        adharCardNO="123456789012",
        mobileNo=9876543210
    )
    logger.info("Person created successfully")
    return person


if __name__ == "__main__":
    try:
        person = create_person()
        print(
            f"Person created: {person} | "
            f"Mobile: {person.mobileNo} | "
            f"Aadhaar: {person.adharCardNO}"
        )

        # ---------- Update mobile number ----------
        person.mobileNo = 1234567890
        logger.info("Mobile number updated successfully")

        print(
            f"Updated person details: {person} | "
            f"Mobile: {person.mobileNo} | "
            f"Aadhaar: {person.adharCardNO}"
        )

    except ValueError as e:
        logger.error(f"Error: {e}")
        print(f"Error updating person details: {e}")
