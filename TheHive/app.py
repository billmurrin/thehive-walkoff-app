from apps import App, action, event
from apps.TheHive.events import hive_event


class TheHive(App):

    def __init__(self, name=None, device=None):
        App.__init__(self, name, device)
        self.result = {}

    @event(hive_event)
    def web_hook_handler(data):
        print("I'm in the handler. Here's the data")
        print(data)
        return data

    @action
    def obtain_tlp(self, data):
        print("Obtain TLP method")
        print(data)

    def shutdown(self):
        return
