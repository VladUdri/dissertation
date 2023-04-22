from abc import ABC, abstractmethod


class ICommand(ABC):
    def __init__(self, app) -> None:
        self.app = app

    def execute(self):
        pass

