from datetime import datetime
from Utils.enums import AppointmentType, EventType
from Events.appointmentEvent import AppointmentEvent
from Events.medChangeEvent import MedChangeEvent
from Events.seizureEvent import SeizureEvent
from Events.event import Event


def serializedEventFactory(serializedEvent: dict[str, str]) -> Event:
    match serializedEvent["eventType"]:
        case EventType.SEIZURE.value:
            return SeizureEvent(datetime.min, "", False, -1).deserialize(serializedEvent)
                    
        case EventType.APPOINTMENT.value:
            return AppointmentEvent(datetime.min, "", AppointmentType.OTHER, "") .deserialize(serializedEvent)
        
        case EventType.MEDCHANGE.value:
            return MedChangeEvent(datetime.min, "", "", "", "").deserialize(serializedEvent)
        
        case _:
            raise TypeError("Invalid Event Type")