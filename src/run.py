from datetime import datetime
from typing import List
from Events.seizureEvent import SeizureEvent
from Events.appointmentEvent import AppointmentEvent
from Utils.enums import AppointmentType
from Events.event import Event
from FileSystem.eventfile import readEventsFromFile, writeEventsToFile
from Events.medChangeEvent import MedChangeEvent
from UserInterface.testinterface import TestInterface
from Handlers.handler import NewInputEventHandler
from UserInterface.commandline import CommandLineInterface

# a = AppointmentEvent(datetime.now(), "testdesc", AppointmentType.NEUROLOGY, "testreason")
a = SeizureEvent(date=datetime.now(), description="test", temporalSymptoms=True, duration=5)

b = AppointmentEvent(date=datetime.now(), description="test", appointmentType=AppointmentType.NEUROLOGY, reason="check up")

c = MedChangeEvent(description= "New Med", date= datetime.now(), medName="Med", oldDosage="oldDose", newDosage="newDose")

events: List[Event] = [a, b, c]

writeEventsToFile(events)

events2 = readEventsFromFile()
print(events2[0].duration if isinstance(events2[0], SeizureEvent) else "First Event Failed to Save/Load")
print(events2[1].appointmentType if isinstance(events2[1], AppointmentEvent) else "Second Event Failed to Save/Load")
print(events2[2].oldDosage if isinstance(events2[2], MedChangeEvent) else "Third Event Failed to Save/Load")

testInterface = TestInterface()

eventHandler = NewInputEventHandler(interface=CommandLineInterface())

eventFromHandler = eventHandler.addEventFromUser()
print(eventFromHandler.serialize())