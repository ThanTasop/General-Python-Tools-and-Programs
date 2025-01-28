from random import randrange
def starting_prints():
    global player
    if i % 2 == 0:
        print(f"         ROUND {int(i/2 + 1)}        ")
        print("-----------------------------")
    if player == "Player 2":
        player = "Player 1"
    else:
        player = "Player 2"
    print(f"{player} plays\n")
def play():
    rollingdices = 5
    hand = []
    print("If u want to keep a dice, press the number of the dice you want, (from left to right).\n"
          "If u dont want another dice, just press something different from the specified numbers\n")
    for i in range(3):
        print("Throw the dices!\n")
        zaria = []
        for i in range(rollingdices):
            zaria.append(randrange(1, 7))
        zaria.sort()
        print(f"Dices: {zaria}")
        choices = []
        numer = 0
        while numer < 5 - len(hand):
            choice = input("Give number of dice or press enter to roll again: ")
            if choice in [str(j) for j in range(1, 6)] and choice not in choices:
                hand.append(zaria[int(choice) - 1])
                choices.append(choice)
                numer += 1
                print(f"Current hand: {hand}")
            elif choice in choices:
                print("You have already chose this dice")
                continue
            else:
                break
        rollingdices = 5 - len(hand)
    return hand
def sum_points():
    choice = input("Press the number you want to stack your points on: ")
    while True:
        if score[i % 2][choice] == 0:
            for num in hand:
                if num == int(choice):
                    score[i % 2][choice] += num
            if score[i % 2][choice] == 0:
                score[i % 2].pop(choice)
            break
        else:
            choice = input("This choice is not available, see the available list and choose one of em")
def winner_is():
    if sum(score[0].values())>sum(score[1].values()):
        print("And the winner is player 1!")
    elif sum(score[0].values())<sum(score[1].values()):
        print("And the winner is player 2!")
    else:
        print("It's a draw!")

score = [{str(i):0 for i in range(1,7)},{str(i):0 for i in range(1,7)}]
player = "Player 2"

for i in range(12):
    starting_prints()
    hand = play()
    print(hand)
    print("The available options are the following: ", end="")
    for key in score[i % 2].keys():
        if score[i % 2][key] == 0:
            print(f"{key}'s", end=" ")
    print("")
    sum_points()
    print("")
    print(f"Current Score: {sum(score[0].values())} - {sum(score[1].values())} (Player 1 - Player 2)\n")
winner_is()




