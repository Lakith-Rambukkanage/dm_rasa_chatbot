# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from actions.search import product_search
from actions.util import format_prod_string

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


        # query from preference slots
        query_vector = {
            "product_category": tracker.get_slot("product_category"),
            "product_name": tracker.get_slot("product_name"),
            "size": tracker.get_slot("size"),
            "colour": tracker.get_slot("colour"),
            "material": tracker.get_slot("material"),
            "brand": tracker.get_slot("brand"),
        }

        response_product_list = product_search(query_vector)

        print(query_vector)
        
        if len(response_product_list)>0:
            dispatcher.utter_message(text="--ගැලපෙන භාණ්ඩ--")

            for product in response_product_list:
                product_string = format_prod_string(product)
                dispatcher.utter_message(text=product_string)
        else:
            dispatcher.utter_message(text="--ගැලපෙන භාණ්ඩ නැත--")
        
        return []
