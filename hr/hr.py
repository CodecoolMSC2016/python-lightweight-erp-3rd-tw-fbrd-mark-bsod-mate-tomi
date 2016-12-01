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

YEARS = 2
NAMES = 1

# start this module by a module menu like the main menu
# user need to go back to the main menu from here
# we need to reach the default and the special functions of this module from the module menu
#
def start_module():
    list_functions = ["Show table", "Add", "Remove", "Update", "Get oldest person", "Get persons closest to average"]
    ui.print_menu("Hr manager", list_functions, "Back to main menu")
    choose()

def choose():
    inputs = ui.get_inputs(["Please enter a number: "], "")
    option = inputs[0]
    if option == "1":
        show_table(data_manager.get_table_from_file("hr/persons.csv"))
    elif option == "2":
        data_manager.write_table_to_file("hr/export_hr.csv", add(data_manager.get_table_from_file("hr/persons.csv")))
    elif option == "3":
        data_manager.write_table_to_file("hr/export_hr.csv", remove(data_manager.get_table_from_file("hr/persons.csv"), ui.get_inputs(["Enter an ID: "], "")))
    elif option == "4":
        data_manager.write_table_to_file("hr/export_hr.csv", update(data_manager.get_table_from_file("hr/persons.csv"), ui.get_inputs(["Enter an ID: "], "")))
    elif option == "5":
        get_oldest_person(data_manager.get_table_from_file("hr/persons.csv"))
    elif option == "6":
        get_persons_closest_to_average(data_manager.get_table_from_file("hr/persons.csv"))
    elif option == "0":
        sys.exit(0)
    else:
        raise KeyError("There is no such option.")

# print the default table of records from the file
#
# @table: list of lists
def show_table(table):
    structure_elements = common.get_hr_structure_elements()
    ui.print_table(data_manager.get_table_from_file("hr/persons.csv"), structure_elements)
    start_module()

# Ask a new record as an input from the user than add it to @table, than return @table
#
# @table: list of lists
def add(table):
    structure_elements = common.get_hr_structure_elements()
    ID = common.generate_random(table)
    new_record = ui.get_inputs(structure_elements[1::], " ")
    new_record.insert(0, ID)
    table.append(new_record)

    return table
# Remove the record having the id @id_ from the @list, than return @table
#
# @table: list of lists
# @id_: string
def remove(table, id_):
    index_id = 0
    for i in range(len(table)):
        if str(table[i][index_id]) == str(id_[index_id]):
            table.remove(table[i])
            break

    return table

# Update the record in @table having the id @id_ by asking the new data from the user,
# than return @table
#
# @table: list of lists
# @id_: string
def update(table, id_):
    index_id = 0
    structure_elements = common.get_hr_structure_elements()
    for i in range(len(table)):
        if (table[i][index_id] == id_[index_id]):
            table.remove(table[i])
            update_entry = ui.get_inputs(structure_elements[1::], "")
            update_entry.insert(0, id_[0])
            table.insert(i, update_entry)
            break
    return table

# special functions:
# ------------------

# the question: Who is the oldest person ?
# return type: list of strings (name or names if there are two more with the same value)
def get_oldest_person(table):
    data_manager.get_table_from_file("hr/persons.csv")
    oldest = 999999
    for row in range(len(table)):
        if int(table[row][YEARS]) < oldest:
            oldest = int(table[row][YEARS])
    for row in table:
        if int(row[YEARS]) == oldest:
            ui.print_result(row[NAMES], "The oldest person is: ")


# the question: Who is the closest to the average age ?
# return type: list of strings (name or names if there are two more with the same value)
def get_persons_closest_to_average(table):
    average = 0
    for item in table:
        average += int(item[2])
    average = average / len(table)
    YEARS =
    NAMES =
#
#    pass
