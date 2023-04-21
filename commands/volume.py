from commands.command import ICommand
from speak import Speak


class Volume(ICommand):
    def __init__(self, app, type_of_action) -> None:
        super().__init__(app)
        self.app = app
        self.type_of_action = type_of_action

    def execute(self):
        speaker = Speak()
        try:
            if self.type_of_action == 'computer_volume_up':
                self.app.computer_volume_up()
                speaker.speak('computer_volume_up', True)
            elif self.type_of_action == 'computer_volume_down':
                self.app.computer_volume_down()
                speaker.speak('computer_volume_down', True)
            elif self.type_of_action == 'computer_volume_value':
                self.app.computer_volume_value()
                speaker.speak('computer_volume_value', True)

        except:
            speaker.simple_speak('Something went wrong, please try again!')
        else:
            if self.type_of_action == 'computer_volume_up':
                speaker.speak('computer_volume_up', False)
            elif self.type_of_action == 'computer_volume_down':
                speaker.speak('computer_volume_down', False)
            elif self.type_of_action == 'computer_volume_value':
                speaker.speak('computer_volume_value', False)
