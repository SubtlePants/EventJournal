from datetime import datetime
from Utils.enums import AppointmentType, EventType
from Events.appointmentEvent import AppointmentEvent
from Events.medChangeEvent import MedChangeEvent
from Events.seizureEvent import SeizureEvent
from Events.event import Event
from Events.stressevent import StressEvent


def serializedEventFactory(serializedEvent: dict[str, str]) -> Event:
    match serializedEvent["eventType"]:
        case EventType.SEIZURE.value:
            return SeizureEvent(date=datetime.min, description="", temporalSymptoms=False, duration=-1).deserialize(serializedEvent)
                    
        case EventType.APPOINTMENT.value:
            return AppointmentEvent(date=datetime.min, description="", appointmentType=AppointmentType.OTHER, reason="") .deserialize(serializedEvent)
        
        case EventType.MEDCHANGE.value:
            return MedChangeEvent(date=datetime.min, description="", medName="", oldDosage="", newDosage="").deserialize(serializedEvent)
        
        case EventType.STRESS.value:
            return StressEvent(description="", date=datetime.min).deserialize(serializedEvent)
        
        case _:
            raise TypeError("Invalid Event Type")