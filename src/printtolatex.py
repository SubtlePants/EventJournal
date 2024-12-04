
from typing import List

from Events.event import Event
from FileSystem.eventfile import readEventsFromFile
from Printers.latexprinter import LatexPrinter


try:
    eventsList: List[Event] = readEventsFromFile()
except:
    raise IOError("Could not read events from file")

printer = LatexPrinter(eventsList)

printer.printEventsJournal()