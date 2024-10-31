from datetime import datetime
from Events.event import Event
from Utils.SerializeUtils.serializeUtils import deserializeAppointmentType
from Utils.enums import AppointmentType, EventType

class AppointmentEvent(Event):
    def __init__(self, date: datetime, description: str, appointmentType: AppointmentType, reason: str ) -> None:
        super().__init__(date, description, EventType.APPOINTMENT)
        self.appointmentType: AppointmentType = appointmentType
        self.reason: str = reason
    
    def serialize(self) -> dict[str, str]:
        parentDict =super().serialize()
        parentDict.update({"appointmentType": self.appointmentType.value, "reason": self.reason})
        return parentDict

    
    def deserialize(self, obj: dict[str, str]):
        super().deserialize(obj)
        self.appointmentType = deserializeAppointmentType(obj["appointmentType"])
        self.reason = obj["reason"]
        return self