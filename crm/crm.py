# data structure:
# id: string
#     Unique and random generated (at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter)
# name: string
# email: string
# subscribed: boolean (Is she/he subscribed to the newsletter? 1/0 = yes/not)


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
    menu_elements=["Show Table","Add","Remove","Update","Get longest name","Get subscribed ID"]
    ui.print_menu("Customer Relationship Management", menu_elements, "Back to main menu")
    inputs = ui.get_inputs(["Please enter a number: "], "")
    option = inputs[0]
    if option == "1":
        show_table(data_manager.get_table_from_file("crm/customers.csv"))
    elif option == "2":
        add(data_manager.get_table_from_file("crm/customers.csv"))
    elif option == "3":
        remove(data_manager.get_table_from_file("crm/customers.csv"),id_ = ui.get_inputs(["Please enter an ID"], ""))
    elif option == "4":
        update(data_manager.get_table_from_file("crm/customers.csv"),id_ = ui.get_inputs(["Please enter an ID"], ""))
    elif option == "5":
        get_longest_name_id(data_manager.get_table_from_file("crm/customers.csv"))
    elif option == "6":
        get_subscribed_emails()
    elif option == "0":
         pass
    else:
        raise KeyError("There is no such option.")


    pass


# print the default table of records from the file
#
# @table: list of lists
def show_table(table):
    title_list = ["id", "name", "email", "subscribed",]
    ui.print_table(table, title_list)
    pass


# Ask a new record as an input from the user than add it to @table, than return @table
#
# @table: list of lists
def add(table):
    #id+=common.generate_random(data_manager.get_table_from_file("crm/customers.csv"))
    structure_elements = ["name", "email", "subscribed",]
    structure_elements=ui.get_inputs(structure_elements,"")
    structure_elements.insert(0,common.generate_random(table))
    table.append(structure_elements)
    data_manager.write_table_to_file("crm/customers.csv", table)
    # your code

    return table


# Remove the record having the id @id_ from the @list, than return @table
#
# @table: list of lists
# @id_: string
def remove(table, id_):
    index_id = 0

    for i in range(0, len(table)):
        if (table[i][index_id] == id_[0]):
            table.remove(table[i])
            break

    data_manager.write_table_to_file("crm/customers.csv", table)
    return table


# Update the record in @table having the id @id_ by asking the new data from the user,
# than return @table
#
# @table: list of lists
# @id_: string
def update(table, id_):
    index_id = 0
    structure_elements = ["id","name", "email", "subscribed",]
    ID = common.generate_random(table)
    for i in range(0, len(table)):
        if (table[i][index_id] == id_[index_id]):
            table.remove(table[i])
            updated_entry = ui.get_inputs(structure_elements[1::], "")
            updated_entry.insert(0, ID)
            table.insert(i, updated_entry)
            break
    data_manager.write_table_to_file("crm/customers.csv", table)

    return table


# special functions:
# ------------------


# the question: What is the id of the customer with the longest name ?
# return type: string (id) - if there are more than one longest name, return the first of descending alphabetical order
def get_longest_name_id(table):
    index_subscribe=3
    index_name=1
    index_id=0
    longestsubscribename=0
    longestid=""
    for i in range(0, len(table)):
        if table[i][index_subscribe] == '1' and longestsubscribename<=len(table[i][index_name]):
            longestid=table[i][index_id]
            longestsubscribename=table[i][index_name]
            break
    print(longestid)
    return longestid
    # your code

    pass


# the question: Which customers has subscribed to the newsletter?
# return type: list of string (where string is like email+separator+name, separator=";")
def get_subscribed_emails(table):

    # your code

    pass
