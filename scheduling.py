from time_operator import Time
from text_formatter import text_format

def sorting_key(event):
    return event.start.fractional

class Event():
    def __init__(self, title, description, start, end):
        self.title = title
        self.description = description
        self.start = start
        self.end = end

    def overlap(self, other):
        return (other.start < self.end <= other.end) or (other.start <= self.start < other.end)

    def display(self):
        print(text_format.BOLD + text_format.RED + self.title + text_format.END)
        print(text_format.ORANGE + self.description + text_format.END)
        print(text_format.CYAN +
        f'{self.start.hour}:{self.start.minute} - {self.end.hour}:{self.end.minute}' +
        text_format.END)
        print('')
    

class DaySchedule():
    def __init__(self, name):
        self.name = name
        self.events = []

    def add_event(self, new_event, debug = True):
        for event in self.events:
            if new_event.overlap(event):
                if debug:
                    print(f"Error: Unable to add event '{new_event.title}': Overlaps with '{event.title}'.")
                return

        self.events.append(new_event)
        self.events.sort(key = sorting_key)
        if debug:
            print("Successfully added event.")

    def display_events(self):
        print('\n'*4)
        for i in range(len(self.events)):
            print(i+1, end=' - ')
            self.events[i].display()
        print('\n'*4)




# weekday = DaySchedule('Weekday')

# wake_up = Event(title="Wake Up", description="Get out of bed.", start=Time(hour=6, minute=0), end=Time(hour=6,minute=30))
# weekday.add_event(wake_up)

# brush = Event(title="Brush", description="Self-evident, hopefully", start=Time(hour=6, minute=29), end=Time(hour=7,minute=0))
# weekday.add_event(brush)

# weekday.display_events()