from datetime import datetime
from Events.seizureEvent import SeizureEvent

# a = AppointmentEvent(datetime.now(), "testdesc", AppointmentType.NEUROLOGY, "testreason")
a = SeizureEvent(datetime.now(), "test", True, 5)

serA = a.serialize()

#deserA = AppointmentEvent(datetime.now(), "blah", AppointmentType.OTHER, "blah")
deserA = SeizureEvent(datetime.now(), "", False, 0)

deserA.deserialize(serA)

print(deserA.eventType)
#print(deserA.appointmentType)
print(deserA.description)
print(deserA.temporalSymptoms)
print(deserA.duration)