import sys
from colors import Colors
from help import Help
from programs.mp3ytdownload import Download


class Commands:
    def close_program(self) -> None:
        sys.exit()

    def test(self) -> str:
        return f'{Colors.OKGREEN}FUNKCJA TESTOWA{Colors.ENDC}'

    def help(self):
        for help_cmd in Help.help_commands:
            return help_cmd

    def download(self) -> None:
        downld = Download()
        downld.check_instructions()


class ListOfCommands:
    cmd = Commands()
    executable_commands = {
        'exit': cmd.close_program,
        'test': cmd.test,
        '-help': cmd.help,
        'download': cmd.download
    }
