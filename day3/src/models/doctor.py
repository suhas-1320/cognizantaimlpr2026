"""This module defines the Doctor class, which represents a medical professional with a name, ID, and specialty."""


class Doctor:
    def __init__(self, name: str, id: int, specialty: str):
        self.name = name
        self.id = id
        self.specialty = specialty

    def __str__(self):
        return f"Doctor {self.name}, ID: {self.id}, Specialty: {self.specialty}"