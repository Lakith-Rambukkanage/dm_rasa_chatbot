# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from actions.search import format_string, product_search

from dummy_data.dummy_data import products_list


class ActionGetProductsList(Action):
    def name(self) -> Text:
        return "action_get_product_list"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:

        # slots
        product_category = tracker.get_slot("product_category")
        product_name = tracker.get_slot("product_name")
        brand = tracker.get_slot("brand")
        size = tracker.get_slot("size")
        colour = tracker.get_slot("colour")
        material = tracker.get_slot("material")

        response_product_list = product_search(
            product_category, product_name, size, colour, material, brand
        )

        for product in response_product_list:
            products_string = "--ගැලපෙන භාණ්ඩ--"
            products_string += format_string(product)

        dispatcher.utter_message(text=products_string)

        return []
