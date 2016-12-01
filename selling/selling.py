# data structure:
# id: string
#     Unique and random generated (at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter)
# title: string
# price: number (the actual selling price in $)
# month: number
# day: number
# year: number
# month,year and day combined gives the date the purchase was made


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
     menu_elements = ["Show_table",
                     "Add",
                     "Remove",
                     "Update",
                     "Lowest price item",
                     "Items sold between"]
     ui.print_menu("Selling", menu_elements, "Back to main menu")
     choose()

def choose():
    inputs = ui.get_inputs(["Please enter a number: "], "")
    option = inputs[0]
    if option == "1":
        show_table(data_manager.get_table_from_file("selling/sellings.csv"))
    elif option == "2":
        add(data_manager.get_table_from_file("selling/sellings.csv"))
    elif option == "3":
        remove(data_manager.get_table_from_file(
            "selling/sellings.csv"), ui.get_inputs(["Enter id"], ""))
    elif option == "4":
        update(data_manager.get_table_from_file(
            "selling/sellings.csv"), ui.get_inputs(["Enter id"], ""))
    elif option == "5":
        get_lowest_price_item_id(data_manager.get_table_from_file(
            "selling/sellings.csv"))
    elif option == "6":
        inputs = ui.get_inputs(["month_from", "day_from", "year_from", "month_to", "day_to", "year_to"], "Enter dates" )
        get_items_sold_between(data_manager.get_table_from_file(
            "selling/sellings.csv"),inputs[0], inputs[1], inputs[2], inputs[3], inputs[4], inputs[5])
    elif option == "0":
        pass
    else:
        raise KeyError("There is no such option.")


# print the default table of records from the file
#
# @table: list of lists
def show_table(table):
    title_list = common.get_selling_structure_elements()
    ui.print_table(table, title_list)
    start_module()


# Ask a new record as an input from the user than add it to @table, than return @table
#
# @table: list of lists
def add(table):
    structure_elements = common.get_selling_structure_elements()
    ID = common.generate_random(table)

    new_entry = ui.get_inputs(
        structure_elements[1::], "Selling - Add Entry")

    new_entry.insert(0, ID)
    table.append(new_entry)

    data_manager.write_table_to_file("selling/sellings.csv", table)
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

    data_manager.write_table_to_file("selling/sellings.csv", table)
    return table



# Update the record in @table having the id @id_ by asking the new data from the user,
# than return @table
#
# @table: list of lists
# @id_: string
def update(table, id_):
    ID = id_[0]
    index_id = 0
    structure_elements = common.get_selling_structure_elements()

    for i in range(0, len(table)):
        if (table[i][index_id] == id_[index_id]):
            table.remove(table[i])
            updated_entry = ui.get_inputs(structure_elements[1::], "")
            updated_entry.insert(0, ID)
            table.insert(i, updated_entry)
            break

    data_manager.write_table_to_file("selling/sellings.csv", table)
    return table


# special functions:
# ------------------

# the question: What is the id of the item that sold for the lowest price ?
# return type: string (id)
# if there are more than one with the lowest price, return the first of descending alphabetical order
def get_lowest_price_item_id(table):
    lowest_price = 9999999999999999999
    for i in range(0, len(table)):
        if int(table[i][2]) < lowest_price:
            lowest_price = int(table[i][2])
    for i in table:
        if int(i[2]) == lowest_price:
            ui.print_result(i[0], "The id of item sold on lowest price")
            return i[0]


# the question: Which items are sold between two given dates ? (from_date < birth_date < to_date)
# return type: list of lists (the filtered table)
def get_items_sold_between(table, month_from, day_from, year_from, month_to, day_to, year_to):
    filtered_table = []
    for i in table:
        if int(year_from) < int(i[5]) and int(year_to) > int(i[5]) \
            and int(month_from) < int(i[3]) and int(month_to) > int(i[3]) \
            and int(day_from) < int(i[4]) and int(day_to) > int(i[4]):
            filtered_table.append(i)
    ui.print_result(filtered_table, "items between dates")
    return filtered_table
