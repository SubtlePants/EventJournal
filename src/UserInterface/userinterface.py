from abc import ABC, abstractmethod

class UserInterface(ABC):
    @abstractmethod
    def getEventFromUser(self) -> dict[str, str]:
        while False:
            yield None