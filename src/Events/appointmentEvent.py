from dataclasses import field, dataclass
from Events.event import Event
from Utils.SerializeUtils.serializeUtils import deserializeAppointmentType
from Utils.enums import AppointmentType, EventType

@dataclass
class AppointmentEvent(Event):
    appointmentType: AppointmentType
    reason: str
    eventType: EventType = field(default = EventType.APPOINTMENT, init= False)
    
    def serialize(self) -> dict[str, str]:
        parentDict =super().serialize()
        parentDict.update({"appointmentType": self.appointmentType.value, "reason": self.reason})
        return parentDict

    
    def deserialize(self, obj: dict[str, str]):
        super().deserialize(obj)
        self.appointmentType = deserializeAppointmentType(obj["appointmentType"])
        self.reason = obj["reason"]
        return self