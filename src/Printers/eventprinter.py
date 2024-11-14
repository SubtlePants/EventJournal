

from abc import ABC, abstractmethod
from typing import List

from Events.event import Event


class EventPrinter(ABC):
    @abstractmethod
    def printEventsJournal(self, events: List[Event]) -> None:
        while False:
            yield None