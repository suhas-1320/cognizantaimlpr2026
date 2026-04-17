
import sys
import os
from datetime import date, datetime

# Get absolute paths for day3 root and its src folder
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))
SRC_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../"))

for path in (ROOT_DIR, SRC_DIR):
    if path not in sys.path:
        sys.path.append(path)

from configuration.logger_configuration import configure_logger
from stores.patient_store import PatientStore
from stores.doctor_store import DoctorStore
from stores.appointment_store import AppointmentStore
from models.patient import Patient
from models.doctor import Doctor
from models.appointment import Appointment
from exceptions.patient_not_found_exception import PatientNotFoundException
from exceptions.doctor_not_found_exception import DoctorNotFoundException

"""
    Entry point for the application. This module initializes the application and runs the main logic.
"""

logger = configure_logger()
patient_store = PatientStore()
doctor_store = DoctorStore()
appointment_store = AppointmentStore()


def create_patient(patient_id: int, name: str, dob: date, disease: str) -> Patient:
    patient = Patient(name=name, id=patient_id, dob=dob, diesease=disease)
    patient_store.add_patient(patient)
    logger.info("create_patient: %s", patient)
    return patient


def read_patient(patient_id: int) -> Patient:
    patient = patient_store.get_patient_by_id(patient_id)
    logger.info("read_patient: %s", patient)
    return patient


def update_patient(patient_id: int, name: str | None = None, dob: date | None = None, disease: str | None = None) -> Patient:
    patient = patient_store.get_patient_by_id(patient_id)
    fields_changed = []

    if name is not None:
        patient.name = name
        fields_changed.append("name")
    if dob is not None:
        patient.dob = dob
        fields_changed.append("dob")
    if disease is not None:
        patient.diesease = disease
        fields_changed.append("disease")

    logger.info("update_patient id=%s fields=%s", patient_id, fields_changed or "none")
    return patient


def delete_patient(patient_id: int) -> Patient:
    patient = patient_store.get_patient_by_id(patient_id)
    patient_store.patients = [p for p in patient_store.patients if p.id != patient_id]
    logger.info("delete_patient: %s", patient)
    return patient


def create_doctor(doctor_id: int, name: str, specialty: str) -> Doctor:
    doctor = Doctor(name=name, id=doctor_id, specialty=specialty)
    doctor_store.add_doctor(doctor)
    logger.info("create_doctor: %s", doctor)
    return doctor


def read_doctor(doctor_id: int) -> Doctor:
    doctor = doctor_store.get_doctor_by_id(doctor_id)
    logger.info("read_doctor: %s", doctor)
    return doctor


def update_doctor(doctor_id: int, name: str | None = None, specialty: str | None = None) -> Doctor:
    doctor = doctor_store.get_doctor_by_id(doctor_id)
    fields_changed = []

    if name is not None:
        doctor.name = name
        fields_changed.append("name")
    if specialty is not None:
        doctor.specialty = specialty
        fields_changed.append("specialty")

    logger.info("update_doctor id=%s fields=%s", doctor_id, fields_changed or "none")
    return doctor


def delete_doctor(doctor_id: int) -> Doctor:
    doctor = doctor_store.get_doctor_by_id(doctor_id)
    doctor_store.doctors = [d for d in doctor_store.doctors if d.id != doctor_id]
    logger.info("delete_doctor: %s", doctor)
    return doctor


def create_appointment(appointment_id: int, patient_id: int, doctor_id: int, appointment_date: datetime, appointment_time: datetime) -> Appointment:
    read_patient(patient_id)
    read_doctor(doctor_id)
    appointment = Appointment(id=appointment_id, patient_id=patient_id, doctor_id=doctor_id, date=appointment_date, time=appointment_time)
    appointment_store.add_appointment(appointment)
    logger.info("create_appointment: %s", appointment)
    return appointment


def list_appointments_by_patient(patient_id: int) -> list[Appointment]:
    appointments = appointment_store.get_appointments_by_patient_id(patient_id)
    logger.info("list_appointments_by_patient id=%s count=%s", patient_id, len(appointments))
    return appointments


def list_appointments_by_doctor(doctor_id: int) -> list[Appointment]:
    appointments = appointment_store.get_appointments_by_doctor_id(doctor_id)
    logger.info("list_appointments_by_doctor id=%s count=%s", doctor_id, len(appointments))
    return appointments


def cancel_appointment(appointment_id: int) -> Appointment:
    appointment = next((appt for appt in appointment_store.appointments if appt.appointment_id == appointment_id), None)
    if appointment is None:
        raise ValueError(f"Appointment with ID {appointment_id} not found.")

    appointment_store.appointments = [appt for appt in appointment_store.appointments if appt.appointment_id != appointment_id]
    logger.info("cancel_appointment: %s", appointment)
    return appointment


def run():
    logger.info("Running the application...")

    alice = create_patient(1, "Alice Smith", date(1990, 3, 15), "Flu")
    dr_brown = create_doctor(1, "Dr. Brown", "Cardiology")
    appointment = create_appointment(1, alice.id, dr_brown.id, datetime(2026, 4, 17), datetime(2026, 4, 17, 14, 0))

    read_patient(alice.id)
    update_patient(alice.id, disease="Recovered")
    list_appointments_by_patient(alice.id)
    cancel_appointment(appointment.appointment_id)

    logger.info("Application finished successfully.")


# handle entry point for the application
if __name__ == "__main__":
    run()