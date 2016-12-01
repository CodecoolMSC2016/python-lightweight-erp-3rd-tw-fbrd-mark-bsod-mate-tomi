# data structure:
# id: string
#     Unique and random generated (at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter)
# title: string
# manufacturer: string
# price: number (dollar)
# in_stock: number


# importing everything you need
import os
from importlib.machinery import SourceFileLoader
current_file_path = os.path.dirname(os.path.abspath(__file__))
# User interface module
ui = SourceFileLoader("ui", current_file_path + "/../ui.py").load_module()
# data manager module
data_manager = SourceFileLoader(
    "data_manager", current_file_path + "/../data_manager.py").load_module()
# common module
common = SourceFileLoader(
    "common", current_file_path + "/../common.py").load_module()


# start this module by a module menu like the main menu
# user need to go back to the main menu from here
# we need to reach the default and the special functions of this module from the module menu
#
def start_module():
    menu_elements = ["Show table",
                     "Add",
                     "Remove",
                     "Update",
                     "Kind of games",
                     "Avarage amount of games in stock"]
    ui.print_menu("Store", menu_elements, "Back to main menu")
    choose()


def choose():
    inputs = ui.get_inputs(["Please enter a number: "], "")
    option = inputs[0]
    if option == "1":
        show_table(data_manager.get_table_from_file("store/games.csv"))
    elif option == "2":
        add(data_manager.get_table_from_file("store/games.csv"))
    elif option == "3":
        remove(data_manager.get_table_from_file(
            "store/games.csv"), ui.get_inputs(["Enter id"], ""))
    elif option == "4":
        update(data_manager.get_table_from_file(
            "store/games.csv"), ui.get_inputs(["Enter id"], ""))
    elif option == "5":
        get_counts_by_manufacturers(data_manager.get_table_from_file(
            "store/games.csv"))
    elif option == "6":
        inputs = ui.get_inputs(
            ["manufacturer"], "Enter the name of the manufacturer")
        get_average_by_manufacturer(data_manager.get_table_from_file(
            "store/games.csv"), inputs[0])
    elif option == "0":
        pass
    else:
        raise KeyError("There is no such option.")


# print the default table of records from the file
#
# @table: list of lists
def show_table(table):
    title_list = common.get_store_structure_elements()
    ui.print_table(table, title_list)
    start_module()


# Ask a new record as an input from the user than add it to @table, than return @table
#
# @table: list of lists
def add(table):
    structure_elements = common.get_store_structure_elements()
    ID = common.generate_random(table)

    new_entry = ui.get_inputs(
        structure_elements[1::], "Store - Add Entry")

    new_entry.insert(0, ID)
    table.append(new_entry)

    data_manager.write_table_to_file("store/games_test.csv", table)

    return table


# Remove the record having the id @id_ from the @list, than return @table
#
# @table: list of lists
# @id_: string
def remove(table, id_):
    index_id = 0

    for i in range(0, len(table)):
        if (table[i][index_id] == id_[index_id]):
            table.remove(table[i])
            break

    data_manager.write_table_to_file("store/games_test.csv", table)
    return table


# Update the record in @table having the id @id_ by asking the new data from the user,
# than return @table
#
# @table: list of lists
# @id_: string
def update(table, id_):
    index_id = 0
    structure_elements = common.get_store_structure_elements()
    ID = common.generate_random(table)
    for i in range(0, len(table)):
        if (table[i][index_id] == id_[index_id]):
            table.remove(table[i])
            updated_entry = ui.get_inputs(structure_elements[1::], "")
            updated_entry.insert(0, ID)
            table.insert(i, updated_entry)
            break

    data_manager.write_table_to_file("store/games_test.csv", table)

    return table


# special functions:
# ------------------

# the question: How many different kinds of game are available of each manufacturer?
# return type: a dictionary with this structure: { [manufacturer] : [count] }
def get_counts_by_manufacturers(table):
    GAME_NAME = 1
    PUBLISHER_NAME = 2
    game_repertoire = {}

    for games in table:
        if games[PUBLISHER_NAME] not in game_repertoire:
            pass
    pass


# the question: What is the average amount of games in stock of a given manufacturer?
# return type: number
def get_average_by_manufacturer(table, manufacturer):
    stock_max = 0
    counter = 0
    STOCK = 4
    MANUFACTURER = 2

    for game in table:
        if game[MANUFACTURER] == manufacturer:
            stock_max += int(game[STOCK])
            counter += 1
    ui.print_result(stock_max / counter, "Avarage stock by given manufacturer")
    return stock_max / counter
