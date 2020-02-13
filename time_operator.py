def normal_to_frac(hour, minute):
    frac = hour + (minute/60.0)
    return frac

def frac_to_normal(diff):
    hour = abs(int(diff - (diff % 1)))
    minute = abs(int(60*(diff%1)))
    return hour, minute

class Time():
    def __init__(self, hour, minute):
        self.hour = hour
        self.minute = minute
        self.fractional = hour + (minute/60.0)

    # > and >= are inferred
    def __lt__(self, other):
        return self.fractional < other.fractional
    def __le__(self, other):
        return self.fractional <= other.fractional
    def __eq__(self, other):
        return self.fractional == other.fractional

    def __sub__(self, other):
        hour, minute = frac_to_normal(self.fractional - other.fractional)
        return Time(hour, minute)
