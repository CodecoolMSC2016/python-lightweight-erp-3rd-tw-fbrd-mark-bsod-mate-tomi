

# This function needs to print outputs like this:
# /-----------------------------------\
# |   id   |      title     |  type   |
# |--------|----------------|---------|
# |   0    | Counter strike |    fps  |
# |--------|----------------|---------|
# |   1    |       fo       |    fps  |
# \-----------------------------------/
#
# @table: list of lists - the table to print out
# @title_list: list of strings - the head of the table
def print_table(table, title_list):
    line_width = 0
    title_width = 0
    dict_column_width = {}

    for title in title_list:
        dict_column_width[title] = len(title)
        title_width += len(title)

    for row_index in range(len(table)):
        for column_index in range(len(table[row_index])):
            if(len(table[row_index][column_index]) > dict_column_width[title_list[column_index]]):
                dict_column_width[title_list[column_index]] = len(
                    table[row_index][column_index])

    for k, v in dict_column_width.items():
        line_width += v + 2

    # Black Magic happens here
    line_width += 4
    line_width -= 5 - (len(title_list))

    print("/" + "-" * line_width + "\ ")  # topline

    for elements, title in zip(title_list, title_list):
        print("|", end="")
        print(elements.center(dict_column_width[title] + 2, " "), end="")

    print("|", end="")
    print()
    print("|" + "-" * line_width + "| ")  # aftertitleline

    for i in range(0, len(table)):
        for elements, title in zip(table[i], title_list):
            print("|", end="")
            print(elements.center(dict_column_width[title] + 2, " "), end="")

        print("|", end="")
        print()
        if i == len(table) - 1:
            pass
        else:
            print("|" + "-" * line_width + "| ")

    print('\\' + "-" * line_width + "/")  # bottomline
    pass


# This function needs to print result of the special functions
#
# @result: string or list or dictionary - result of the special function
# @label: string - label of the result
def print_result(result, label):

    if type(result) is list:
        print(label)
        for elem in result:
            print(elem)

    elif type(result) is dict:
        print(label)
        for k, v in result.items():
            print(k + ": " + str(v))

    else:
        print(label + ": " + str(result))

    pass


# This function needs to generate outputs like this:
# Main menu:
# (1) Store manager
# (2) Human resources manager
# (3) Inventory manager
# (4) Accounting manager
# (5) Selling manager
# (6) Customer relationship management (CRM)
# (0) Exit program
#
# @title: string - title of the menu
# @list_options: list of strings - the options in the menu
# @exit_message: string - the last option with (0) (example: "Back to main menu")
def print_menu(title, list_options, exit_message):

    print("\n" + title + ":")

    for i in range(0, len(list_options)):
        menu_index = i + 1
        print("(" + str(menu_index) + ") " + list_options[i])

    print("(0) " + exit_message)

    pass


# This function gets a list of inputs from the user by the terminal
#
# @list_labels: list of strings - the labels of the inputs
# @title: string - title of the "input section"
# @inputs: list of string - list of the received values from the user
def get_inputs(list_labels, title):
    inputs = []

    print(title)

    for labels in list_labels:
        if (labels[-1] == " " and labels[-2] == ":"):
            inputs.append(input(labels))
        else:
            inputs.append(input(labels + ": "))

    return inputs


# This function needs to print an error message. (example: Error: @message)
#
# @message: string - the error message
def print_error_message(message):

    print("ERROR: " + message)

    pass
