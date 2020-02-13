from os import path

from scheduling import Event, DaySchedule
from text_formatter import text_format
from time_operator import Time
from terminal_commands import clear

def read_schedule_data(schedule_name, path):
    data = open(path, "r").read().split("\n")
    schedule = DaySchedule(schedule_name)    
    for i in range(len(data)):
        line = data[i]
        attributes = line.split("&")
        if len(attributes) == 6:
            event = Event(title=attributes[0], 
                    description=attributes[1],
                    start=Time(hour=int(attributes[2]), minute=int(attributes[3])),
                    end=Time(hour=int(attributes[4]), minute=int(attributes[5]))
                    )
            schedule.add_event(event, debug = False)
    return schedule

def write_schedule_data(schedule, path):
    f = open(path, "w")
    for event in schedule.events:
        attributes = [event.title, event.description,
                    str(event.start.hour), str(event.start.minute),
                    str(event.end.hour), str(event.end.minute)]
        line = "&".join(attributes)
        f.write(line + "\n")

def add_schedule():
    clear()
    name = input("Enter the name of the new schedule: ")

    f = open("data/schedules", "a")
    f.write(name + "\n")
    f.close()

    # Create data file for schedule
    g = open(f"data/{name}_data", "a")
    g.close()

    print("Successfully added new schedule.")

    stop = input("")
    clear()

def add_event():
    clear()
    valid_names = open("data/schedules", "r").read().split("\n")[:-1]
    print(f"{len(valid_names)} schedules found: " + ", ".join(valid_names) + ".")
    schedule_name = input("Enter the name of the schedule you want to add to: ")
    if schedule_name in valid_names and path.exists(f"data/{schedule_name}_data"):
        schedule = read_schedule_data(schedule_name, f"data/{schedule_name}_data")
        print("\n\nEvents so far:")
        schedule.display_events()

        # Get user event and add it to the schedule
        print("Adding new event...")
        title = input("title: ")
        description = input("description: ")
        print("start time -")
        s_hour = int(input(" "*8 + "hour: "))
        s_minute = int(input(" "*8 + "minute: "))
        print("end time -")
        e_hour = int(input(" "*8 + "hour: "))
        e_minute = int(input(" "*8 + "minute: "))

        schedule.add_event(Event(title=title, description=description,
                                start=Time(s_hour, s_minute),
                                end=Time(e_hour, e_minute)))
        
        write_schedule_data(schedule, f"data/{schedule_name}_data")

    else:
        print("Error: Could not find that schedule.")
        return
    
    stop = input("")
    clear()

def view_schedule():
    clear()
    valid_names = open("data/schedules", "r").read().split("\n")[:-1]
    print(f"{len(valid_names)} schedules found: " + ", ".join(valid_names) + ".")
    schedule_name = input("Enter the name of the schedule you want to view: ")

    if schedule_name in valid_names and path.exists(f"data/{schedule_name}_data"):
        schedule = read_schedule_data(schedule_name, f"data/{schedule_name}_data")
        schedule.display_events()

    else:
        print("Error: Could not find that schedule.")
        return

    stop = input("")
    clear()


if __name__ == "__main__":
    while True:
        clear()
        print("\n"*4)
        print(text_format.BOLD + text_format.RED + "TimeKeeper - Scheduling App" + text_format.END)
        print("\n"*4)
        
        try:
            key = input(text_format.CYAN +
            "View Schedule - 1\n\nAdd Event - 2\n\nAdd Schedule - 3\n\nQuit - Q\n\n" +
            text_format.END)
            if key == "1":
                view_schedule()
            elif key == "2":
                add_event()
            elif key == "3":
                add_schedule()
            elif key == "Q":
                clear()
                break

        except:
            print("Invalid key.")

        stop = input("")
        clear()