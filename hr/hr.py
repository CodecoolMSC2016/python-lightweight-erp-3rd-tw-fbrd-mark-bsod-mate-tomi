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
data_manager = SourceFileLoader(
    "data_manager", current_file_path + "/../data_manager.py").load_module()
# common module
common = SourceFileLoader(
    "common", current_file_path + "/../common.py").load_module()

YEARS = 2
NAMES = 1

# start this module by a module menu like the main menu
# user need to go back to the main menu from here
# we need to reach the default and the special functions of this module from the module menu
#


def start_module():
    list_functions = ["Show table", "Add", "Remove", "Update",
                      "Get oldest person", "Get persons closest to average"]
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
        remove(data_manager.get_table_from_file("hr/persons.csv"), ui.get_inputs(["Enter id"], ""))
    elif option == "4":
        update(data_manager.get_table_from_file("hr/persons.csv"), ui.get_inputs(["Enter id"], ""))
    elif option == "5":
        get_oldest_person(data_manager.get_table_from_file("hr/persons.csv"))
    elif option == "6":
        get_persons_closest_to_average(data_manager.get_table_from_file("hr/persons.csv"))
    elif option == "0":
        pass
    else:
        raise KeyError("There is no such option.")

# print the default table of records from the file
#
# @table: list of lists


def show_table(table):
    structure_elements = common.get_hr_structure_elements()
    ui.print_table(table, structure_elements)
    start_module()

# Ask a new record as an input from the user than add it to @table, than return @table
#
# @table: list of lists


def add(table):
    structure_elements = common.get_hr_structure_elements()
    ID = common.generate_random(table)
    new_entry = ui.get_inputs(structure_elements[1::], " ")
    new_entry.insert(0, ID)
    table.append(new_entry)
    data_manager.write_table_to_file("hr/persons.csv", table)
    return table
# Remove the record having the id @id_ from the @list, than return @table
#
# @table: list of lists
# @id_: string


def remove(table, id_):
    index_id = 0
    for i in range(0, len(table)):
        if table[i][index_id] == id_[index_id]:
            table.remove(table[i])
            break

    data_manager.write_table_to_file("hr/persons.csv", table)
    return table

# Update the record in @table having the id @id_ by asking the new data from the user,
# than return @table
#
# @table: list of lists
# @id_: string


def update(table, id_):
    ID = id_[0]
    index_id = 0
    structure_elements = common.get_hr_structure_elements()
    ID = common.generate_random(table)
    for i in range(0, len(table)):
        if (table[i][index_id] == id_[index_id]):
            table.remove(table[i])
            update_entry = ui.get_inputs(structure_elements[1::], "")
            update_entry.insert(0, ID)
            table.insert(i, update_entry)
            break
    data_manager.write_table_to_file("hr/persons.csv", table)
    return table

# special functions:
# ------------------

# the question: Who is the oldest person ?
# return type: list of strings (name or names if there are two more with
# the same value)


def get_oldest_person(table):
    data_manager.get_table_from_file("hr/persons.csv")
    oldest_persons = []
    oldest = 999999
    for row in range(len(table)):
        if int(table[row][YEARS]) < oldest:
            oldest = int(table[row][YEARS])
    for row in table:
        if int(row[YEARS]) == oldest:
            oldest_persons.append(row[NAMES])
    ui.print_result(oldest_persons, "The oldest person is/are: ")
    return oldest_persons

# the question: Who is the closest to the average age ?
# return type: list of strings (name or names if there are two more with
# the same value)


def get_persons_closest_to_average(table):
    sum_years = 0
    for item in table:
        sum_years += int(item[YEARS])

    average = sum_years / len(table)
    average_difference = []

    for item in range(len(table)):
        difference = int(table[item][YEARS]) - average
        average_difference.append(abs(difference))

    min_diff = 0
    for difference in range(len(average_difference)):
        if int(average_difference[difference]) < average_difference[min_diff]:
            min_diff = difference

    closest_names = []
    closest_names.append(table[min_diff][NAMES])
    ui.print_result(closest_names, "Closest to average: ")
    return closest_names
