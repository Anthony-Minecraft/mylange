# IMPORTS
from enum import Enum
# Thanks Chat
class AnsiColor(Enum):
    RESET = "\033[0m"
    BLACK = "\033[30m"
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    MAGENTA = "\033[35m"
    CYAN = "\033[36m"
    WHITE = "\033[37m"
    
    BRIGHT_BLACK = "\033[90m"
    BRIGHT_RED = "\033[91m"
    BRIGHT_GREEN = "\033[92m"
    BRIGHT_YELLOW = "\033[93m"
    BRIGHT_BLUE = "\033[94m"
    BRIGHT_MAGENTA = "\033[95m"
    BRIGHT_CYAN = "\033[96m"
    BRIGHT_WHITE = "\033[97m"

    @staticmethod
    def colorize(text:str, color:'AnsiColor') -> str:
        return f"{color.value}{text}{AnsiColor.RESET.value}"
    
    @staticmethod
    def println(text:str, color:'AnsiColor') -> None:
        print(AnsiColor.colorize(text, color))