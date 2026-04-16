from configuration.logger_configuration import configure_logger
from models.doctor import Doctor
from models.appointment import Appointment
from models.patient import Patient
from exceptions.doctor_not_found_exception import DoctorNotFoundException

logger = configure_logger()

class DoctorStore:
    def __init__(self):
        self.doctors = []

    def add_doctor(self, doctor: Doctor):
        self.doctors.append(doctor)
        logger.info(f"Doctor added: {doctor}")

    def get_doctor_by_id(self, doctor_id: int) -> Doctor:
        for doctor in self.doctors:
            if doctor.id == doctor_id:
                return doctor
            raise DoctorNotFoundException(doctor_id)


    def get_doctors_by_specialization(self, specialization: str) -> list[Doctor]:
        return [doctor for doctor in self.doctors if doctor.specialization == specialization]
    
    def get_all_doctors(self) -> list[Doctor]:
        return self.doctors

    def __str__(self):
        return f"Doctor Store with {len(self.doctors)} doctors."