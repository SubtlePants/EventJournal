from enum import Enum

class AppointmentType(Enum):
    PRIMARYCARE = "Primary Care"
    NEUROLOGY = "Neurology"
    CARDIOLOGY = "Cardiology"
    EMERGENCYROOM = "Emergency Room"
    OTHER = "Other"

class EventType(Enum):
    APPOINTMENT= "Appointment"
    MEDCHANGE = "Med Change"
    SEIZURE = "Seizure"
    STRESS = "Stress"