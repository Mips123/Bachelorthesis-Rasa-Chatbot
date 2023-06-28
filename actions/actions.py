# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


from typing import Any, Text, Dict, List
from rasa_sdk.events import SlotSet
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_hello_world"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Hello World!")

        return []

"""
class ActionListen(Action):
    def name(self) -> Text:
        return "action_listen"

    def run(
            self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:
        # Nachricht senden und auf Benutzereingabe warten
        #dispatcher.utter_message(text="I´m listening...")
        return []
"""


class ConfirmLearning(Action):
    def name(self) -> Text:
        return "action_confirm_learning"

    def run(
            self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:
        # Nachricht senden und auf Benutzereingabe warten
        dispatcher.utter_message(text="Great, let´s learn something new!")
        return []


class ActionSaveName(Action):
    def name(self) -> Text:
        return "action_save_name"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        user_name = next(tracker.get_latest_entity_values("userName"), None)
        if user_name:
            dispatcher.utter_message(text="Nice to meet you, " + user_name)
            return [SlotSet("userName", user_name)]
        else:
            dispatcher.utter_message(
                text="Sorry i didnt get that, please enter your name again.")
            return []
