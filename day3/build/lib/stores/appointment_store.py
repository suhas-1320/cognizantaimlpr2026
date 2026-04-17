from configuration.logger_configuration import configure_logger
from models.doctor import Doctor
from models.appointment import Appointment
from models.patient import Patient

logger = configure_logger() 

class AppointmentStore:
    def __init__(self):
        self.appointments = []
        self.doctors = []
        self.patients = []

    def add_appointment(self, appointment: Appointment):
        self.appointments.append(appointment)
        logger.info(f"Appointment added: {appointment}")

    def add_doctor(self, doctor: Doctor):
        self.doctors.append(doctor)
        logger.info(f"Doctor added: {doctor}")

    def add_patient(self, patient: Patient):
        self.patients.append(patient)
        logger.info(f"Patient added: {patient}")

    def get_appointments_by_patient_id(self, patient_id: int) -> list[Appointment]:
        return [appointment for appointment in self.appointments if appointment.patient_id == patient_id]

    def get_appointments_by_doctor_id(self, doctor_id: int) -> list[Appointment]:
        return [appointment for appointment in self.appointments if appointment.doctor_id == doctor_id]

    def get_doctor_by_id(self, doctor_id: int) -> Doctor:
        for doctor in self.doctors:
            if doctor.id == doctor_id:
                return doctor
        return None

    def get_patient_by_id(self, patient_id: int) -> Patient:
        for patient in self.patients:
            if patient.id == patient_id:
                return patient
        return None

    def __str__(self):
        return f"Appointment Store with {len(self.appointments)} appointments."