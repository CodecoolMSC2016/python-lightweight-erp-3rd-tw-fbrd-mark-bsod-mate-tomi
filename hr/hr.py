# data structure:
# id: string
#     Unique and random generated (at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter)
# name: string
# birth_date: number (year)


# importing everything you need
import os
from importlib.machinery import SourceFileLoader
current_file_path = os.path.dirname(os.path.abspath(__file__))
# User interface module
ui = SourceFileLoader("ui", current_file_path + "/../ui.py").load_module()
# data manager module
data_manager = SourceFileLoader("data_manager", current_file_path + "/../data_manager.py").load_module()
# common module
common = SourceFileLoader("common", current_file_path + "/../common.py").load_module()


# start this module by a module menu like the main menu
# user need to go back to the main menu from here
# we need to reach the default and the special functions of this module from the module menu
#
def start_module():
    list_functions = ["Show table", "Add", "Remove", "Update", "Available tools", "Average durability by manufacturers"]
    ui.print_menu("Hr manager", list_functions, "Back to main menu")
    choose()

def choose():
    inputs = ui.get_inputs(["Please enter a number: "], "")
    option = inputs[0]
    if option == "1":
        show_table(data_manager.get_table_from_file("hr/persons.csv"))
    elif option == "2":
        add(data_manager.get_table_from_file("hr/persons.csv"))
    elif option == "3":
        remove(data_manager.get_table_from_file("hr/persons.csv"), ui.get_inputs(["Enter an ID: "], ""))
    elif option == "4":
        update(data_manager.get_table_from_file("hr/persons.csv"), ui.get_inputs(["Enter an ID: "], ""))
    elif option == "5":
        get_available_tools(data_manager.get_table_from_file("hr/persons.csv"))
    elif option == "6":
        get_average_durability_by_manufacturers(data_manager.get_table_from_file("hr/persons.csv"))
    elif option == "0":
        sys.exit(0)
    else:
        raise KeyError("There is no such option.")

# print the default table of records from the file
#
# @table: list of lists
def show_table(table):
    title_list = ["ID", "Name", "Date of birth"]
    ui.print_table(data_manager.get_table_from_file("hr/persons.csv"), title_list)
    start_module()
#    pass

# Ask a new record as an input from the user than add it to @table, than return @table
#
# @table: list of lists
def add(table):
    title_list = ["ID", "Name", "Date of birth"]
    ID = common.generate_random(table)
    new_record = ui.get_inputs(title_list, " ")
    table.append(new_record)

#    return table
    data_manager.writ_table_to_file("hr/export_hr.csv", table)

# Remove the record having the id @id_ from the @list, than return @table
#
# @table: list of lists
# @id_: string
def remove(table, id_):
    for i in range(len(table)):
        if (table[i][0] == id_[0]):
            table.remove(table[i])
#            del table[i]
            break
    data_manager.write_table_to_file("hr/export_hr.csv", table)

    return table


# Update the record in @table having the id @id_ by asking the new data from the user,
# than return @table
#
# @table: list of lists
# @id_: string
def update(table, id_):

    # your code

    return table


# special functions:
# ------------------

# the question: Who is the oldest person ?
# return type: list of strings (name or names if there are two more with the same value)
def get_oldest_person(table):

    # your code

    pass


# the question: Who is the closest to the average age ?
# return type: list of strings (name or names if there are two more with the same value)
def get_persons_closest_to_average(table):

    # your code

    pass
