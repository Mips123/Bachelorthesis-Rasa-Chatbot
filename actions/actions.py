from typing import Any, Text, Dict, List
from rasa_sdk.events import SlotSet
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


# Common test function
class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_hello_world"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Hello World!")

        return []


# this function should confirm the learning process and should unlock the bot if he´s stuck
class ConfirmLearning(Action):
    def name(self) -> Text:
        return "action_confirm_learning"

    def run(
            self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:
        # Send message and wait for user response
        dispatcher.utter_message(text="Great, let´s learn something new!")
        return []


# this function should save the name of the user
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
                text="Sorry i did not get that, please enter your name again.")
            return []


# this function should explain the usage of the bot
class ExplainBotToUser(Action):
    def name(self) -> Text:
        return "action_explain_bot_to_user"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(
            text=f"I am Bob the learning bot. \n"
                 f"My purpose is to learn something together with you. Here is how it works. \n"
                 f"Have a look at page 4 of your script. "
                 f"If you want to teach me the content, write a text like this: \n"
                 f"\"Professional Software development consists of programming as side activity and professional programming\" \n"
                 f"After that, you can ask me what i have learned via \"Tell me something about professional software development\"\n"
                 f"When you are finished, ask me what we´ve learned today and i will summarize it for you. \n"
                 f"When you are done for today, just write \"stop\" \n"
                 f"So let´s start!")
        return []
