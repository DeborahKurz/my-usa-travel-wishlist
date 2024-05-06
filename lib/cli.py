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
            delete_state()
        else:
            print("Invalid choice")

def cities_loop(state):
    list_cities(state)
    sub_menu(state)
    choice = input("> ")
    if choice == "0":
        main()
    elif choice == "1":
        add_city(state)
    elif choice == "2":
        delete_city(state)
    else:
        print("Invalid choice")


def menu():
    separator()
    print("Please select an option:")
    print("0. Exit the program")
    print("1. List all saved U.S. States")
    print("2. Add a new U.S. State")
    print("3. View details of a State")
    print("4. Delete a State")

def sub_menu(state):
    separator()
    print(f'Please select an option:')
    print("0. Return to the main menu")
    print("1. Add a new city")
    print("2. Delete a city")


if __name__ == "__main__":
    main()