# implement commonly used functions here

import random


def get_tool_manager_structure_elements():
    structure_elements = ["id", "name",
                          "manufacturer", "purchase date", "durability"]
    return structure_elements


def get_selling_structure_elements():
    structure_elements = ["id", "title", "price", "month", "day", "year"]
    return structure_elements


def get_accounting_structure_elements():
    structure_elements = ["id", "month", "day", "year", "type", "amount"]
    return structure_elements


# generate and return a unique and random string
# other expectation:
# - at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter
# - it must be unique in the list
#
# @table: list of list
# @generated: string - generated random string (unique in the @table)
def generate_random(table):
    """Generates a random ID, until it creates such value,
    which is not present in the list of list given in parameters

    Arguments:
    table - list of lists
    """
    generated = ''
    ID = 0

    # character sets
    spec_char = "!@#$%^&*()?"
    uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lowercase = "abcdefghijklmnopqrstuvwxyz"
    digits = "0123456789"

    present_ids_in_table = []

    # we get all the id-s from the table for checking purposes
    for entries in table:
        present_ids_in_table.append(entries[ID])

    # we generate random id-s until we get a unique one which is nor present
    # in the table, or if we did not generated one already
    while len(generated) < 8 or generated in present_ids_in_table:
        generated = ""
        generated += lowercase[random.randint(0, len(lowercase) - 1)]
        generated += uppercase[random.randint(0, len(uppercase) - 1)]
        generated += digits[random.randint(0, len(digits) - 1)]
        generated += lowercase[random.randint(0, len(lowercase) - 1)]
        generated += digits[random.randint(0, len(digits) - 1)]
        generated += spec_char[random.randint(0, len(spec_char) - 1)]
        generated += spec_char[random.randint(0, len(spec_char) - 1)]
        generated += uppercase[random.randint(0, len(uppercase) - 1)]

    return generated
