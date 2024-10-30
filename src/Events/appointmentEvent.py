from datetime import datetime
from Events.event import Event
from Utils.SerializeUtils.serializeUtils import deserializeAppointmentType
from Utils.enums import AppointmentType

class AppointmentEvent(Event):
    def __init__(self, date: datetime, description: str, type: AppointmentType, reason: str ) -> None:
        super().__init__(date, description)
        self.type: AppointmentType = type
        self.reason: str = reason
    
    def serialize(self) -> dict[str, str]:
        parentDict =super().serialize()
        parentDict.update({"type": self.type.value, "reason": self.reason})
        return parentDict

    
    def deserialize(self, obj: dict[str, str]) -> None:
        super().deserialize(obj)
        self.type = deserializeAppointmentType(obj["type"])
        self.reason = obj["reason"]