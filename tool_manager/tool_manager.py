# data structure:
# id: string
#     Unique and random generated (at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter)
# name: string
# manufacturer: string
# purchase_date: number (year)
# durability: number (year)


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

    menu_elements = ["Show table", "Add", "Remove", "Update",
                     "Available tools", "Avg Durability by manufacturer"]

    ui.print_menu("Tool manager", menu_elements, "Back to main menu")
    choose()


def choose():
    inputs = ui.get_inputs(["Please enter a number: "], "")
    option = inputs[0]
    if option == "1":
        show_table(data_manager.get_table_from_file("tool_manager/tools.csv"))
    elif option == "2":
        add(data_manager.get_table_from_file("tool_manager/tools.csv"))
    elif option == "3":
        remove(data_manager.get_table_from_file(
            "tool_manager/tools.csv"), ui.get_inputs(["Enter id"], ""))
    elif option == "4":
        update(data_manager.get_table_from_file(
            "tool_manager/tools.csv"), ui.get_inputs(["Enter id"], ""))
    elif option == "5":
        get_available_tools()
    elif option == "6":
        get_average_durability_by_manufacturers()
    elif option == "0":
        pass
    else:
        raise KeyError("There is no such option.")


# print the default table of records from the file
#
# @table: list of lists
def show_table(table):
    ui.print_table(table, common.get_tool_manager_structure_elements())


# Ask a new record as an input from the user than add it to @table, than return @table
#
# @table: list of lists
def add(table):
    structure_elements = common.get_tool_manager_structure_elements()

    ID = common.generate_random(table)

    new_entry = ui.get_inputs(structure_elements[1::], "")
    new_entry.insert(0, ID)

    table.append(new_entry)

    data_manager.write_table_to_file("tool_manager/export_tools.csv", table)


# Remove the record having the id @id_ from the @list, than return @table
#
# @table: list of lists
# @id_: string
def remove(table, id_):
    index_id = 0

    for i in range(0, len(table)):
        if (table[i][index_id] == id_):
            table.remove(table[i])
            break

    data_manager.write_table_to_file("tool_manager/export_tools.csv", table)


# Update the record in @table having the id @id_ by asking the new data from the user,
# than return @table
#
# @table: list of lists
# @id_: string
def update(table, id_):
    index_id = 0

    for i in range(0, len(table)):
        if (table[i][index_id] == id_):
            table.remove(table[i])
            updated_entry = ui.get_inputs(structure_elements[1::], "")
            table.insert(i, updated_entry)
            break

    data_manager.write_table_to_file("tool_manager/export_tools.csv", table)


# special functions:
# ------------------

# the question: Which items has not yet exceeded their durability ?
# return type: list of lists (the inner list contains the whole row with their actual data types)
#
# @table: list of lists
def get_available_tools(table):

    # your code

    pass


# the question: What are the average durability time for each manufacturer?
# return type: a dictionary with this structure: { [manufacturer] : [avg] }
#
# @table: list of lists
def get_average_durability_by_manufacturers(table):

    # your code

    pass
