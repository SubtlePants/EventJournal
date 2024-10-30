from Utils.SerializeUtils.serializeUtils import serializeDateTime, deserializeDateTime
from datetime import datetime

class Event:
    def __init__(self, date: datetime, description: str ) -> None:
        self.date = date
        self.description: str = description
    
    def serialize(self) -> dict[str, str]:
        return {"date": serializeDateTime(self.date), "description": self.description}
    
    def deserialize(self, obj: dict[str, str]) -> None:
        self.date = deserializeDateTime(obj["date"])
        self.description = obj["description"]
        
    def returnNum(self) -> int:
        a :str = "blah"
        return a