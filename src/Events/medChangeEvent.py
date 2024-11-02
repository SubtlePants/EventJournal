from dataclasses import dataclass, field
from typing import Self
from Events.event import Event
from Utils.enums import EventType

@dataclass
class MedChangeEvent(Event):
    medName: str
    oldDosage: str
    newDosage: str
    eventType: EventType = field(init=False, default=EventType.MEDCHANGE)

    def serialize(self) -> dict[str, str]:
        parentDict =super().serialize()
        parentDict.update({"medName": self.medName, "oldDosage": self.oldDosage, "newDosage": self.newDosage})
        return parentDict
    
    def deserialize(self, obj: dict[str, str]) -> Self:
        super().deserialize(obj)
        self.medName = obj["medName"]
        self.oldDosage = obj["oldDosage"]
        self.newDosage = obj["newDosage"]
        return self