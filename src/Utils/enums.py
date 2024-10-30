from enum import Enum

class AppointmentType(Enum):
    PRIMARYCARE = "Primary Care"
    NEUROLOGY = "Neurology"
    CARDIOLOGY = "Cardiology"
    EMERGENCYROOM = "Emergency Room"
    OTHER = "Other"