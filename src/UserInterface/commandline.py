
from datetime import datetime
from enum import Enum
from Utils.enums import AppointmentType, EventType
from Utils.SerializeUtils.serializeUtils import deserializeDateTime, serializeDateTime, serializedDateFormatCode
from UserInterface.userinterface import UserInterface

def enumStringValueToCharAbbrev(type: Enum) -> str:
    return type.value[0]

def enumStringValueToTwoCharAbbrev(type: Enum) -> str:
    return type.value[0] + type.value[1]

class CommandLineInterface(UserInterface):
    
    def getEventFromUser(self) -> dict[str, str]:
        event: dict[str, str] = {}
        (event, eventType) = self.getEventTypeFromUser(event)
        event = self.getUserDate(event)
        userDescription = input("Input the description of the event: \n")
        event["description"] = userDescription
        
        match eventType:
            case EventType.APPOINTMENT:
                event = self.getAppointmentInformationFromUser(event)
            case EventType.MEDCHANGE:
                event = self.getMedChangeInformationFromUser(event)
            case EventType.SEIZURE:
                event= self.getSeizureInformationFromUser(event)
            case EventType.STRESS:
                event = self.getStressEventInformationFromUser(event)


        return event
    
    def getEventTypeFromUser(self, event:dict[str, str]) -> tuple[dict[str,str], EventType]:
        print("What type of event would you like to record? \n")
        eventTypeAbbreviations: dict[str, EventType] = {}
        typeString: str = ""
        for type in EventType:
            eventTypeAbbreviations[enumStringValueToTwoCharAbbrev(type).lower()] = type
            typeString += f" ({enumStringValueToTwoCharAbbrev(type).lower()}) {type.value}"
        userTypeAbbrev = input(typeString + '\n')

        try:
            event["eventType"] = eventTypeAbbreviations[userTypeAbbrev].value
            return (event, eventTypeAbbreviations[userTypeAbbrev])
        except:
            print("I'm sorry, you input was invalid. Try again \n")
            return self.getEventTypeFromUser(event)
        
        
        
        
        return ({}, EventType.APPOINTMENT)
    
    def getAppointmentInformationFromUser(self, event: dict[str,str]) -> dict[str,str]:
        event = self.getAppointmentTypeFromUser(event)
        userReason = input("What was the reason for this appointment? \n")
        event["reason"] = userReason
        return event
    
    def getAppointmentTypeFromUser(self, event: dict[str,str]) -> dict[str,str]:
        appointmentTypeAbbreviations: dict[str, AppointmentType] = {}
        typeString: str = ""
        for type in AppointmentType:
            appointmentTypeAbbreviations[enumStringValueToCharAbbrev(type).lower()] = type
            typeString += f" ({enumStringValueToCharAbbrev(type).lower()}) {type.value}"
        userTypeAbbrev = input(typeString + '\n')

        try:
            event["appointmentType"] = appointmentTypeAbbreviations[userTypeAbbrev].value
            return event
        except:
            print("I'm sorry, you input was invalid. Try again")
            return self.getAppointmentTypeFromUser(event)


    def getMedChangeInformationFromUser(self, event: dict[str,str]) -> dict[str,str]:
        event["medName"] = input("What is the name of the medication? \n")
        event["oldDosage"] = input("What was the previous dose of this medication? \n")
        event["newDosage"] = input("What is the new dosage of this medication? \n")
        return event

    def getSeizureInformationFromUser(self, event: dict[str,str]) -> dict[str,str]:
        userTemporalFlag = input("Did this seizure have temporal symptoms? (y,n) \n")
        match userTemporalFlag.lower():
            case "y":
                event["temporal"] = "True"
            case "n":
                event["temporal"] = "False"
            case _:
                print("Input must be y or n, try again")
                return self.getSeizureInformationFromUser(event)
        
        userDuration = input("How long was the seizure in whole minutes? \n")
        try:
            int(userDuration)
            event["duration"] = userDuration
        except:
            print("Duration must be a valid integer, try again")
            return self.getSeizureInformationFromUser(event)
            
        return event

    def getStressEventInformationFromUser(self, event: dict[str,str]) -> dict[str,str]:
        return event

    def getUserDate(self, event: dict[str, str]) -> dict[str,str]:
        useNow= input("Use now? y/n \n")
        match useNow.lower():
            case "y":
                event["date"] = serializeDateTime(dateTime= datetime.now())
                return event
            case "n":
                userDate = input(f"Please Input a date in the following format {serializedDateFormatCode}: \n")
                try:
                    deserializeDateTime(userDate)
                except:
                    print("Date Format Invalid, try again")
                    return self.getUserDate(event)
                    
                event["date"] = userDate
                return event
            case _:
                print ("I didn't quite catch that, please try again:")
                return self.getUserDate(event)


    
    
        
        
   