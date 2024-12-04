
from datetime import datetime
from itertools import groupby
from typing import List
from Events.appointmentEvent import AppointmentEvent
from Events.event import Event
from Events.medChangeEvent import MedChangeEvent
from Events.seizureEvent import SeizureEvent
from Events.stressevent import StressEvent
from Printers.eventprinter import EventPrinter
from pylatex import Document as Document
from pylatex import Document, Command, Section, Subsection
from pylatex.utils import NoEscape, bold
from Utils.dateformatcodes import justDayFormatCode, justTimeFormatCode
from Utils.enums import EventType


class LatexPrinter(EventPrinter):
    def __init__(self, events: List[Event]) -> None:
        self.events = events
        super().__init__()

    def printEventsJournal(self) -> None:

        journalDocument = EventJournalDocument()
        
        self.events.sort(key= lambda event : event.date)

        for key, group in groupby(self.events, lambda event: event.date.day):
            journalDocument.addDateSection(list(group))
        
        journalDocument.generate_tex("Seizure_Journal")
        



class EventJournalDocument(Document):
    def __init__(self):
        super().__init__() # type: ignore

        self.preamble.append(Command("title", "Seizure Journal")) # type: ignore
        self.preamble.append(Command("author", "Amy Ortega")) # type: ignore
        self.append(NoEscape(r"\maketitle")) # type: ignore

    def addDateSection(self, singleDaysEvents: List[Event]) -> None:
        date: datetime = singleDaysEvents[0].date
        with self.create(Section(date.strftime(justDayFormatCode), numbering= False,)):
            for event in singleDaysEvents:
                self._addEventSection(event, event.date)

    def _addEventSection(self, event: Event, date: datetime) -> None:
        with self.create(Subsection(date.strftime(justTimeFormatCode), False)):
            self._appendNameAndDataStrings("Type: ", event.eventType.value)
            self._appendNameAndDataStrings("Description: ", event.description)
            self.append("\n")

            match event.eventType:
                case EventType.APPOINTMENT:
                    self._addAppointmentEventSubSection(event)
                case EventType.MEDCHANGE:
                    self._addMedChangeEventSubSection(event)
                case EventType.SEIZURE:
                    self._addSeizureEventSubSection(event)
                case EventType.STRESS:
                    self._addStressEventSubSection(event)
                case _:
                    raise TypeError("Invalid Event Type in Latex Printer")
                    

    
    def _addAppointmentEventSubSection(self, event: AppointmentEvent) -> None:
        self._appendNameAndDataStrings("Appointment Type: ", event.appointmentType.value)
        self._appendNameAndDataStrings("Reason for Appointment: ", event.reason)
    
    def _addMedChangeEventSubSection(self, event: MedChangeEvent) -> None:
        self._appendNameAndDataStrings("Medicine Name: ", event.medName)
        self._appendNameAndDataStrings("Old Dose: ", event.oldDosage)
        self._appendNameAndDataStrings("New Dose", event.newDosage)
    
    def _addSeizureEventSubSection(self, event: SeizureEvent):
        self._appendNameAndDataStrings("Includes Temporal Symptoms: ", str(event.temporalSymptoms))
        self._appendNameAndDataStrings("Duration: ", str(event.duration))
    
    def _addStressEventSubSection(self, event: StressEvent) -> None:
        pass
    
    def _appendNameAndDataStrings(self, name :str, data: str):
        self.append(bold(name))
        self.append(data)
        self.append("\n")
