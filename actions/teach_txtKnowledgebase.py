from typing import Any, Dict, List, Text
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.knowledge_base.actions import ActionQueryKnowledgeBase
from rasa_sdk.knowledge_base.storage import InMemoryKnowledgeBase

"""
class MyKnowledgeBaseAction(ActionQueryKnowledgeBase):
    def __init__(self):
        knowledge_base = InMemoryKnowledgeBase("data.json")
        super().__init__(knowledge_base)
"""


class ActionTeach(Action):
    def name(self) -> Text:
        return "action_teach"

    def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:
        # Eingabe vom Benutzer abrufen
        next_user_input = tracker.latest_message.get("text")

        # Eingabe in Wissensdatenbank speichern
        with open("knowledge_base.txt", "a") as file:
            file.write(next_user_input + "\n")

        # Bestätigungsnachricht senden
        dispatcher.utter_message(text="Ich habe etwas gelernt!")

        return []


def load_knowledge_base() -> List[str]:
    # Wissensdatenbank aus Textdatei laden
    try:
        with open("knowledge_base.txt", "r") as file:
            knowledge_base = [line.strip() for line in file]
            return knowledge_base
    except FileNotFoundError:
        return []


class RetrieveKnowlegeFromDB(Action):
    def name(self) -> Text:
        return "action_select_random_entry_from_db"

    def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:
        # Wissensdatenbank abrufen
        knowledge_base = load_knowledge_base()

        if knowledge_base:
            # Zufälligen Eintrag aus der Wissensdatenbank auswählen
            import random
            response = random.choice(knowledge_base)
            dispatcher.utter_message(text=response)
        else:
            # Keine Einträge in der Wissensdatenbank
            dispatcher.utter_message(text="Ich habe noch nichts gelernt.")

        return []

