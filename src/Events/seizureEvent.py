from datetime import datetime
from Events.event import Event
from Utils.enums import EventType

class SeizureEvent(Event):
    def __init__(self, date: datetime, description: str, temporalSymptoms: bool, duration: int) -> None:
        super().__init__(date, description, EventType.SEIZURE)
        self.temporalSymptoms = temporalSymptoms
        self.duration = duration
    
    def serialize(self) -> dict[str, str]:
        parentDict = super().serialize()
        parentDict.update({"temporal": str(self.temporalSymptoms), "duration": str(self.duration)})
        return parentDict
    
    def deserialize(self, obj: dict[str, str]) -> None:
        super().deserialize(obj)
        self.temporalSymptoms = True if obj["temporal"] == "True" else False
        self.duration = int(obj["duration"])