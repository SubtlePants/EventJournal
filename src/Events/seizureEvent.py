from dataclasses import dataclass, field
from typing import Self
from Events.event import Event
from Utils.enums import EventType

@dataclass
class SeizureEvent(Event):
    temporalSymptoms: bool
    duration: int
    eventType: EventType = field(init=False,default= EventType.SEIZURE)
    
    def serialize(self) -> dict[str, str]:
        parentDict = super().serialize()
        parentDict.update({"temporal": str(self.temporalSymptoms), "duration": str(self.duration)})
        return parentDict
    
    def deserialize(self, obj: dict[str, str]) -> Self:
        super().deserialize(obj)
        self.temporalSymptoms = True if obj["temporal"] == "True" else False
        self.duration = int(obj["duration"])
        return self