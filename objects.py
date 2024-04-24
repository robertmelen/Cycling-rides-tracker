class Cyclist:
    def __init__(self, name, dob, age, skill_level ) -> None:
        self.name = name
        self.dob = dob
        self.age = age
        self.skill_level = skill_level

class Ride:
    def __init__(self, name, date, length, location, start, finish, start_time) -> None:
        self.name = name
        self.date = date
        self.length = length
        self.location = location
        self.start = start
        self.finish = finish
        self.start_time = start_time
        self.cyclists = []

    def add_cyclist(self, cyclist_name):
        self.cyclists.append(cyclist_name)
