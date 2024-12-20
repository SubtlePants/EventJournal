from typing import List
import json
from Events.event import Event
from Events.eventfactory import serializedEventFactory

EVENTS_FILE_PATH = 'events.json'

def _serializeEvents(events: List[Event]) -> List[dict[str, str]]:
    serializedEvents: List[dict[str, str]] = []
   
    for event in events:
        serializedEvents.append(event.serialize())
   
    return serializedEvents

def _deserializeEvents(serializedEvents: List[dict[str,str]]) -> List[Event]:
    events: List[Event] = []
    for event in serializedEvents:
        events.append(serializedEventFactory(event))
    return events

def writeEventsToFile(events: List[Event]) -> None:
    with open(EVENTS_FILE_PATH, 'w') as file:
        file.write(json.dumps(_serializeEvents(events)))

def readEventsFromFile() -> List[Event]:
    try:
        with open(EVENTS_FILE_PATH, 'r') as file:
            eventsJSON = file.read()
        serializedEvents = json.loads(eventsJSON)
        return _deserializeEvents(serializedEvents)
    except:
        raise IOError("File not found")
