from datetime import datetime
from Utils.enums import AppointmentType, EventType

serializedDateFormatCode = "%d/%m/%y %H:%M"

def serializeDateTime(dateTime: datetime) -> str:
    return dateTime.strftime(serializedDateFormatCode)

def deserializeDateTime(dateString: str) -> datetime:
    return datetime.strptime(dateString, serializedDateFormatCode)

def deserializeAppointmentType(typeValue: str) -> AppointmentType:
    try:
        return AppointmentType(typeValue)
    except:
        raise TypeError("Unknown Appointment Type")

def deserializeEventType(typeValue: str) -> EventType:
    try:
        return EventType(typeValue)
    except:
        raise TypeError("Unkown Event Type")