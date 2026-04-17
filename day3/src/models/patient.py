"""Patient model representing a patient in the hospital system.
"""
import typing 
from datetime import date

class Patient:
    def __init__(self, name: str, id: int, dob: date, diesease: str):
        self.name = name
        self.id = id
        self.dob = dob
        self.diesease = diesease

    def __str__(self):
        return f"Patient {self.name}, ID: {self.id}, DOB: {self.dob}, Disease: {self.diesease}"