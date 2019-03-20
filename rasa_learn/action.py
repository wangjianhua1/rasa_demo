from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet


# 继承Action
class ActionAskWeather(Action):
    def name(self):
        return 'action_ask_weather'

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message(f'您访问的天气地点是哪里呢')
        return [SlotSet(('city', '武汉'))]
