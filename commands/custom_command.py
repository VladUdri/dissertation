from commands.command import ICommand
from speak import Speak
from key_action import KeyAction
import json


class CustomCommand(ICommand):
    def __init__(self, app, custom) -> None:
        super().__init__(app)
        self.app = app
        self.custom = custom
        with open('jsons/custom_commands.json') as f:
            self.custom_comm = json.load(f)

    def execute(self):
        speaker = Speak()
        try:
            KeyAction().execute(self.custom_comm[self.custom])
        except:
            speaker.simple_speak('Something went wrong, please try again!')
