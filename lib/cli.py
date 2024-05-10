# lib/cli.py

from helpers import (
    exit_program,
    list_states,
    add_state,
    choose_state,
    delete_state,
    list_cities,
    add_city,
    delete_city,
    separator
)


def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            list_states()
        elif choice == "2":
            add_state()
        elif choice == "3":
            state = choose_state()
            cities_loop(state)
        elif choice == "4":
            list_states()
            delete_state()
        else:
            print("Oops... We don't know what to do with that choice. \n Please select a number based on the options.")

def cities_loop(state):
    if state:
        separator()
        print(f'You are in {state.name}! (Or atleast in your {state.name} Menu...)\n')
        list_cities(state)
        sub_menu(state)
        choice = input("> ")
        if choice == "0":
            main()
        elif choice == "1":
            list_cities(state)
            add_city(state)
            cities_loop(state)
        elif choice == "2":
            list_cities(state)
            delete_city(state)
            cities_loop(state)
        else:
            print("Invalid choice: Please choose a number from the menu.")
        cities_loop(state)
    else:
        print("Need help coming up with a State?\nThink about what places you've always wanted to visit.")

def menu():
    separator()
    print("Save & Manage your U.S.A travel wishlist!")
    print("------------------------------------------------------------")
    print("You are in your U.S.A States Menu. Please select an option below: \n")
    print("1. See all saved U.S. States")
    print("2. Add a new U.S. State")
    print("3. View a State's details")
    print("4. Delete a State")
    print("0. Exit this program")

def sub_menu(state):
    separator()
    print(f"Please select an option: \n")
    print("1. Add a new city")
    print("2. Delete a city")
    print("0. Return to the 'States' Menu")


if __name__ == "__main__":
    main()