"""Create Patient not found exception
"""

class PatientNotFoundException(Exception):
    """Exception raised when a patient is not found in the system."""
    def __init__(self, patient_id: int):
        super().__init__(f"Patient with ID {patient_id} not found.")