# actions/actions.py

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet, EventType

class ActionSubmitFeedbackForm(Action):
    def name(self) -> Text:
        return "action_submit_positive_feedback_form"

    def run(self, dispatcher, tracker, domain) -> List[EventType]:
        positive_feedback = tracker.get_slot("positive_feedback")
        #negative_feedback = tracker.get_slot("negative_feedback")

        # Process the feedback or store it in a file, database, etc.
        # For now, we'll simply echo it back to the user.

        dispatcher.utter_message("Thank you for your positive feedback!")
        #dispatcher.utter_message(f"Positive feedback: {positive_feedback}")
        #dispatcher.utter_message(f"Negative feedback: {negative_feedback}")

        return [SlotSet("positive_feedback", None)]

class ActionSubmitNegativeFeedbackForm(Action):
    def name(self) -> Text:
        return "action_submit_negative_feedback_form"

    def run(self, dispatcher, tracker, domain) -> List[EventType]:
        #positive_feedback = tracker.get_slot("positive_feedback")
        negative_feedback = tracker.get_slot("negative_feedback")

        # Process the feedback or store it in a file, database, etc.
        # For now, we'll simply echo it back to the user.

        dispatcher.utter_message("Thank you for your negative feedback!")
        #dispatcher.utter_message(f"Positive feedback: {positive_feedback}")
        #dispatcher.utter_message(f"Negative feedback: {negative_feedback}")

        return [SlotSet("negative_feedback", None)]


class ActionPositiveFeedback(Action):

    def name(self) -> Text:
        return "action_set_positive_feedback"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:
        file_path = "feedback.txt"  # Replace with the actual path to your file

        # Open the file in append mode
        with open(file_path, 'a') as file:
            content_to_append = tracker.latest_message.get("text") + "\n"
            file.write(content_to_append)
            file.close()

        return [
            SlotSet("positive_feedback", tracker.latest_message.get("text"))
        ]

class ActionNegativeFeedback(Action):

    def name(self) -> Text:
        return "action_set_negative_feedback"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:
        file_path = "feedback.txt"  # Replace with the actual path to your file

        # Open the file in append mode
        with open(file_path, 'a') as file:
            content_to_append = tracker.latest_message.get("text") + "\n"
            file.write(content_to_append)
            file.close()

        return []


class ActionSummarize(Action):

    def name(self) -> Text:
        return "action_summarize"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:
        file_path = "feedback.txt"  # Replace with the actual path to your file

        # Open the file in append mode
        content=""
        with open(file_path, 'r') as file:
            content = file.read()
            print(content)
            file.close()


        #dispatcher.utter_message("content to summarize " + content)

        prompt = content
        summary = summarize_for_manager(prompt)
        dispatcher.utter_message("Recommendations from generative AI for Manager")
        dispatcher.utter_message(summary)
            
        return []

import requests
import os
import openai

def summarize_for_manager(prompt):
    #print(prompt)
    system_message = {
    "role": "system",
    "content": "Separate each bullet with a new line. Organize it under each name with title as name and type of feedback which is Positive and Negative. give some recommendations to each under their name.",
    }
    message_content = [system_message, {"role":"user","content":prompt}]
    api_url = "https://api.openai.com/v1/chat/completions"
    #openai.api_key = "YOUR_OPENAI_API_KEY"  # Replace with your OpenAI API key
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=message_content,
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    print("\n response from api start \n")
    print(response.choices[0].message.content)
    print("\n response from api end \n")
    return response.choices[0].message.content



