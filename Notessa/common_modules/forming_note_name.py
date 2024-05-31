from PySide6.QtCore import QDateTime


def forming_note_file_name(note_type: str) -> str:
    """ Method for forming the name of notes. The input is the type of note that is used as part of the name,
    to which the current date and time is added. """
    current_date_time = QDateTime.currentDateTime()

    note_file_name = (f"{note_type}_{current_date_time.date().day()}-{current_date_time.date().month()}-{current_date_time.date().year()}_"
                      f"{current_date_time.time().hour()}-{current_date_time.time().minute()}-{current_date_time.time().second()}")

    return note_file_name
