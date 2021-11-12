import sys
import pytest
import re

# gloabl variable
car_info = {"x": -1, "y": -1, "dir": None}
# the fourth direction
valid_directions = ["N", "E", "S", "W"]
the_map = {"max_x": 0, "max_y": 0}

#///////////////////////////////////////// TEST
def test_outof_map_right_test():
    # 0, 0, E
    initial_map("5 5")
    assert put_car_into_map([5, 5, "E"]) == None
    assert command_M() == False



def test_outof_map_left_test():
    # 0, 0, W
    assert put_car_into_map([0, 0, "W"]) == None
    assert command_M() == False


def test_outof_map_top_test():
    # 5 5 N
    initial_map("5 5")
    assert put_car_into_map([5, 5, "N"]) == None
    assert command_M() == False



def test_outof_map_bottom():
    # 0 0 S
    assert put_car_into_map([0, 0, "S"]) == None
    assert command_M() == False

def test_not_valid_car_initial_info():
    initial_map("0 0")
    assert put_car_into_map([0, 1, "N"]) == False
    assert put_car_into_map([1, 0, "N"]) == False
    assert put_car_into_map([-1, 0, "N"]) == False
    assert put_car_into_map([0, -1, "N"]) == False

#///////////////////////////////////////// HELP FUNTIONS

# get the max row and the max col----------------
# y-> row, x->col
def initial_map(row_col):
    args = row_col.split(' ')
    if (len(args) != 2):
        raise
    the_map["max_x"] = int(args[0])
    the_map["max_y"] = int(args[1])

def put_car_into_map(args):
    # update the position
    try:
        if len(args) != 3:
            print("Enter valid car info, please")
            raise

        x = args[0]
        y = args[1]
        direction = args[2]
        if int(x) > the_map["max_x"] or int(y) > the_map["max_x"] or int(x) < 0 or int(y) < 0:
            raise
        car_info["x"] = int(x)
        car_info["y"] = int(y)
        # update the directionx
        if direction != "S" and direction != "N" and direction != "E" and direction != "W":
            raise
        car_info["dir"] = direction
    except:
        return False

# 90 degrees left 
# without movement
def command_L():
    car_info["dir"] = valid_directions[valid_directions.index(car_info["dir"]) - 1]


# 90 degrees right
# without movement
def command_R():
    index = valid_directions.index(car_info["dir"]) + 1
    if index > 3:
        index = 0
    car_info["dir"] = valid_directions[index]

# move a grid in the current direction 
def command_M():
    # N
    # y + 1
    try:
        if car_info["dir"] == "N":
            if car_info["y"] + 1 > int(the_map["max_y"]):
                raise
            car_info["y"] = car_info["y"] + 1
        # W
        elif car_info["dir"] == "E":
            if car_info["x"] + 1 > int(the_map["max_x"]):
                raise
            car_info["x"] = car_info["x"] + 1
        # S
        elif car_info["dir"] == "S":
            if car_info["y"] - 1 < 0:
                raise
            car_info["y"] = car_info["y"] - 1
        #E
        elif car_info["dir"] == "W":
            if car_info["x"] - 1 < 0:
                raise
            car_info["x"] = car_info["x"] - 1
    except:
        return False

def executeTheCommands(commands):
    # invalid input, exit the program
    if commands == None or len(commands) == 0:
        print("Enter valid command, please")
        return

    commands = list(commands)
    for i in range(0, len(commands)):
        command = commands[i]
        if command == "L":
            command_L()
        elif command == "R":
            command_R()
        elif command == "M":
            # invalid command
            if command_M() == False:
                raise
        else:
            # invalid command
           raise

    


#-------------------------------MAIN------------------------------
def main():
    # invalid input
    try:
        row_col = input().strip()
        initial_map(row_col)

        while (True):
            car_info_input = input().strip()

            #initial the info of the car
            # if the input is invalid, exit the program
            if put_car_into_map(car_info_input.split(' ')) == False:
                break

            # control
            executeTheCommands(input().strip())

            # print the final info of the car
            print(f'{car_info["x"]} {car_info["y"]} {car_info["dir"]}')
    except:
        print("Enter valid input, please")
        return
if __name__ == "__main__":
    main()

