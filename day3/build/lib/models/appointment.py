class Appointment:
    def __init__(self, id, date, time, doctor, patient):
        self.appointment_id = id
        self.date = date
        self.time = time
        self.doctor = doctor
        self.patient = patient

    def __repr__(self):
        return (
            f"Appointment("
            f"id={self.appointment_id}, "
            f"date={self.date}, "
            f"time={self.time}, "
            f"doctor={self.doctor}, "
            f"patient={self.patient}"
            f")"
        )