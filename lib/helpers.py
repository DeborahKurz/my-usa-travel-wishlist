# lib/helpers.py
from models.state import State
from models.city import City

def exit_program():
    print("Happy Travels!")
    exit()

def list_states():
    states = State.get_all()
    line_break()
    print(f'Your saved States include: ')
    for i, state in enumerate(states, start=1):
        print(f'{i}. {state.name}')

def choose_state():
    states = State.get_all()
    chosen_state = input("Enter the number corresponding to the State you would like to view: ")
    state = states[int(chosen_state) -1]
    return state

def delete_state():
    states = State.get_all()
    chosen_state = input("Enter the number corresponding to the State you would like to delete: ")
    state = states[int(chosen_state) -1]
    State.delete(state)
    line_break()
    print("Your list has been updated.")

def add_state():
    new_state = input("What State do you want to add to your travel list?: ")
    line_break()

    if isinstance(new_state, str) and len(new_state):
        try:
            state = State.create(new_state)
            print(f'Amazing! {new_state} has been added to your list!')
        except Exception as exc:
            print("Oh no! We ran into an error while saving your State: ", exc)
    else:
        print("Oops! Your new State must be a word with atleast 1 character.")

def list_cities(state):
    cities = City.get_all()
    city_list = [city for city in cities if city.state_id == state.id]
    separator()
    print(f'Welcome to {state.name}!')
    line_break()
    if len(city_list) > 0:
        print("Your cities include:")
        for i, city in enumerate(city_list, start=1):
            print(f'{i}. {city.name}: {city.attraction}')
    else:
        print("Please add a city!")


def add_city(state):
    state_id = state.id
    name = input("What city do you want to add?: ")
    attraction = input("What specifically do you want to visit/do in this city?: ")
    line_break()
    try:
        city = City.create(name, attraction, state_id)
        print(f'Hooray! {name} ({attraction}) has been added to your list!')
    except Exception as exc:
        print("Oh no! We ran into an error while saving your city: ", exc)

def delete_city(state):
    cities = City.get_all()
    city_list = [city for city in cities if city.state_id == state.id]
    chosen_city = int(input("Enter the number corresponding to the City you would like to delete: "))
    city = city_list[int(chosen_city) -1]
    City.delete(city)
    line_break()
    print("Your list has been updated.")
    
def separator():
    line_break()
    star_line()
    line_break()

def star_line():
    print("*********************************")

def line_break():
    print("")