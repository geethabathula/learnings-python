print("================rock, paper, scissors=====================")
user1input = input("Player1's Turn")
user2input = input("Player2's Turn")
if user1input == user2input:
    print("Its a tie")
elif user1input == "rock":
    if user2input == "scissors":
        print("Player1 Wins")
    if user2input == "paper":
        print("Player2 Wins")
elif user1input == "paper":
    if user2input == "rock":
        print("Player1 Wins")
    if user2input == "scissors":
        print("Player2 Wins")
elif user1input == "scissors":
    if user2input == "rock":
        print("Player1 Wins")
    if user2input == "paper":
        print("Player2 Wins")
''' 
if (user1input == "rock" and user2input == "scissors"):
    print("Player1 Wins")
elif (user1input == "rock" and user2input == "paper"):
    print("Player2 Wins")
elif (user1input == "paper" and user2input == "rock"):
    print("Player1 Wins")
elif (user1input == "paper" and user2input == "scissors"):
    print("Player2 Wins")
elif (user1input == "scissors" and user2input == "rock"):
    print("Player1 Wins")
elif (user1input == "scissors" and user2input == "paper"):
    print("Player2 Wins")
else:
    print("Something Went Wrong")
'''