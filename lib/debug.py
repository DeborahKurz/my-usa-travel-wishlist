#!/usr/bin/env python3
# lib/debug.py
from models.__init__ import CONN, CURSOR
from models.state import State
from models.city import City

def reset_database():
    City.drop_table()
    State.drop_table()
    State.create_table()
    City.create_table()
    #seed data
    colorado = State.create("Colorado")
    florida = State.create("Florida")
    hawaii = State.create("Hawaii")
    City.create("Denver", "Museum Of Natural History", colorado.id)
    City.create("Dinosaur", "Dinosaur National Monument", colorado.id)
    City.create("Marathon", "Dolphin Research Center", florida.id)
    City.create("Key West", "Mile Marker 0", florida.id)
    City.create("Maui", "Scenic Drive", hawaii.id)
    City.create("Maui", "Sea Turtle Tour", hawaii.id)

breakpoint()