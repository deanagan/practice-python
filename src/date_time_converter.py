from datetime import datetime as dt


def date_time(time: str) -> str:
    dtc = dt.strptime(time, "%d.%m.%Y %H:%M")
    hour = 'hour' if dtc.hour == 1 else 'hours'
    minute = 'minute' if dtc.minute == 1 else 'minutes'
    return f"{dtc.day} {dtc.strftime('%B')} {dtc.year} year {dtc.hour} {hour} {dtc.minute} {minute}"
