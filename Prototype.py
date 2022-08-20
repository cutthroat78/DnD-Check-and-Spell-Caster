import random
while True:
    spell = input("What spell would you like to cast? Type exit to end the Program.")
    if spell == "fireball":
        result = random.randint(1,20)
        if result >= 10:
            print("You roll a " + str(result) + "," + "You cast a fireball successfully!")
        else:
            print("You roll a " + str(result) + "," + "You fail at casting a fireball!")

    if spell == "iceball":
        result = random.randint(1,20)
        if result >= 10:
            print("You roll a " + str(result) + "," + "You cast a iceball successfully!")   
        else:
            print("You roll a " + str(result) + "," + "You fail at casting a iceball!")
    if spell == "exit":
        break
