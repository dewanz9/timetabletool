import os.path

"""
timetable tool program
author: Connor Dewar
date: 09/05/2016
"""

def print_title():
    """
    prints the title sequence and instructions for the tool
    """
    print("#" * 10, end='')
    print("Welcome to timetable tool", end='')
    print("#" * 10)

def create_table(file_to_use):
    """
    creates a table from a given file
    """
    lines = []
    for line in file_to_use:
        lines.append(line.split(","))
        lines[-1][-1] = lines[-1][-1][:-1]
    return lines


def load_table(date):
    """
    loads the dated timetable file
    """
    if os.path.isfile(date+".table"):
        file_using = open(date+".table", "r")
        return create_table(file_using)
    else:
        return False


def print_title_border_horiz(max_name, max_roomcode, max_type):
    """
    prints a horizontal table border
    """
    print("+", end='')
    print("-" * 5, end='')
    print("+", end='')
    print("-" * max_name, end='')
    print("+", end='')
    print("-" * max_type, end='')
    print("+", end='')
    print("-" * max_roomcode, end='')
    print("+", end='')
    print("-" * 1, end='')
    print("+")

def print_data_line(line, max_name, max_roomcode, max_type):
    """
    prints a single data line
    """
    print("|", end='')
    print(line[0], end='')
    print("|", end='')
    print(line[1], end='')
    print(" " * (max_name - len(line[1])), end='')
    print("|", end='')
    print(line[4], end='')
    print(" " * (max_type - len(line[4])), end='')
    print("|", end='')
    print(line[2], end='')
    print(" " * (max_roomcode - len(line[2])), end='')
    print("|", end='')
    print(line[3], end='')
    print("|")

def print_day(day):
    """
    prints a given day
    """
    timetable = load_table(day)
    if timetable == False:
        print("file not found")
    else:
        max_name = 0
        max_roomcode = 0
        max_type = 0
        for line in timetable:
            if len(line[1]) > max_name:
                max_name = len(line[1])
            if len(line[2]) > max_roomcode:
                max_roomcode = len(line[2])
            if len(line[4]) > max_type:
                max_type = len(line[4])
        print_title_border_horiz(max_name, max_roomcode, max_type)
        for line in timetable:
            print_data_line(line, max_name, max_roomcode, max_type)
        print_title_border_horiz(max_name, max_roomcode, max_type)

def save_table(date, table):
    """
    saves a given table
    """
    if os.path.isfile(date+".table"):
        file_using = open(date+".table", "w")
    else:
        return False
    file_using.seek(0)
    file_using.truncate()
    for line in table:
        file_using.write("{},{},{},{},{}\n".format(line[0], line[1], line[2], line[3], line[4]))
    file_using.close()

def change_event(date, time, event_title, room_code, length, type):
    """
    changes a given event at a given time on a given day
    """
    table = load_table(date)
    if table == False:
        print("file not found")
    else:
        position = int(time[:2])-8
        row = table[position]
        row[1] = event_title
        row[2] = room_code
        row[3] = length
        row[4] = type
        table[position] = row
    save_table(date, table)


def handle_command(list_of_inputs):
    """
    handles the command that was inputed
    """
    if list_of_inputs[0] == "view":
        print_day(list_of_inputs[1])
    elif list_of_inputs[0] == "change":
        date = list_of_inputs[1]
        print("changing date {}".format(date))
        time = input("what time would you like to change? ")
        event_title = input("what is the name of the event? ")
        room_code = input("what location is this event? ")
        length = input("how long is this event? ")
        type = input("what type of event is this? ")
        change_event(date, time, event_title, room_code, length, type)
    else:
        print("command not recognized")

def run_terminal():
    """
    runs the terminal like machine for the tool.
    """
    playing = True
    while playing:
        print("$", end='')
        command = input()
        list_of_inputs = command.split(" ")
        if list_of_inputs[0] == "exit":
            playing = False
        handle_command(list_of_inputs)


def main():
    """
    The main function for the program
    """
    print_title()
    run_terminal()


main()
