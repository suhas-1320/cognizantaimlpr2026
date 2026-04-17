'''
Test cases for doctor store functionality
'''
import sys
import os
import pytest

# ---------- Project Root ----------
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))
sys.path.append(project_root)

from exceptions.doctor_not_found_exception import DoctorNotFoundException
from src.stores.doctor_store import DoctorStore

def test_doctor_not_found_exception():
    """Test that an exception is raised when doctor ID doesn't exist"""
    # Create a fresh doctor store instance
    store = DoctorStore()
    
    # Ensure the doctor store is empty (should be by default)
    assert len(store.doctors) == 0

    # Attempt to retrieve a doctor that does not exist
    with pytest.raises(Exception) as exc_info:
        store.get_doctor_by_id(999)  # Using an ID that is unlikely to exist
    
    # Verify it's the right type of exception
    assert isinstance(exc_info.value, DoctorNotFoundException)
    # Verify the exception message
    assert "Doctor with ID 999 not found" in str(exc_info.value)

   
