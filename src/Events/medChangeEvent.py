from datetime import datetime
from Events.event import Event

class MedChangeEvent(Event):
    def __init__(self, date: datetime, description: str, medName: str, oldDosage: str, newDosage: str) -> None:
        super().__init__(date, description)
        self.medName = medName
        self.oldDosage = oldDosage
        self.newDosage = newDosage