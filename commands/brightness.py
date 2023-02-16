from command import ICommand
from speak import Speak
from computer_actions import ComputerActions


class Brightness(ICommand):
    def __init__(self, app, type_of_action) -> None:
        super().__init__(app)
        self.app = app
        self.type_of_action = type_of_action

    def execute(self):
        speaker = Speak()
        try:
            if self.type_of_action == 'up':
                self.app.brightness_up()
                speaker.speak('brightness_up', self.app, True)
            elif self.type_of_action == 'down':
                self.app.brightness_down()
                speaker.speak('brightness_down', self.app, True)
            elif self.type_of_action == 'value':
                self.app.brightness_value()
                speaker.speak('brightness_value', self.app, True)

        except:
            speaker.speak('create_new', self.app, None)
            print('exception create new')
        else:
            speaker.speak('create_new', self.app, False)