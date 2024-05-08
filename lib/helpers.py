# lib/helpers.py
from models.state import State
from models.city import City

def exit_program():
    print("Happy Travels!")
    exit()

def list_states():
    states = State.get_all()
    if len(states) > 0:
        print(f'\nYour saved States include: ')
        for i, state in enumerate(states, start=1):
            print(f'{i}. {state.name}')
    else:
        print("\nYou don't have any saved States. Add one to get started!")

def choose_state():
    states = State.get_all()
    chosen_state = input("\nEnter the number corresponding to the State you would like to view: \n")
    state = states[int(chosen_state) -1]
    return state

def delete_state():
    states = State.get_all()
    chosen_state = input("\nEnter the number corresponding to the State you would like to delete: \n")
    state = states[int(chosen_state) -1]
    for city in state.cities():
        City.delete(city)
    State.delete(state)

def add_state():
    new_state = input("\nWhat State do you want to add to your travel list?: \n")
    if isinstance(new_state, str) and len(new_state):
        try:
            State.create(new_state)
            print(f'\n\nAmazing! {new_state} has been added to your list!')
        except Exception as exc:
            print("Oh no! We ran into an error while saving your State: ", exc)
    else:
        print("Oops! Your new State must be a word with atleast 1 character.")

def list_cities(state):
    cities = City.get_all()
    city_list = [city for city in cities if city.state_id == state.id]
    separator()
    print(f'You are in {state.name}! (Or atleast in your {state.name} Menu...)\n')
    if len(city_list) > 0:
        print("Your cities include:")
        for i, city in enumerate(city_list, start=1):
            print(f'{i}. {city.name}: {city.attraction}')
    else:
        print("Please add a city!")

def add_city(state):
    state_id = state.id
    name = input("\nWhat city do you want to add?: \n")
    attraction = input("\nWhat specifically do you want to visit/do in this city?: \n")
    try:
        City.create(name, attraction, state_id)
        print(f'Hooray! {name} ({attraction}) has been added to your list!')
    except Exception as exc:
        print("Oh no! We ran into an error while saving your city: ", exc)

def delete_city(state):
    cities = City.get_all()
    city_list = [city for city in cities if city.state_id == state.id]
    chosen_city = int(input("\nEnter the number corresponding to the City you would like to delete: \n"))
    city = city_list[int(chosen_city) -1]
    City.delete(city)
    print("\nYour list has been updated.")
    
def separator():
    print("\n************************************************************\n")