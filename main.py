import os
from commands import ListOfCommands
from colors import Colors
from typing import List


class Variables:
    location = 'D:\\'
    directory = 'PyCmd\\folder'
    full_path = os.path.join(location, directory)


class CreateEnvironment(Variables):
    def __init__(self):
        super().__init__()
        self.make_dir()

    def make_dir(self):
        try:
            os.mkdir(self.full_path)
        except FileExistsError:
            pass


def search_commands(command: str) -> bool:
    if command.split()[0] in ListOfCommands.executable_commands:
        # ListOfCommands.executable_commands[self.command[0]].__call__()
        return True
    return False
