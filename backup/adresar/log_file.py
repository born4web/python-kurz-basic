"""
Log soubor pro podporu projektu

1. standardne bude soubor error.log
2. log_file.py knihovna pro praci s logem
3. kazdy zaznqam logu bude vypadat:
    ---------------------------------------------------
    datum, cas *** error/warning/info *** vlastni text zpravy
    ---------------------------------------------------
"""
from datetime import datetime

LOG_FILE = "error.log"
ERROR_MESSAGE = "Error"
WARNING_MESSAGE = "Warning"
INFO_MESSAGE = "Info"
MESSAGE_DEVIDER = "---------------------------------------------------"
USE_MESAGE_DEVIDER = True


class ErrorLogFile:
    def __init__(self, file_name=None, **kwargs):
        if file_name is None:
            self.file_name = LOG_FILE
        else:
            self.file_name = file_name

        # Default hodnoty internich parametru
        self.message_devider = MESSAGE_DEVIDER
        self.use_message_devider = USE_MESAGE_DEVIDER

        # Pretizime interni default parametry a dokonce muzeme zavest i nove podle potreby
        for key, value in kwargs.items():
            self.__setattr__(key, value)

    def _write_log_message(self, msg, message_type=ERROR_MESSAGE):
        with open(self.file_name, "a") as log_file:
            log_file.write(f"{message_type} *** {msg}\n")
            if self.use_message_devider:
                log_file.write(f"{self.message_devider}\n")

    def error_message(self, msg):
        self._write_log_message(msg, message_type=ERROR_MESSAGE)

    def warning_message(self, msg):
        self._write_log_message(msg, message_type=WARNING_MESSAGE)

    def info_message(self, msg):
        self._write_log_message(msg, message_type=INFO_MESSAGE)


if __name__ == "__main__":
    log = ErrorLogFile()
    # log = ErrorLogFile(message_devider='******************************')
    log.error_message("Tvrda chyba priogramu")
    log.warning_message("Jmeno zapsano malymi pismeny")
    log.info_message("Nacteno 20 kontaktu ze souboru")
    # log._write_log_message("Uz je pomalu cas jit do hajan", "LOUCENI")

