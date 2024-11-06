
from Handlers.handler import NewEventHandler
from UserInterface.commandline import CommandLineInterface
from FileSystem.eventfile import readEventsFromFile, writeEventsToFile
from Events.event import Event
from typing import List

try:
    eventsList: List[Event] = readEventsFromFile()
except:
    eventsList: List[Event] = []

eventHandler = NewEventHandler(CommandLineInterface())

eventsList.append(eventHandler.addEventFromUser())

writeEventsToFile(eventsList)