import json
from typing import Any, Dict, List, Text
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet


# this function sets knowledge in slot-DB
class ActionSaveKnowledge(Action):
    def name(self) -> Text:
        return "action_save_knowledge"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # gives a list back with a slots available
        temp_mapping = list(tracker.slots.keys())

        # init slots to set / learned content
        slots_to_set = []
        # search in list of all defined slots if any content has been found for related slot and safe it
        for slot_name in temp_mapping:
            learned_content = list(tracker.get_latest_entity_values(slot_name))
            if learned_content:
                dispatcher.utter_message(text=f"I have learned about {slot_name}: {', '.join(learned_content)}")
                slots_to_set.append(SlotSet(slot_name, learned_content))
        if slots_to_set:
            return slots_to_set
        else:
            dispatcher.utter_message(text="Sorry, I didn't get that. Please provide valid input.")
            return []


# this function only return the set of information about a certain topic - softwareType
class ActionGetInformationSoftwareType(Action):
    def name(self) -> Text:
        return "action_get_softwareTypes"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        search_value = "softwareTypes"

        information_learned = tracker.get_slot(search_value)

        if information_learned:
            dispatcher.utter_message(text=f"Learned content for {search_value} is: {information_learned}")
        else:
            dispatcher.utter_message(f"No information about {search_value} learned so far.")

        return []


# this function only return the set of information about a certain topic - softwareQuality
class ActionGetInformationSoftwareQuality(Action):
    def name(self) -> Text:
        return "action_get_softwareQuality"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        search_value = "softwareQuality"

        information_learned = tracker.get_slot(search_value)

        if information_learned:
            dispatcher.utter_message(text=f"Learned content for {search_value} is: {information_learned}")
        else:
            dispatcher.utter_message(f"No information about {search_value} learned so far.")

        return []


# this function only return the set of information about a certain topic - systematicProcess
class ActionGetInformationSystematicProces(Action):
    def name(self) -> Text:
        return "action_get_systematicProcess"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        search_value = "systematicProcess"

        information_learned = tracker.get_slot(search_value)

        if information_learned:
            dispatcher.utter_message(text=f"Learned content for {search_value} is: {information_learned}")
        else:
            dispatcher.utter_message(f"No information about {search_value} learned so far.")

        return []


# this function only return the set of information about a certain topic - AreasOfTension
class ActionGetInformationSAreasOfTension(Action):
    def name(self) -> Text:
        return "action_get_areasOfTension"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        search_value = "areasOfTension"

        information_learned = tracker.get_slot(search_value)

        if information_learned:
            dispatcher.utter_message(text=f"Learned content for {search_value} is: {information_learned}")
        else:
            dispatcher.utter_message(f"No information about {search_value} learned so far.")

        return []


# this function only return the set of information about a certain topic - typesOfApplication
class ActionGetInformationTypesOfApplication(Action):
    def name(self) -> Text:
        return "action_get_typesOfApplication"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        search_value = "typesOfApplication"

        information_learned = tracker.get_slot(search_value)

        if information_learned:
            dispatcher.utter_message(text=f"Learned content for {search_value} is: {information_learned}")
        else:
            dispatcher.utter_message(f"No information about {search_value} learned so far.")

        return []


# this function only return the set of information about a certain topic - professionalSoftwareDevelopment
class ActionGetInformationProfessionalSoftwareDevelopment(Action):
    def name(self) -> Text:
        return "action_get_professionalSoftwareDevelopment"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        search_value = "professionalSoftwareDevelopment"

        information_learned = tracker.get_slot(search_value)

        if information_learned:
            dispatcher.utter_message(text=f"Learned content for {search_value} is: {information_learned}")
        else:
            dispatcher.utter_message(f"No information about {search_value} learned so far.")

        return []


# this function only return the set of information about a certain topic - professionalSoftwareDevelopment
class ActionGetInformationSoftware(Action):
    def name(self) -> Text:
        return "action_get_software"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        search_value = "software"

        information_learned = tracker.get_slot(search_value)

        if information_learned:
            dispatcher.utter_message(text=f"Learned content for {search_value} is: {information_learned}")
        else:
            dispatcher.utter_message(f"No information about {search_value} learned so far.")

        return []


# this function only return the set of information about a certain topic - softwareEngineeringDisciplines
class ActionGetSoftwareEngineeringDisciplines(Action):
    def name(self) -> Text:
        return "action_get_softwareEngineeringDisciplines"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        search_value = "softwareEngineeringDisciplines"

        information_learned = tracker.get_slot(search_value)

        if information_learned:
            dispatcher.utter_message(text=f"Learned content for {search_value} is: {information_learned}")
        else:
            dispatcher.utter_message(f"No information about {search_value} learned so far.")

        return []


# this function only return the set of information about a certain topic - softwareEthics
class ActionGetsoftwareEthics(Action):
    def name(self) -> Text:
        return "action_get_softwareEthics"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        search_value = "softwareEthics"

        information_learned = tracker.get_slot(search_value)

        if information_learned:
            dispatcher.utter_message(text=f"Learned content for {search_value} is: {information_learned}")
        else:
            dispatcher.utter_message(f"No information about {search_value} learned so far.")

        return []


# this function should return all the information learned (maybe add that this is dumbed into a file)
class ActionGetAllLearnedContent(Action):
    def name(self) -> Text:
        return "action_get_all_learned_content"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Get all the set slot names
        slot_names = tracker.slots.keys()

        # Create a dictionary to store the non-None slot values
        slot_values = {}

        # Store the non-None slot values
        for slot_name in slot_names:
            slot_value = tracker.get_slot(slot_name)
            if slot_value is not None:
                slot_values[slot_name] = slot_value

        # Print the non-None slot values
        dispatcher.utter_message(text="Here is what we have learned today: \n")
        for slot_name, slot_value in slot_values.items():
            dispatcher.utter_message(text=f"{slot_name}: {slot_value}")

        # Save the non-None slot values in a JSON file
        with open('learned_content.json', 'w') as file:
            json.dump(slot_values, file)
            dispatcher.utter_message(text="The learned content can be found in the file: learned_content.json")

        return []


# this function should return the set of information about a certain topic
# as of today the try to make it generic, but no idea yet
class ActionGetInformationAboutCertainTopic(Action):
    def name(self) -> Text:
        return "action_get_information_about_certain_topic"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # searches all slot values
        # search_value = self.extract_slot_info(tracker)
        # print("The Search value is: " + search_value)
        # searches only for certain entity

        last_slot_name = tracker.current_slot_values()
        slotname = last_slot_name.get('searchValue')
        print(type(slotname))
        print(last_slot_name)
        print(f"\n")
        last_slot_name_2 = tracker.get_slot("searchValue")
        print(last_slot_name_2)

        """
        if search_value:
            # Hier können Sie die gewünschte Logik für die Verarbeitung der Slot-Werte implementieren
            slot_values = [value for value in tracker.slots.values() if value is not None]
            information = ", ".join(slot_values)  # Beispiel: Alle Slot-Werte zu einem Text verbinden
            dispatcher.utter_message(text=f"Here is the information I have about {search_value}: " + information)
        else:
            dispatcher.utter_message(text="I don't have any information at the moment.")"""

        return []
