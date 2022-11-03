from models.events import Event
import datetime

event1= Event("80s party", datetime.date(2022, 11, 2), 50, "Assembly room", "Social event with dancing class")
event2= Event("Techno night", datetime.date(2022, 11, 27), 60, "Cellar", "Rave, no food, host to provide DJ" )

events_list=[event1,event2]

def add_new_event(event):
    events_list.append(event)

#name, date, num_of_guests, room_location, description