from datetime import datetime as dt


def date_time(time: str) -> str:
    dtc = dt.strptime(time, "%d.%m.%Y %H:%M")
    return f"{dtc.day} {dtc.strftime('%B')} {dtc.year} year {dtc.hour} hours {dtc.minute} minutes"
