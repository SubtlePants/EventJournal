from datetime import datetime
from typing import List
from Events.seizureEvent import SeizureEvent
from Events.appointmentEvent import AppointmentEvent
from Utils.enums import AppointmentType
from Events.event import Event
from FileSystem.eventfile import readEventsFromFile, writeEventsToFile

# a = AppointmentEvent(datetime.now(), "testdesc", AppointmentType.NEUROLOGY, "testreason")
a = SeizureEvent(datetime.now(), "test", True, 5)

b = AppointmentEvent(datetime.now(), "test", AppointmentType.NEUROLOGY, "check up")

events: List[Event] = [a, b]

writeEventsToFile(events)

events2 = readEventsFromFile()
print(events2[0].duration if isinstance(events2[0], SeizureEvent) else "First Event Failed to Save/Load")
print(events2[1].appointmentType if isinstance(events2[1], AppointmentEvent) else "Second Event Failed to Save/Load")