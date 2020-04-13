from rasa_sdk import Action
from typing import Any, Text, Dict, List, Union
from rasa_sdk.forms import FormAction, REQUESTED_SLOT
from rasa_sdk.events import Form, AllSlotsReset, SlotSet, Restarted, EventType
from rasa_sdk.executor import CollectingDispatcher, Tracker
import os

# class ActionSharePrice(Action):
#     """custom action to return share price from alphavantage""""
#     def name(self) -> Text:
#         return "action_shareprice"

#     def fetchprice(self):
class StatusCheck(FormAction):
    """Form to know the status"""

    def name(self) -> Text:
        """Unique identifier of the form"""
        return "form_statuscheck"
    
    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""

        return ["status", "name", "number"]

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        """A dictionary to map required slots to
            - an extracted entity
            - intent: value pairs
            - a whole message
            or a list of them, where a first match will be picked"""
        
        return {
            "status":self.from_text(intent=None),
            "name":self.from_text(intent=None),
            "number":self.from_text(intent=None)
        }

    def validate_status(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        """Validate name value."""
        if value.lower() in ['new', 'existing']:
            return {"status":value}
        else:
            dispatcher.utter_message(template="utter_wrong_input")
            # validation failed, set this slot to None, meaning the
            # user will be asked for the slot again
            return {"status": None}

    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
        """Define what the form has to do
            after all required slots are filled"""

        # utter submit template
        dispatcher.utter_message(template="utter_submit_new")
        return []

        
class PersonalDetails(FormAction):
    """Form to accept name and DOB"""

    def name(self) -> Text:
        """Unique identifier of the form"""
        return "form_personaldetails"
    
    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""

        return ["name", "number", "status"]

    @staticmethod
    def names_db() -> List[Text]:
        """Database of supported cuisines"""

        return [
            "shubham",
            "eashan"
        ]
    
    @staticmethod
    def numbers_db() -> List[Text]:
        """Database of supported cuisines"""

        return [
            "10664864",
            "5034547"
        ]


    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        """A dictionary to map required slots to
            - an extracted entity
            - intent: value pairs
            - a whole message
            or a list of them, where a first match will be picked"""
        
        return {
            "status":self.from_text(intent=None),
            "name":self.from_text(intent=None),
            "number":self.from_text(intent=None)
        }

    def validate_status(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        """Validate name value."""
        if value.lower() in ['new', 'existing']:
            return {"status":value}
        else:
            dispatcher.utter_message(template="utter_wrong_input")
            # validation failed, set this slot to None, meaning the
            # user will be asked for the slot again
            return {"status": None}


    def validate_name(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        """Validate name value."""

        if value.lower() in self.names_db():
            # validation succeeded, set the value of the "cuisine" slot to value
            return {"name": value}
        else:
            dispatcher.utter_message(template="utter_wrong_name")
            # validation failed, set this slot to None, meaning the
            # user will be asked for the slot again
            return {"name": None}


    def validate_number(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        """Validate number value."""

        if value.lower() in self.numbers_db():
            # validation succeeded, set the value of the "cuisine" slot to value
            return {"number": value}
        else:
            dispatcher.utter_message(template="utter_wrong_policynumber")
            # validation failed, set this slot to None, meaning the
            # user will be asked for the slot again
            return {"number": None}

    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
        """Define what the form has to do
            after all required slots are filled"""

        # utter submit template
        dispatcher.utter_message(template="utter_submit")
        return []