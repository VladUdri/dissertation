import pyautogui as pg
from time import sleep
import json

file_path = 'jsons/custom_commands.json'


class SaveJson:
    # A class for saving custom voice commands and their associated actions to a JSON file.
    def __init__(self, data) -> None:
        # Constructor method for SaveJson class.
        self.data = data
        with open(file_path) as f:
            self.json_data = json.load(f)

    def _translate(self, action):
        # A private method for translating action strings into their corresponding pyautogui function names.
        # Args: A string representing the action associated with the custom voice command.
        # Returns: a string representing the corresponding pyautogui function name.
        match action:
            case 'Press':
                return 'press'
            case 'Keep pressed':
                return 'key_down'

    def create_action_list(self):
        # A method for creating a list of pyautogui actions associated with the custom voice command.
        # Returns: A list of pyautogui actions.
        action_list = []
        for i in range(0, len(self.data['actions'])):
            if self.data['actions'][i] != '' and self.data['keys'][i] != '':
                action_list.append(self._translate(self.data['actions'][i]))
                action_list.append(self.data['keys'][i])
            if i > 0 and self.data['actions'][i - 1] == 'Keep pressed' and self.data['actions'][i] == 'Press':
                action_list.append('key_up')
                action_list.append(self.data['keys'][i - 1])
        if self.data['actions'][len(self.data['actions']) - 1] == 'Keep pressed':
            action_list.append('key_up')
            action_list.append(
                self.data['keys'][len(self.data['actions']) - 1])
        return action_list

    def __write_json(self):
        # A private method for writing data to the custom_commands.json file.
        with open(file_path, 'w') as f:
            json.dump(self.json_data, f)

    def execute(self):
        # A method for executing the custom voice command and saving it to the custom_commands.json file.
        # Returns: a boolean value indicating whether the execution and saving process was successful.
        try:
            action_list = self.create_action_list()
            self.json_data[self.data['voice_command']] = {}
            self.json_data[self.data['voice_command']] = action_list
            self.__write_json()
            return True
        except:
            return False
