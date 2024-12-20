from Events.event import Event
from Events.eventfactory import serializedEventFactory
from UserInterface.userinterface import UserInterface

class NewInputEventHandler:
    def __init__(self, interface: UserInterface) -> None:
        self.userInterface = interface
    
    def addEventFromUser(self) -> Event:
        eventFromUser = self.userInterface.getEventFromUser()
        try:
            return serializedEventFactory(eventFromUser)
        except:
            raise IOError(f"Interface returned {eventFromUser} is not correct schema for an event type")