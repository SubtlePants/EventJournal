
from userinterface import UserInterface

class CommandLineInterface(UserInterface):
    def __init__(self) -> None:
        super().__init__()
    
    def getEventFromUser(self) -> dict[str, str]:
        return {}