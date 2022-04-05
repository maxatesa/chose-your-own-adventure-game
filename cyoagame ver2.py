


def direct(direct_input1):
    if direct_input1 == "east":
        print("you went east")
        dir1 = "east"

    if direct_input1 == "west":
        print("you went west")
        dir1 = "west"

    if direct_input1 == "north":
        print("you went north")
        dir1 = "north"

    if direct_input1 == "south":
        print("you went south")
        dir1 = "south"

    if direct_input1 == "weast":
        print("you went weast")
        dir1 = "weast"

    if direct_input1 != ():
        return dir1
# Initial variable storage
dickmove = ""



youfuckedup = "you fucked up and died, you lose"
direct_input1 = ""
new_direct = ""
new_direct2 = ""
hasgun = "n"
dir1 = ""
directs = ("do you want to go north, south, east, west or weast ")
directs2 = ("do you want to kill your parents or masturbate")
direct_input1 = input(directs)
dir1 = direct(direct_input1)
dir2 = ""
castle1 = ""
castle_step_1 = "you come to a large door, open it? "





if dir1 == "west":
    dir2 = input("you come across a large hole, it appears to be non natural do you want to investigate or leave? ")

if dir1 == ("south", "north"):
    print(youfuckedup)
if dir1 == ("weast"):
    dir2 = input("you find a pretty big door, go in? (y/n) ")
    if dir2 == ("y"):
        print("you see a sign, behind that sign you see a massive pile of gold, you have sucsessfully beat the chose you own adventure game, you you read the sign or take the gold and leave? ")
        dickmove = input("take the gold or reed the sign")
        if dickmove == ("take the gold"):
            print("you took the gold but the note told you not too, the gold was coverd in covid, you died 3 days later this is the bad ending ")






if dir1 == "east":
    dir2 = input("you come to a castle, go in? (yes/no) ")


if dir2 == ("yes"):
    hasgun = input("the inside of the castle is filled with guns, take one? (yes/no) ")
    if hasgun == ("yes", "y"):
        print("you picked up a gun, this gun has 6 shots ")
        castle1 = input(castle_step_1)
    if hasgun == ("no", "n"):
        print("you move on and venture deeper into the castle ")
        castle1 = input(castle_step_1)

