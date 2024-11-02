
from Utils.enums import EventType
from UserInterface.userinterface import UserInterface


class TestInterface(UserInterface):
    def getEventFromUser(self) -> dict[str, str]:
        return {"eventType": EventType.SEIZURE.value, "date": "27/02/24 14:00", "description": "Happy Birthday", "duration": "3", "temporal": "True"}