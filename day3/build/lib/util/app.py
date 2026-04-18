import sys
import os
from faker import Faker

# Add project root to Python path
project_root = os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..', '..')
)
sys.path.append(project_root)

from configuration.logger_configuration import configure_logger
from src.models.doctor import Doctor
from src.models.patient import Patient
from src.models.appointment import Appointment
from src.stores.patient_store import PatientStore
from src.stores.doctor_store import DoctorStore
from src.stores.appointment_store import AppointmentStore

"""
Entry point for the application.
"""

doctor_logger = configure_logger()
patient_logger = configure_logger()
appointment_logger = configure_logger()
app_logger = configure_logger()

fake = Faker()

doctorstore = DoctorStore()
patientstore = PatientStore()
appointmentstore = AppointmentStore()

doctor_id = 0
patient_id = 0


def doctor_app():
    doctor_logger.info("app doctor agent is running...")
    doctor = Doctor(
        id=fake.random_int(),
        name=fake.name(),
        specialization=fake.job()
    )
    doctorstore.add_doctor(doctor)
    global doctor_id
    doctor_id = doctor.id
    doctor_logger.info(f"Doctor added: {doctor}")


def patient_app():
    patient_logger.info("app patient agent is running...")
    patient = Patient(
        id=fake.random_int(),
        name=fake.name(),
        dob=fake.date_of_birth(),
        ailment=fake.sentence()
    )
    patientstore.add_patient(patient)
    global patient_id
    patient_id = patient.id
    patient_logger.info(f"Patient added: {patient}")


def appointment_app():
    appointment_logger.info("app appointment agent is running...")
    appointment = Appointment(
        id=fake.random_int(),
        date=fake.date(),
        time=fake.time(),
        doctor=doctorstore.get_doctor_by_id(doctor_id),
        patient=patientstore.get_patient_by_id(patient_id)
    )
    appointmentstore.add_appointment(appointment)
    appointment_logger.info(f"Appointment added: {appointment}")


if __name__ == "__main__":
    app_logger.debug("Starting the application...")
    doctor_app()
    patient_app()
    appointment_app()