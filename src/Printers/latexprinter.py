
from typing import List
from Events.event import Event
from Printers.eventprinter import EventPrinter
from pylatex import Document, Command, Section, Subsection
from pylatex.utils import NoEscape


class LatexPrinter(EventPrinter):
    def printEventsJournal(self, events: List[Event]) -> None:


class EventJournalDocument(Document):
    def __init__(self):
        super().__init__()

        self.preamble.append(Command("title", "Seizure Journal"))
        self.append(NoEscape(r"\maketitle"))