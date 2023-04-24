# Import necessary commands and apps
from commands.google_wikipedia_search import GoogleWikipediaSearch
from commands.notepad_save_as import NotepadSaveAs
from commands.open import Open
from commands.close import Close
from commands.word_create_new import WordCreateNew
from commands.notepad_create_new import NotepadCreateNew
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

from commands.word_save_as import Save
from commands.vosk_dictation import VoskDictation
from commands.brightness import Brightness
from commands.volume import Volume
from commands.outlook_event_create import OutlookEventCreate
from commands.google_search import GoogleSearch
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


class CommandInterpreter:

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
            'word_create_new': WordCreateNew(self.start_apps[self.app]),
            'word_create_new_blank': WordCreateNewBlank(self.start_apps[self.app]),
            'word_save_as': Save(self.start_apps[self.app]),
            'word_change_font': WordChangeFont(self.start_apps[self.app]),
            'word_change_size': WordChangeSize(self.start_apps[self.app]),
            # notepad
            'notepad_create_new': NotepadCreateNew(self.start_apps[self.app]),
            'notepad_save_as': NotepadSaveAs(self.start_apps[self.app]),
            # computer
            'computer_brightness_up': Brightness(self.start_apps[self.app], 'computer_brightness_up'),
            'computer_brightness_down': Brightness(self.start_apps[self.app], 'computer_brightness_down'),
            'computer_brightness_value': Brightness(self.start_apps[self.app], 'computer_brightness_value'),
            'computer_volume_up': Volume(self.start_apps[self.app], 'computer_volume_up'),
            'computer_volume_down': Volume(self.start_apps[self.app], 'computer_volume_down'),
            'computer_volume_value': Volume(self.start_apps[self.app], 'computer_volume_value'),
            # outlook - calendar
            'outlook_event_create': OutlookEventCreate(self.start_apps[self.app]),
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
            'outlook_email_send': OutlookEmailSend(self.start_apps[self.app]),
            # google search
            'google_search': GoogleSearch(self.start_apps[self.app]),
            'google_wikipedia_search': GoogleWikipediaSearch(self.start_apps[self.app]),

            'start_dictation': VoskDictation(),

            'run_interface': Interface(self.start_apps[self.app]),
            'custom': CustomCommand(self.start_apps[self.app], custom)
        }

    def process_command(self, command):
        # if command can be found in self.commands, it executes it
        if command in self.commands:
            print('command: ', command)
            self.commands[command].execute()
            return command
        else:
            return None

    # function that selects the app on which the action will be performed
    def startup_app(self, app, last_app):
        if app is not None:
            self.last_app = self.app = app
        else:
            if last_app != '':
                self.app = last_app
            else:
                return None
        return self.app
