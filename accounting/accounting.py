# data structure:
# id: string
#     Unique and random generated (at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter)
# month: number
# day: number
# year: number
# type: string (in = income, out = outcome)
# amount: number (dollar)


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

# used constants
YEAR_INDEX = 3


# start this module by a module menu like the main menu
# user need to go back to the main menu from here
# we need to reach the default and the special functions of this module
# from the module menu
def start_module():
    options = ["Show table", "Add entry", "Remove entry", "Update entry",
               "Get most profitable year", "Get average profit/item"]
    ui.print_menu("\nAccounting", options, "Back to main menu")
    choose()


def read_file(file_name="accounting/items_test.csv"):
    return data_manager.get_table_from_file(file_name)


def choose():
    inputs = ui.get_inputs(["Please enter a number: "], "")
    option = inputs[0]
    if option == "1":
        show_table(read_file())
    elif option == "2":
        data_manager.write_table_to_file(
            "accounting/items_test.csv", add(data_manager.get_table_from_file("accounting/items_test.csv")))
    elif option == "3":
        data_manager.write_table_to_file("accounting/items_test.csv", remove(read_file(), ui.get_inputs(
            ["Enter ID for removal"], "Accounting - Remove Entry")))
    elif option == "4":
        data_manager.write_table_to_file("accounting/items_test.csv",  update(read_file(), ui.get_inputs(
            ["Enter ID for update"], "Accounting - Update")))
    elif option == "5":
        ui.print_result(which_year_max(read_file()),
                        "We had the highest profit in:")
    elif option == "6":
        ui.print_result(avg_amount(read_file(), ui.get_inputs(
            ["Enter a year"], "Accounting - Average profit/item")), "Average profit/item:")
    elif option == "0":
        pass
    else:
        raise KeyError("There is no such option.")


# print the default table of records from the file
#
# @table: list of lists
def show_table(table):
    ui.print_table(table, common.get_accounting_structure_elements())


# Ask a new record as an input from the user than add it to @table, than return @table
#
# @table: list of lists
def add(table):
    structure_elements = common.get_accounting_structure_elements()
    ID = common.generate_random(table)

    new_entry = ui.get_inputs(
        structure_elements[1::], "Accounting - Add Entry")

    new_entry.insert(0, ID)
    table.append(new_entry)

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

    return table


# Update the record in @table having the id @id_ by asking the new data from the user,
# than return @table
#
# @table: list of lists
# @id_: string
def update(table, id_):
    index_id = 0
    structure_elements = common.get_accounting_structure_elements()

    for i in range(0, len(table)):
        if (table[i][index_id] == id_[index_id]):
            table.remove(table[i])
            updated_entry = ui.get_inputs(structure_elements[1::], "")
            updated_entry.insert(0, id_[index_id])
            table.insert(i, updated_entry)
            break

    return table


# special functions:
# ------------------

# the question: Which year has the highest profit? (profit=in-out)
# return the answer (number)
def which_year_max(table):
    yearly_profits = []
    years_in_table = []
    index_max_profit = 0

    # getting all years from table into a list
    for entry in table:
        if int(entry[YEAR_INDEX]) not in years_in_table:
            years_in_table.append(int(entry[YEAR_INDEX]))

    for years in years_in_table:
        yearly_profits.append(common.get_profit_of_year(table, years))

    for profit in range(len(yearly_profits)):
        if yearly_profits[profit] > yearly_profits[index_max_profit]:
            index_max_profit = profit

    return years_in_table[index_max_profit]


# the question: What is the average (per item) profit in a given year? [(profit)/(items count) ]
# return the answer (number)
def avg_amount(table, year):
    given_year = int(year[0])
    items_count_in_year = 0
    sum_profits = 0

    for entry in table:
        if int(entry[YEAR_INDEX]) == given_year:
            items_count_in_year += 1

    sum_profits = common.get_profit_of_year(table, given_year)

    return sum_profits / items_count_in_year
