from datetime import datetime
from enum import Enum
from log_level import LogLevel

class TestLogger:
    __log_file_path: str = None
    __min_log_level: int

    def __init__(self, min_log_level: Enum, log_file_path: str = None) -> None:
        self.__min_log_level = min_log_level.value

        if log_file_path is not None:
            self.__log_file_path = log_file_path         

    def __append_to_logfile(self, text: str) -> None:
        with open(self.__log_file_path, "a") as myfile:
                    myfile.write(text)

    def Log(self, loglevel: LogLevel, text: str) -> None:
        text = text.strip()
        if loglevel.value >= self.__min_log_level:
            date = datetime.now().strftime("%H:%M:%S")
            s = f"[{date}] {loglevel.name}: {str(text)}"
            print(s)

            if self.__log_file_path is not None:
                self.__append_to_logfile(s)

    def LogDebug(self, text: str) -> None:
        self.Log(LogLevel.DEBUG, text)

    def LogInformation(self, text: str) -> None:
        self.Log(LogLevel.INFORMATION, text)

    def LogWarning(self, text: str) -> None:
        self.Log(LogLevel.WARNING, text)

    def LogError(self, text: str) -> None:
        self.Log(LogLevel.ERROR, text)

    def LogCritical(self, text: str) -> None:
        self.Log(LogLevel.CRITICAL, text)
