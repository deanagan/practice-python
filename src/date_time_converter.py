from datetime import datetime as dt, time as dttime

''' Converts date time to readable string '''
def date_time(time: str) -> str:
    dtc = dt.strptime(time, "%d.%m.%Y %H:%M")
    hour = 'hour' if dtc.hour == 1 else 'hours'
    minute = 'minute' if dtc.minute == 1 else 'minutes'
    return f"{dtc.day} {dtc.strftime('%B')} {dtc.year} year {dtc.hour} {hour} {dtc.minute} {minute}"

''' Converts 12h time format to 24h format '''
def time_converter(time: str):
    def adjust_hour(hour: str, fmt: str):
        hour_num = int(hour)
        return {
            'pm': lambda: str(hour_num + 12) if hour_num != 12 else hour,
            'am': lambda: '00' if hour_num == 12 else hour,
        }.get(fmt, lambda: hour)()

    adjtime = time.replace('.','')
    (h, m), fmt = (t.split(':') if 'm' not in t else t for t in adjtime.split())

    return dttime(int(adjust_hour(h, fmt)), int(m)).strftime('%H:%M')