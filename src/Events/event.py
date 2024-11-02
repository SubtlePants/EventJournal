from dataclasses import dataclass
from typing import Self
from Utils.SerializeUtils.serializeUtils import deserializeEventType, serializeDateTime, deserializeDateTime
from datetime import datetime

from Utils.enums import EventType

@dataclass
class Event:
    description: str
    date: datetime
    eventType: EventType
    
    def serialize(self) -> dict[str, str]:
        return {"date": serializeDateTime(self.date), "description": self.description, "eventType": self.eventType.value}
    
    def deserialize(self, obj: dict[str, str]) -> Self:
        self.date = deserializeDateTime(obj["date"])
        self.description = obj["description"]
        self.eventType = deserializeEventType(obj["eventType"])
        return self