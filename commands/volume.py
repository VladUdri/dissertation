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
            if self.type_of_action == 'up':
                self.app.computer_volume_up()
                speaker.speak('computer_volume_up', self.app, True)
            elif self.type_of_action == 'down':
                self.app.computer_volume_down()
                speaker.speak('computer_volume_down', self.app, True)
            elif self.type_of_action == 'value':
                self.app.computer_volume_value()
                speaker.speak('computer_volume_value', self.app, True)

        except:
            speaker.speak('create_new', self.app, None)
            print('exception create new')
        else:
            speaker.speak('create_new', self.app, False)
