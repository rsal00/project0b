import os

userInputStr = input()
userInputInt = int(userInputStr)

lines = ["+-+", "| |", "+-+-+"]
inner_lines = ["| |", "+-+-+"]

def block1():
    print(lines[0])
    print(lines[1])
    print(lines[0])

doub = lambda a: (a + a) - 4

def blockMain(userIn):
    curr = 0
    le = 0
    if (userIn == 1):
        block1()
    else:
        print(lines[0])
        print(lines[1])
        print(lines[2])
        if (userIn < 4):
            while (curr != (userIn - 1)):
                if (curr % 2 == 0):
                    le = le + 2
                print(" " * (le) + inner_lines[curr % 2])
                curr += 1
                if (curr == (userIn - 1) and (userIn - 1) % 2 == 0):
                    print(" " * (le + 2) + lines[1])
                    break
            print(" " * (curr * 2) + lines[0])
        elif (userIn == 4):
            while (curr != (userIn)):
                if (curr % 2 == 0):
                    le = le + 2
                print(" " * (le) + inner_lines[curr % 2])
                curr += 1
                if (curr == (userIn) and (userIn) % 2 == 0):
                    print(" " * (le + 2) + lines[1])
                    break
            print(" " * (curr + 2) + lines[0])
        elif (userIn == 5):
            while (curr != (userIn + 1)):
                if (curr % 2 == 0):
                    le = le + 2
                print(" " * (le) + inner_lines[curr % 2])
                curr += 1
                if (curr == (userIn + 1) and (userIn + 1) % 2 == 0):
                    print(" " * (le + 2) + lines[1])
                    break
            print(" " * (curr + 2) + lines[0])
        else:
            while (curr != doub(userIn)):
                if (curr % 2 == 0):
                    le = le + 2
                print(" " * (le) + inner_lines[curr % 2])
                curr += 1
                if (curr == doub(userIn) and doub(userIn) % 2 == 0):
                    print(" " * (le + 2) + lines[1])
                    break
            print(" " * (curr + 2) + lines[0])

blockMain(userInputInt)
