"""Appointment model representing an appointment in the hospital system."""

from doctor import Doctor
from patient import Patient
from datetime import datetime 

class Appointment:
    def __init__(self, id: int, patient_id: int, doctor_id: int, date: datetime, time: datetime):
        self.appointment_id = id
        self.patient_id = patient_id
        self.doctor_id = doctor_id
        self.date = date
        self.time = time

    def __str__(self):
        return f"Appointment ID: {self.appointment_id}, Patient ID: {self.patient_id}, Doctor ID: {self.doctor_id}, Date: {self.date}, Time: {self.time}"  