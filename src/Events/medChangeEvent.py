from datetime import datetime
from Events.event import Event

class MedChangeEvent(Event):
    def __init__(self, date: datetime, description: str, medName: str, oldDosage: str, newDosage: str) -> None:
        super().__init__(date, description)
        self.medName = medName
        self.oldDosage = oldDosage
        self.newDosage = newDosage

    def serialize(self) -> dict[str, str]:
        parentDict =super().serialize()
        parentDict.update({"medName": self.medName, "oldDosage": self.oldDosage, "newDosage": self.newDosage})
        return parentDict
    
    def deserialize(self, obj: dict[str, str]) -> None:
        super().deserialize(obj)
        self.medName = obj["medName"]
        self.oldDosage = obj["oldDosage"]
        self.newDosage = obj["newDosage"]