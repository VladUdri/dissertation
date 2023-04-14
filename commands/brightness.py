from commands.command import ICommand
from speak import Speak


class Brightness(ICommand):
    def __init__(self, app, type_of_action) -> None:
        super().__init__(app)
        self.app = app
        self.type_of_action = type_of_action

    def execute(self):
        speaker = Speak()
        try:
            if self.type_of_action == 'computer_brightness_up':
                self.app.computer_brightness_up()
                speaker.speak('computer_brightness_up', True)
            elif self.type_of_action == 'computer_brightness_down':
                self.app.computer_brightness_down()
                speaker.speak('computer_brightness_down', True)
            elif self.type_of_action == 'computer_brightness_value':
                self.app.computer_brightness_value()
                speaker.speak('computer_brightness_value', True)

        except:
            speaker.simple_speak('Something went wrong, please try again!')
        else:
            if self.type_of_action == 'computer_brightness_up':
                speaker.speak('computer_brightness_up', False)
            elif self.type_of_action == 'computer_brightness_down':
                speaker.speak('computer_brightness_down', False)
            elif self.type_of_action == 'computer_brightness_value':
                speaker.speak('computer_brightness_value', False)
