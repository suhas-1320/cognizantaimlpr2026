class Doctor:
    def __init__(self, id, name, specialization):
        self.id = id
        self.name = name
        self.specialization = specialization

    def __repr__(self):
        return f"Doctor(id={self.id}, name={self.name}, specialization={self.specialization})"