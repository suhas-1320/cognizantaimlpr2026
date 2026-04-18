class Patient:
    def __init__(self, id, name, dob, ailment):
        self.id = id
        self.name = name
        self.dob = dob
        self.ailment = ailment

    def __repr__(self):
        return (
            f"Patient(id={self.id}, name={self.name}, "
            f"dob={self.dob}, ailment={self.ailment})"
        )