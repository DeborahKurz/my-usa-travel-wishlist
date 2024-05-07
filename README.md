# My U.S.A Travel Wishlist (States & Cities)
Welcome to my travel wishlist app (USA edition)!

Do you want to keep track of the USA States (and cities in them) that you would like to visit one day? Then this app is for you! Add a State, then add Cities to that State. You can even include a note about *what* you want to do in each city. When you visit a destination during your travels you can come back and update your wishlist by deleting that city (or State) from your list.

This is a Python application that uses a CLI (command line interface) as a menu to enable you to save States and Cities. Data is stored in "states" and "cities" tables, and requests are made to these tables using SQL.

Are you ready to get started?

## Yes please! Let's get started!
Awesome! I'm so excited you will be using this app.
To get things up and running you have a few tasks to complete:

1. **Fork** this app into your Github account.
2. **Copy** this app (Code -> SSH -> *copy*)
3. **Clone:** Open your Terminal and run ```$ git clone then_paste_your_copy_here``
4. **Install Dependencies** by running these two commands:
    1. ```console
        pipenv install
    ```
    2. ```console
        pipenv shell
    ```
5. **Start The App:** To enter the app, run the following command in your terminal: 
    ```console
        python lib/cli.py
    ```

That's it! You are ready to add to your own wishlist!

Want an example of the program before you add your own states? Follow these additional steps: NOTE: DO NOT RUN THESE COMMANDS AFTER YOU HAVE ADDED YOUR WISHLIST. IF YOU DO, YOUR STATES AND CITIES WILL BE DELETED.
6. **Get The Example Working:** In your terminal, exit out of the program (type $ `0`). Then run the following commands:
    ```console
        python lib/debug.py
        reset_database()
        exit()
    ```
7. **Repeat Step 5.** You will now be able to view examples of States and cities.
When you are ready to start your own wishlist, delete the examples and add a State to begin!

## Want to know more about this app?
Sure thing! This application stores your wishlisted States and cities in the `travel.db` file where you will find two tables: 

"states" Table:
| id | name |
| ----------- | ----------- |
|id integer | State name |

"cities" Table:
| id | name | attraction | state_id (foreign key) |
| ----------- | ----------- | ----------- | ----------- |
|id integer | State name | Attraction | Corresponding State id |

### CLI
In order to present cleaner code, the user view was broken into two files:
**cli.py** and **helpers.py**
`cli.py` handles the menus, and helpers.py handles user input and calling our Model's methods.

#### cli.py:
This file gives you the menus that are visible in the CLI and calls methods in `helpers.py` (which call methods that handle SQL in our models).
**`menu()` and `main()`** work together as the main menu (the one we see when we start the app in our CLI). They include the following options:
    1. See all saved U.S. States (this allows you to see all the States they ahve added to the wishlist)
    2. Add a new U.S. State (this lets you add a new State to your wishlist)
    3. View a State's details (this asks you to choose a State and then shows you the details of that state which include the cities you have added and notes on what specifically you want to see/do in each city. Under the hood, this option will take you to the "city menu" described below)
    4. Delete a State (this option is used to delete a State and its corresponding cities from your wishlist)
    5. Exit the program (this is pretty self explainitory: when you are done adding to or updating your wishlist, you can select this option to exit the program)
**`sub_menu` and `cities_loop`** work together to create a second menu designed specifically for handling your saved cities. This menu includes the following options:
    1. Add a new city (this allows you to add a new city to the State you are currently in)
    2. Delete a city (this lets you to remove a city from your wishlist)
    3. Return to the 'States' Menu (this is how you return to the "main menu")




### Models
This application does not use SQLAlchemy, so, in the "models" folder `lib/models`, you will find two Python files (**`city.py`** and **`state.py`**) with SQL statements.

The methods in these files include:
__init__() a method that initalizes 

## Introduction

You now have a basic idea of what constitutes a CLI. Fork and clone this lesson
for a project template for your CLI.

Take a look at the directory structure:

```console
.
├── Pipfile
├── Pipfile.lock
├── README.md
└── lib
    ├── models
    │   ├── __init__.py
    │   └── model_1.py
    ├── cli.py
    ├── debug.py
    └── helpers.py
```

Note: The directory also includes two files named `CONTRIBUTING.md` and
`LICENSE.md` that are specific to Flatiron's curriculum. You can disregard or
delete the files if you want.

---

## Generating Your Environment

You might have noticed in the file structure- there's already a Pipfile!

Install any additional dependencies you know you'll need for your project by
adding them to the `Pipfile`. Then run the commands:

```console
pipenv install
pipenv shell
```

---

## Generating Your CLI

A CLI is, simply put, an interactive script and prompts the user and performs
operations based on user input.

The project template has a sample CLI in `lib/cli.py` that looks like this:

```py
# lib/cli.py

from helpers import (
    exit_program,
    helper_1
)


def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            helper_1()
        else:
            print("Invalid choice")


def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. Some useful function")


if __name__ == "__main__":
    main()
```

The helper functions are located in `lib/helpers.py`:

```py
# lib/helpers.py

def helper_1():
    print("Performing useful function#1.")


def exit_program():
    print("Goodbye!")
    exit()
```

You can run the template CLI with `python lib/cli.py`, or include the shebang
and make it executable with `chmod +x`. The template CLI will ask for input, do
some work, and accomplish some sort of task.

Past that, CLIs can be whatever you'd like, as long as you follow the project
requirements.

Of course, you will update `lib/cli.py` with prompts that are appropriate for
your application, and you will update `lib/helpers.py` to replace `helper_1()`
with a useful function based on the specific problem domain you decide to
implement, along with adding other helper functions to the module.

In the `lib/models` folder, you should rename `model_1.py` with the name of a
data model class from your specific problem domain, and add other classes to the
folder as needed. The file `lib/models/__init__.py` has been initialized to
create the necessary database constants. You need to add import statements to
the various data model classes in order to use the database constants.

You are also welcome to implement a different module and directory structure.
However, your project should be well organized, modular, and follow the design
principal of separation of concerns, which means you should separate code
related to:

- User interface
- Data persistence
- Problem domain rules and logic

---

## Updating README.md

`README.md` is a Markdown file that should describe your project. You will
replace the contents of this `README.md` file with a description of **your**
actual project.

Markdown is not a language that we cover in Flatiron's Software Engineering
curriculum, but it's not a particularly difficult language to learn (if you've
ever left a comment on Reddit, you might already know the basics). Refer to the
cheat sheet in this assignments's resources for a basic guide to Markdown.

### What Goes into a README?

This README serves as a template. Replace the contents of this file to describe
the important files in your project and describe what they do. Each Python file
that you edit should get at least a paragraph, and each function should be
described with a sentence or two.

Describe your actual CLI script first, and with a good level of detail. The rest
should be ordered by importance to the user. (Probably functions next, then
models.)

Screenshots and links to resources that you used throughout are also useful to
users and collaborators, but a little more syntactically complicated. Only add
these in if you're feeling comfortable with Markdown.

---

## Conclusion

A lot of work goes into a good CLI, but it all relies on concepts that you've
practiced quite a bit by now. Hopefully this template and guide will get you off
to a good start with your Phase 3 Project.

Happy coding!

---

## Resources

- [Markdown Cheat Sheet](https://www.markdownguide.org/cheat-sheet/)
