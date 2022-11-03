import datetime

class Event():
    def __init__(self, name, date, num_of_guests, room_location, description):
        self.name=name
        self.date=date
        self.num_of_guests=num_of_guests
        self.room_location=room_location
        self.description=description
