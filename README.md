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
    ```console
        pipenv install
        pipenv shell
    ```
5. **Start The App:** Run the following command in your terminal: 
    ```console
        python lib/cli.py
    ```

That's it! You are ready to add to your own wishlist!

Do you want an example of the program before you add your own states? 
Follow these additional steps (NOTE: DO NOT RUN THESE COMMANDS AFTER YOU HAVE ADDED YOUR WISHLIST. IF YOU DO, YOUR STATES AND CITIES WILL BE DELETED):

6. **Get The Example Working:** In your terminal, exit out of the program (type `0`). Then run the following commands:
    ```console
        python lib/debug.py
        reset_database()
        exit()
    ```
    
7. **Repeat Step 5.** You will now be able to view examples of States and cities.
When you are ready to start your own wishlist, delete the examples and add a State to begin!

## Want to know more about this app?
Sure thing! 
Our directory structure is as follows:
```console
.
├── Pipfile
├── Pipfile.lock
├── README.md
├── travel.db
└── lib
    ├── models
    │   ├── __init__.py
    │   ├── city.py
    │   └── state.py
    ├── cli.py
    ├── debug.py
    └── helpers.py
```

This application stores your wishlisted States and cities in the `travel.db` file where you will find two tables: 

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
**`sub_menu()` and `cities_loop()`** work together to create a second menu designed specifically for handling your saved cities. This menu includes the following options:
    1. Add a new city (this allows you to add a new city to the State you are currently in)
    2. Delete a city (this lets you to remove a city from your wishlist)
    3. Return to the 'States' Menu (this is how you return to the "main menu")

`main()` and `cities_loop()` call methods that were placed in the `helpers.py` file in order to make cleaner code.

#### helpers.py:
This file holds some of the code that is called in `cli.py`. It also draws from our `models` folder (`state.py` and `city.py`) to make the `cli.py` menu work.

`helpers.py` imports both the State and City classes and uses them in some of the following methods:
1. `exit_program()`: Uses `exit()` to exit out of our app's CLI menu.
2. `list_states()`: Lists States or alerts you to add a State if you haven't already.
3. `choose_state()`: Handles user input and allows you to choose which State specifically you would like to see details on.
4. `delete_state()`: Calls methods from both `state.py` and `city.py` to delete a State and all it's associated cities from the database.
5. `add_state()`: Takes your input and allows you to add a state to the database.
6. `list_cities()`: Lists all the cities associated with a chosen State, or alerts you to add a city if there aren't any cities in the database (assicoated with the chosen State).
7. `add_city()`: Handles user input and allows you to add a city to the database.
8. `delete_city()`: Deletes a city associated with a chosen State.
9. `separator()`: Creates a line of stars (*) that acts as a separator in the command line.

These methods call on methods in the `models` folder.

### Models
This application does not use SQLAlchemy, so, in the `models` folder (`lib/models`), you will find two Python files (**`state.py`** and **`city.py`**) with SQL statements.

#### state.py:
In the `State` class, two instance attribut is initialized: `id` (the primary key) and `name`. `name` uses the `@property` decorator as a "setter" and "getter". `@property` also validates that the attributes are strings and at least 1 character long.
`city.py` also includes the following methods:
1. `create_table()`: This class method allows us to create a states table in our database if one does not already exist.
2. `drop_table()`: Another class method, but it allows us to delete our states table in the database. Both this method and the one above are used in `debug.py`.
3. `save()`: An instance method that allows us to map an object to a table row in the states database table.
4. `create()`: A class method that draws on `save()` to not only create a new class instance, but also create a new table row in our states database table.
5. `update()`: An instance method that allows us to update a table row.
6. `delete()`: A instance method that deletes a state row from the states table.
7. `instance_from_db()`: A class method that maps to a states table row from our database into an instance of the class.
8. `get_all()`: This class method gets all rows from the states table, makes them into objects, and returns them in a list.
9. `find_by_id()`: A class method that searches our states table's primary keys for a row that matches. It then returns the row as an object.
10. `cities()`: An instance method that gets all the cities associated with a certain state.

#### city.py:
In the `City` class, four instance attributes are initialized: `id` (the primary key) `name`, `attraction`, and `state_id` (the foreign key). `name`, `attraction`, and `state_id` all use the `@property` decorator as a "setter" and "getter". `@property` also validates that the attributes are strings and at least 1 character long.
`city.py` also includes the following methods:
1. `create_table()`: This class method allows us to create a cities table in our database if one does not already exist.
2. `drop_table()`: Another class method, but it allows us to delete our cities table in the database. Both this method and the one above are used in `debug.py`.
3. `save()`: An instance method that allows us to map an object to a table row in the cities database table.
4. `create()`: A class method that draws on `save()` to not only create a new class instance, but also create a new table row in our cities database table.
5. `update()`: An instance method that allows us to update a table row.
6. `delete()`: A instance method that deletes a city row from the cities table.
7. `instance_from_db()`: A class method that maps a cities table row from our database into an instance of the class.
8. `get_all()`: This class method gets all rows from the cities table, makes them into objects, and returns them in a list.
9. `find_by_id()`: A class method that searches our cities table's primary keys for a row that matches. It then returns the row as an object.

### debug.py
`debug.py` holds seed data in `reset_database()`. `reset_database()` should NOT be called if you have added data into this app already (`reset_database()` will delete everything in the database and seed the database).
You can enter into breakpoint in this file by running the following command in your console:
```console
    python lib/debug.py
```

## Happy Coding!