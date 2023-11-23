import random
def get_choices():
    player_choice = input("Enter a choice(rock,paper,scissor):")
    options=["rock","paper","scissor"]
    computer_choice = random.choice(options)
    choices={"player":player_choice,"computer":computer_choice}
    return choices
def chkwin(player,computer):
    if player==computer:
        print("You choose "+player+" and computer choose "+computer)
        print ("It's a tie")
    elif player=="paper":
        if computer=="rock":
            print("You choose "+player+" and computer choose "+computer)
            return "Paper beats rock, You win!"
        else:
            print("You choose "+player+" and computer choose "+computer)
            return "Scissor beats paper, You lose!"
    elif player=="rock":
        if computer=="scissor":
            print("You choose "+player+" and computer choose "+computer)
            return "Rock beats scissor, You win!"
        else:
            print("You choose "+player+" and computer choose "+computer)
            return "Paper beats rock, You lose!"
    elif player=="scissor":
        if computer=="paper":
            print("You choose "+player+" and computer choose "+computer)
            return "Scissor beats paper, You win!"
        else:
            print("You choose "+player+" and computer choose "+computer)
            return "Rock beats scissor, You lose!"    
choices=get_choices()
results=chkwin(choices["player"],choices["computer"])
print(results)