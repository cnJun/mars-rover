import sys
import pytest

# gloabl variable
car_info = {"x": -1, "y": -1, "dir": None}
# the fourth direction
valid_directions = ["N", "W", "S", "E"]
the_map = {"max_x": 0, "max_y": 0}

#/////////////////////////////////////////
def test_outof_map_right_test():
    # 0, 0, E
    initial_map("5 5")
    assert put_car_into_map(5, 5, "E") == None
    assert command_M() == False



def test_outof_map_left_test():
    # 0, 0, W
    assert put_car_into_map(0, 0, "W") == None
    assert command_M() == False


def test_outof_map_top_test():
    # 5 5 N
    initial_map("5 5")
    assert put_car_into_map(5, 5, "N") == None
    assert command_M() == False



def test_outof_map_bottom():
    # 0 0 S
    assert put_car_into_map(0, 0, "S") == None
    assert command_M() == False

def test_not_valid_car_initial_info():
    initial_map("0 0")
    assert put_car_into_map(0, 1, "N") == False
    assert put_car_into_map(1, 0, "N") == False
    assert put_car_into_map(-1, 0, "N") == False
    assert put_car_into_map(0, -1, "N") == False

#/////////////////////////////////////////

# get the max row and the max col----------------
# y-> row, x->col
def initial_map(row_col):
    args = row_col.split(' ')
    if (len(args) != 2):
        raise
    the_map["max_x"] = int(args[0])
    the_map["max_y"] = int(args[1])

# help funtions ------------------------------
def put_car_into_map(x, y, direction):
    # update the position
    try:
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
    


#-------------------------------MAIN------------------------------
def main():
    '''
    1 2 N
    LMLMLMLMM
    3 3 E
    MMRMMRMRRM'''
    row_col = input().strip()
    initial_map(row_col)
    car_info_input = input()
    car_info_input.strip()
    while (car_info_input):
        args = car_info_input.split(' ')
        if len(args) != 3:
            raise
        
        #initial the info of the car
        put_car_into_map(args[0], args[1], args[2])

        # control
        control_command = input()
        control_command = control_command.strip()
        if control_command == None or len(control_command) == 0:
            raise
        commands = list(control_command)
        for i in range(0, len(commands)):
            print(car_info)
            command = commands[i]
            if command == "L":
                command_L()
            elif command == "R":
                command_R()
            elif command == "M":
                command_M()
            else:
                # invalid command
                raise
        # print the final info of the car
        print(f'{car_info["x"]} {car_info["y"]} {car_info["dir"]}')
        car_info_input = input()
        car_info_input = car_info_input.strip()

if __name__ == "__main__":
    main()

