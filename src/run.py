from datetime import datetime
from Events.appointmentEvent import AppointmentEvent
from Utils.enums import AppointmentType

a = AppointmentEvent(datetime.now(), "testdesc", AppointmentType.NEUROLOGY, "testreason")

serA = a.serialize()

deserA = AppointmentEvent(datetime.now(), "blah", AppointmentType.OTHER, "blah")

deserA.deserialize(serA)

print(deserA.type)
print(deserA.description)
print(deserA.reason)