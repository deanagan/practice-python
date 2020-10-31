from datetime import datetime as dt
from math import floor

def sun_angle(time: str) -> [int, str]:
    return floor(((dt.strptime(time, '%H:%M') - dt.strptime('06:00', '%H:%M')).seconds // 60) * 0.25)
