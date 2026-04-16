from configuration.logger_configuration import configure_logger
from models.doctor import Doctor
from models.appointment import Appointment
from models.patient import Patient
from exceptions.patient_not_found_exception import PatientNotFoundException

logger = configure_logger()

class PatientStore:
    def __init__(self):
        self.patients = []
        self.doctors = []
        self.appointments = []

    def add_patient(self, patient: Patient):
        self.patients.append(patient)
        logger.info(f"Patient added: {patient}")
    

    def get_patient_by_id(self, patient_id: int) -> Patient:
        for patient in self.patients:
            if patient.id == patient_id:
                return patient
        raise PatientNotFoundException(patient_id)
        