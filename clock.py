#Sanya Sinha
# 25 October, 2023

import datetime

class Clock:
    def __init__(self, hour=0, minute=0, second=0):
        self.set_hour(hour)
        self.set_minute(minute)
        self.set_second(second)

    def __str__(self):
        return f"{self._hour:02}:{self._minute:02}:{self._second:02}"

    __repr__ = __str__

    def hour(self):
        return self._hour

    def minute(self):
        return self._minute

    def second(self):
        return self._second

    def set_hour(self, new_hour):
        if 0 <= new_hour <= 23:
            self._hour = new_hour
        else:
            raise ValueError("Hour should be between 0 and 23 inclusive.")

    def set_minute(self, new_minute):
        if 0 <= new_minute <= 59:
            self._minute = new_minute
        else:
            raise ValueError("Minute should be between 0 and 59 inclusive.")

    def set_second(self, new_second):
        if 0 <= new_second <= 59:
            self._second = new_second
        else:
            raise ValueError("Second should be between 0 and 59 inclusive.")

    def advance_hour(self, amount_to_advance):
        if amount_to_advance >= 0:
            self._hour = (self._hour + amount_to_advance) % 24
        else:
            raise ValueError("Cannot advance by a negative amount.")

    def advance_minute(self, amount_to_advance):
        if amount_to_advance >= 0:
            self._minute += amount_to_advance
            while self._minute > 59:
                self._minute -= 60
                self.advance_hour(1)
        else:
            raise ValueError("Cannot advance by a negative amount.")

    def set_to_current_time(self):
        now = datetime.datetime.now()
        self.set_hour(now.hour)
        self.set_minute(now.minute)
        self.set_second(now.second)

    def __eq__(self, other):
        if isinstance(other, Clock):
            return self._hour == other.hour() and self._minute == other.minute() and self._second == other.second()
        return False

    def __lt__(self, other):
        if isinstance(other, Clock):
            return (self._hour, self._minute, self._second) < (other.hour(), other.minute(), other.second())
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Clock):
            return (self._hour, self._minute, self._second) > (other.hour(), other.minute(), other.second())
        return NotImplemented


