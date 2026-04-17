import sys
import os
import pytest
import csv

# ---------- Project Root ----------
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))
sys.path.append(project_root)

from src.models.patient import Patient

# ---------- CSV Path ----------
CSV_FILE_PATH = os.path.join(
    project_root,
    "tests",
    "patient.csv"
)

# ---------- CSV Loader ----------
def load_patient_test_data(csv_file_path):
    if not os.path.exists(csv_file_path):
        raise FileNotFoundError(f"CSV file not found: {csv_file_path}")

    data = []
    with open(csv_file_path, newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append((
                row["name"],
                int(row["id"]),
                row["dob"],
                row["disease"]
            ))
    return data

# ---------- Fixture ----------
@pytest.fixture
def initialize_patient():
    return Patient(
        name="Test Patient",
        id=1,
        dob="1990-01-01",
        disease="Flu"
    )

# ---------- Basic Test ----------
def test_patient_creation(initialize_patient):
    assert initialize_patient.name == "Test Patient"
    assert initialize_patient.id == 1
    assert initialize_patient.dob == "1990-01-01"
    assert initialize_patient.disease == "Flu"

# ---------- Parameterized Test Using CSV ----------
@pytest.mark.parametrize(
    "name, patient_id, dob, disease",
    load_patient_test_data(CSV_FILE_PATH)
)
def test_parameterized_patient_creation(name, patient_id, dob, disease):
    patient = Patient(name, patient_id, dob, disease)

    assert patient.name == name
    assert patient.id == patient_id
    assert patient.dob == dob
    assert patient.disease == disease
