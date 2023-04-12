from commands.google_wikipedia_search import GoogleWikipediaSearch
from commands.open import Open
from commands.close import Close
from commands.new_word import NewWord
from commands.new_notepad import NewNotepad
from commands.outlook_email_add_body import OutlookEmailAddBody
from commands.outlook_email_add_cc import OutlookEmailAddCc
from commands.outlook_email_add_subject import OutlookEmailAddSubject
from commands.outlook_email_add_to import OutlookEmailAddTo
from commands.outlook_email_create_new import OutlookEmailCreateNew
from commands.outlook_email_send import OutlookEmailSend
from commands.outlook_event_add_title import OutlookEventAddTitle
from commands.outlook_event_add_start_time import OutlookEventAddStartTime
from commands.outlook_event_add_end_time import OutlookEventAddEndTime
from commands.outlook_event_make_event_all_day import OutlookEventMakeEventAllDay
from commands.outlook_event_save import OutlookEventSave
from commands.outlook_event_add_body import OutlookEventAddBody

from commands.send_email import SendEmail
from commands.save import Save
from commands.vosk_dictation import VoskDictation
from commands.brightness import Brightness
from commands.volume import Volume
from commands.new_calendar_event import NewEvent
from commands.search import Search
from apps.google import Google
from apps.word import Word
from apps.outlook import Outlook
from apps.computer_actions import ComputerActions
from apps.notepad import Notepad
from commands.interface import Interface
from commands.custom_command import CustomCommand
from commands.word_change_font import WordChangeFont
from commands.word_change_size import WordChangeSize
from commands.word_create_new_blank import WordCreateNewBlank


class CommandInterpretor:

    start_apps = {
        'word': Word(),
        'outlook': Outlook(),
        'google': Google(),
        'notepad': Notepad(),
        'computer': ComputerActions(),
        'custom': ''
    }

    def __init__(self, app, last_app, custom='') -> None:
        self.app = app
        self.last_app = last_app
        self.custom = custom
        self.startup_app(app, last_app)
        self.commands = {
            'open_app': Open(self.start_apps[self.app]),
            'close_app': Close(self.start_apps[self.app]),

            # word
            'create_new_word': NewWord(self.start_apps[self.app]),
            'word_create_new_blank': WordCreateNewBlank(self.start_apps[self.app]),
            'save_as_word': Save(self.start_apps[self.app]),
            'start_dictation': VoskDictation(),
            'word_change_font': WordChangeFont(self.start_apps[self.app]),
            'word_change_size': WordChangeSize(self.start_apps[self.app]),
            # notepad
            'create_new_notepad': NewNotepad(self.start_apps[self.app]),
            'notepad_save_as': Save(self.start_apps[self.app]),
            # computer
            'brightness_up': Brightness(self.start_apps[self.app], 'up'),
            'brightness_down': Brightness(self.start_apps[self.app], 'down'),
            'brightness_value': Brightness(self.start_apps[self.app], 'value'),
            'volume_up': Volume(self.start_apps[self.app], 'up'),
            'volume_down': Volume(self.start_apps[self.app], 'down'),
            'volume_value': Volume(self.start_apps[self.app], 'value'),
            # outlook - calendar
            'create_event': NewEvent(self.start_apps[self.app]),
            'outlook_event_add_title': OutlookEventAddTitle(self.start_apps[self.app]),
            'outlook_event_add_start_time': OutlookEventAddStartTime(self.start_apps[self.app]),
            'outlook_event_add_end_time': OutlookEventAddEndTime(self.start_apps[self.app]),
            'outlook_event_make_event_all_day': OutlookEventMakeEventAllDay(self.start_apps[self.app]),
            'outlook_event_save': OutlookEventSave(self.start_apps[self.app]),
            'outlook_event_add_body': OutlookEventAddBody(self.start_apps[self.app]),
            # outlook - email
            'outlook_email_create_new': OutlookEmailCreateNew(self.start_apps[self.app]),
            'outlook_email_add_subject': OutlookEmailAddSubject(self.start_apps[self.app]),
            'outlook_email_add_to': OutlookEmailAddTo(self.start_apps[self.app]),
            'outlook_email_add_cc': OutlookEmailAddCc(self.start_apps[self.app]),
            'outlook_email_add_body': OutlookEmailAddBody(self.start_apps[self.app]),
            'send_email': SendEmail(self.start_apps[self.app]),
            # google search
            'search': Search(self.start_apps[self.app]),
            'google_wikipedia_search': GoogleWikipediaSearch(self.start_apps[self.app]),

            'run_interface': Interface(self.start_apps[self.app]),
            'custom': CustomCommand(self.start_apps[self.app], custom)
        }

    def process_command(self, command):
        if command in self.commands:
            print('command: ', command)
            self.commands[command].execute()
            return command
        else:
            print('not known')
            return None

    # def startup_app(self, app):
    #     print(app, self.app, self.last_app)
    #     if app is not None:
    #         self.last_app = self.app = app
    #     else:
    #         if self.last_app != '':
    #             self.app = self.last_app
    #         else:
    #             print('\n# ', self.last_app, ' #')

    #             return None
    #     return self.app

    def startup_app(self, app, last_app):
        if app is not None:
            self.last_app = self.app = app
        else:
            if last_app != '':
                self.app = last_app
            else:
                return None
        return self.app
