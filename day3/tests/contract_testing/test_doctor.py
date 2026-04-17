import sys
import os
import pytest
import csv

# ---------- Project Root ----------
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))
sys.path.append(project_root)

from src.models.doctor import Doctor

# ---------- CSV Path ----------
CSV_FILE_PATH = os.path.join(
    project_root,
    "tests",
    "doctor.csv"
)

# ---------- CSV Loader ----------
def load_doctor_test_data(csv_file_path):
    if not os.path.exists(csv_file_path):
        raise FileNotFoundError(f"CSV file not found: {csv_file_path}")

    data = []
    with open(csv_file_path, newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append((
                row["name"],
                int(row["id"]),                 # ✅ matches CSV
                row["specialty"]           # ✅ matches CSV
            ))
    return data

# ---------- Fixture ----------
@pytest.fixture
def initialize_doctor():
    return Doctor(
        name="Dr. Smith",
        id=1,
        specialty="Cardiology"
    )

def test_doctor_creation(initialize_doctor):
    assert initialize_doctor.name == "Dr. Smith"
    assert initialize_doctor.id == 1
    assert initialize_doctor.specialty == "Cardiology"

# ---------- Parameterized Test Using CSV ----------
@pytest.mark.parametrize(
    "name, doctor_id, specialty",
    load_doctor_test_data(CSV_FILE_PATH)
)
def test_parameterized_doctor_creation(name, doctor_id, specialty):
    doctor = Doctor(name, doctor_id, specialty)

    assert doctor.name == name
    assert doctor.id == doctor_id
    assert doctor.specialty == specialty