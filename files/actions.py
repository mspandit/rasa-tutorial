# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/

# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List, Union
#
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction
#
#
class ProcessorForm(FormAction):
   def name(self) -> Text:
      return "processor_form"

   @staticmethod
   def required_slots(tracker: Tracker) -> List[Text]:
      """A list of required slots that the form has to fill"""
      return ["use_conditions", "vertical_segment", "cores_minimum"]

   def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
      """A dictionary to map required slots to
         - an extracted entity
         - intent: value pairs
         - a whole message
         or a list of them, where a first match will be picked"""
      return {
         "use_conditions": [
            self.from_entity(entity="use_conditions"),
            self.from_text()
         ],
         "vertical_segment": [
            self.from_entity(entity="vertical_segment"),
            self.from_text()
         ],
         "cores_minimum": [
            self.from_entity(entity="cores_minimum"),
            self.from_entity(entity="number"),
            self.from_text()
         ]
      }

   def validate_use_conditions(self, value: Text, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> Dict[Text, Any]:
      """Validate use conditions"""
      if value.lower() in ["automotive", "pc", "tablet", "server"]:
         return {"use_conditions": value}
      else:
         dispatcher.utter_template("utter_wrong_use_conditions", tracker)
         return {"use_conditions": None}

   def validate_vertical_segment(self, value: Text, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> Dict[Text, Any]:
      """Validate vertical segment"""
      if value.lower() in ["desktop", "embedded", "mobile", "server", "workstation"]:
         return {"vertical_segment": value}
      else:
         dispatcher.utter_template("utter_wrong_vertical_segment", tracker)
         return {"vertical_segment": None}

   def validate_cores_minimum(self, value: Text, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> Dict[Text, Any]:
      """Validate minimum cores"""
      if int(value) > 0 or int(value) < 121:
         return {"cores_minimum": value}
      else:
         dispatcher.utter_template("utter_wrong_cores_minimum", tracker)
         return {"cores_minimum": None}
   
   def submit(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict]:
     """Define what the form has to do
         after all required slots are filled"""

     # utter submit template
     dispatcher.utter_template("utter_submit", tracker)
     return []
