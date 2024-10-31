from Utils.SerializeUtils.serializeUtils import deserializeEventType, serializeDateTime, deserializeDateTime
from datetime import datetime

from Utils.enums import EventType

class Event:
    def __init__(self, date: datetime, description: str, eventType: EventType ) -> None:
        self.date: datetime = date
        self.description: str = description
        self.eventType: EventType = eventType
    
    def serialize(self) -> dict[str, str]:
        return {"date": serializeDateTime(self.date), "description": self.description, "eventType": self.eventType.value}
    
    def deserialize(self, obj: dict[str, str]) -> None:
        self.date = deserializeDateTime(obj["date"])
        self.description = obj["description"]
        self.eventType = deserializeEventType(obj["eventType"])