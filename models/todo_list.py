from models.event import *
import datetime


event1 = Event(datetime.date(2022, 12, 6), "Misha's birthday", 25, "Edinburgh", "birthday party", True)
event2 = Event(datetime.date(2023, 2, 24), "Effie's birthday", 30, "Edinburgh", "birthday party", True)
event3 = Event(datetime.date(2022, 11, 4), "CodeClan lesson", 22, "Edinburgh", "Career talks", False)
events = [event1, event2, event3]

def add_new_event(event):
    events.append(event)
