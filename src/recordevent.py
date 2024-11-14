
from Handlers.handler import NewInputEventHandler
from UserInterface.commandline import CommandLineInterface
from FileSystem.eventfile import readEventsFromFile, writeEventsToFile
from Events.event import Event
from typing import List

try:
    eventsList: List[Event] = readEventsFromFile()
except:
    print("Events list not found, creating new events list")
    eventsList: List[Event] = []

eventHandler = NewInputEventHandler(CommandLineInterface())

eventsList.append(eventHandler.addEventFromUser())

writeEventsToFile(eventsList)