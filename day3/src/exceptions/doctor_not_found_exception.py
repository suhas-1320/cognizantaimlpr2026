"""
Create Doctor not found exception
"""

class DoctorNotFoundException(Exception):
    """Exception raised when a doctor is not found in the system."""
    def __init__(self, doctor_id: int):
        super().__init__(f"Doctor with ID {doctor_id} not found.")
