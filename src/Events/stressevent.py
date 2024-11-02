from typing import Self
from dataclasses import dataclass, field
from Events.event import Event
from Utils.enums import EventType


@dataclass
class StressEvent(Event):
    eventType: EventType = field(init=False, default=EventType.STRESS)

    def serialize(self) -> dict[str, str]:
        return super().serialize()
    
    def deserialize(self, obj: dict[str, str]) -> Self:
        super().deserialize(obj)
        return self