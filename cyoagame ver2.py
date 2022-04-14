import random


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

    if direct_input1 not in valid_dir:
        print("please input a valid word next time (north east south west weast)")
        exit()

    # if direct_input1 != "":
    #    return dir1

    return dir1


# Initial variable storage
directs = "do you want to go north, south, east, west or weast "
direct_input1 = input(directs)
you_fucked_up = "you fucked up and died, you lose"
new_direct = ""
new_direct2 = ""
hasgun = ""
valid_dir = ["weast", "south", "north", "west", "east"]
dir3 = ""
dir4 = ""
global dir1
dir1 = direct(direct_input1)
dir2 = "im pretty sure jared is gay"
castle1 = ""
castle_step_1 = "you come to a large door, open it? "
dick_move = ""
game_state = ""
gun1 = ""
gun2 = ""
fight1 = ""
inventory = []
storage = []
valid_dir2 = [""]
Valid_words = ["yes", "y", "no", "n", "im pretty sure jared is gay"]
list1 = [0, 8, 109, 220, 222, 241, 149, 107, 75, 248, 254, 140, 16, 66,
         74, 21, 211, 47, 80, 242, 154, 27, 205, 128, 161, 89, 77, 36,
         95, 110, 85, 48, 212, 140, 211, 249, 22, 79, 200, 50, 28, 188,
         52, 140, 202, 120, 68, 145, 62, 70, 184, 190, 91, 197, 152, 224,
         149, 104, 25, 178, 252, 182, 202, 182, 141, 197, 4, 81, 181, 242,
         145, 42, 39, 227, 156, 198, 225, 193, 219, 93, 122, 175, 249, 0,
         175, 143, 70, 239, 46, 246, 163, 53, 163, 109, 168, 135, 2, 235,
         25, 92, 20, 145, 138, 77, 69, 166, 78, 176, 173, 212, 166, 113,
         94, 161, 41, 50, 239, 49, 111, 164, 70, 60, 2, 37, 171, 75,
         136, 156, 11, 56, 42, 146, 138, 229, 73, 146, 77, 61, 98, 196,
         135, 106, 63, 197, 195, 86, 96, 203, 113, 101, 170, 247, 181, 113,
         80, 250, 108, 7, 255, 237, 129, 226, 79, 107, 112, 166, 103, 241,
         24, 223, 239, 120, 198, 58, 60, 82, 128, 3, 184, 66, 143, 224,
         145, 224, 81, 206, 163, 45, 63, 90, 168, 114, 59, 33, 159, 95,
         28, 139, 123, 98, 125, 196, 15, 70, 194, 253, 54, 14, 109, 226,
         71, 17, 161, 93, 186, 87, 244, 138, 20, 52, 123, 251, 26, 36,
         17, 46, 52, 231, 232, 76, 31, 221, 84, 37, 216, 165, 212, 106,
         197, 242, 98, 43, 39, 175, 254, 145, 190, 84, 118, 222, 187, 136,
         120, 163, 236, 249]

# west path, hole, DEAD END PATH
if dir1 == "west":
    dir4 = input("you come across a large hole, it appears to be non natural do you want to (investigate) or (leave?) ")
    if dir4 == "investigate":
        print("you fell into the hole and took", list1[random.randint(0, 254)], "damage, you died, the end")
    if dir4 == "leave":
        print("you left, but you tripped and died, rip")

# used to show illusion of choice, will just kill player instantly
if dir1 in ("south", "north"):
    print(you_fucked_up)
    exit()

# weast path, ending one,
if dir1 == "weast":

    while dir2 != valid_dir2:
        dir2 = input("you find a pretty big door, go in? (y/n) ")
        if dir2 in ("y", "yes"):
            print("you see a sign, behind that sign you see a massive pile of gold, you have successfully beat the "
                  "chose you own adventure game,  you you read the sign or take the gold and leave? ")

            dick_move = input("(take the gold) or (read the sign) ")
            if dick_move in "take the gold":
                print("you took the gold but the note told you not too, the gold was covered in covid, you died 3 days "
                      "later this is the bad ending ")
                exit()
            if dick_move in "read the sign":
                print("the sign says to not take the gold, you follow the directions of the sign and leave, "
                      "this is the good ending")
                exit()
            if dick_move not in ('read the sign', "take the gold"):
                print("you did neither, you died for not being able to read, game over man, game over")
                exit()
        if dir2 in ("n", "no"):
            print("you leave and die many years later, wondering, what was in that door")
            exit()
        if dir2 not in Valid_words:
            print("you chose not to put a valid word and died, you lose")

# east path, castle and skeleton
if dir1 == "east":
    dir3 = input("you come to a castle, go in? (yes,y/no,n) ")
if dir3 in ("no", "n"):
    print("placeholder")
if dir3 in ("yes", "y"):
    hasgun = input("the inside of the castle is filled with guns, take one? (yes/no) ")
if hasgun in ("yes", "y"):
    print("you picked up a gun, this gun has 6 shots ")
    gun1 = "yes"
    gun2 = "gun"

if gun1 == "yes":
    inventory.append("gun")

if hasgun in ("no", "n"):
    print("you move on and venture deeper into the castle ")
    castle1 = input("castle_step_1")
if dir3 not in Valid_words:
    print("you waited too long and died of old age ")
# 'increments the code in the east path,
if gun1 == "yes":
    castle_step_2 = input("you enter a large chamber, you spot a large skeleton, do you (fight him), or (talk to him) ")
    if castle_step_2 in ("fight", "fight him"):
        print("you chose to fight the skeleton, this absolute lad beats you into a fine paste, you die")
    if castle_step_2 in ("talk", "talk to him"):
        print("you speak to this large beast")
        sleep = 3
        print("he tells you that he will kill you")
        fight1 = input("what do you do ")
        if fight1 == ("use gun", "shoot him"):
            if gun2 == "gun":
                print("you shoot the skeleton with the gun,")

            if gun2 != "gun":
                print("you reach for your non existent gun, the skeleton bites you and you die, you lose")
                exit()


