"""
Log soubor pro podporu projektu

1. standarne bude soubor error.log
2. log_file.py knihovna pro práci s lohem
knihovna s podpurnou třídou log_file
3. kazdy zaznam logu bude vypadat:
    --------------------------------------------------- #oddelení zaznamu
    datum, cas *** error/warning/info *** vlastni text zpravy
    ---------------------------------------------------
"""
from _datetime import datetime

LOG_FILE = "error.log"
ERROR_MESSAGE = "Error"
WARNING_MESSAGE = "Warning"
INFO_MESSAGE = "Info"
MESSAGE_DEVIDER = "----------------------------------------------------"
USE_MESSAGE_DEVIDER = True

class ErrorLogFile:

    def __init__(self, file_name=None, **kwargs): #v None by mohla byt cela cesta k souboru
        if file_name is None:
            self.file_name = LOG_FILE
        else:
            self.file_name = file_name

        #Default hodnoty internich parametru
        self.messge_devider = MESSAGE_DEVIDER
        self.use_message_devider = USE_MESSAGE_DEVIDER

        #pretizime interni default parametry a dokonce muzeme zavest i nove podle potreby
        for key, value in kwargs:
            self.__setattr__(key, value) #setattr - nastavuje interni atribut podle kwargs

#error_log = ErrorLogFile(message_devider="**********")
#jakoze lze prepsat

    def _write_log_message(self, msg, message_type=ERROR_MESSAGE):
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(self.file_name, "a") as log_file:
            log_file.write(f"{current_time} *** {message_type} *** {msg}\n")
            if self.use_message_devider:
                log_file.write(f"{self.messge_devider}\n")

    def error_message(self, msg):
        self._write_log_message(msg, message_type=ERROR_MESSAGE)

    def warning_message(self, msg):

        self._write_log_message(msg, message_type=WARNING_MESSAGE)

    def info_message(self, msg):
        self._write_log_message(msg, message_type=INFO_MESSAGE)

if __name__ == "__main__":
    log = ErrorLogFile() #sem můžu použít název interní proměnné a hodnotu, např message_devider="*****"
    log.error_message("Tvrda chyba pri programu")
    log.warning_message("jmeno zapsano malymi pismeny")
    log.info_message("Nacteno 20 kontaktu ze souboru")
