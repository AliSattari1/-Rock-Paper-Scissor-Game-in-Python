import random

choices = ["r", "p", "s"]

choice_meaning = {
    "r" : "Rock" ,
    "p" : "Paper" ,
    "s" : "Scissor"
}

user_choice = input("Select from Rock, Paper, Scissor (r, p, s): ")

# ai_choise = "r"
ai_choice = random.choice(choices)

if user_choice in choices:
    print(f"Your choice is {choice_meaning[user_choice]}, And AI choice is {choice_meaning[ai_choice]}.")

    # r > s , s > p , p > r
    if user_choice == ai_choice:
        print("Tie")
    # elif user_choice == "r" and ai_choice =="s":
    #     print("You Won!")
    # elif user_choice == "s" and ai_choice =="p":
    #     print("You Won!")
    # elif user_choice == "p" and ai_choice =="r":
    #     print("You Won!")
    
    elif (user_choice == "r" and ai_choice =="s") or (user_choice == "s" and ai_choice =="p") or (user_choice == "p" and ai_choice =="r"):
        print("You Won!")

    else:
        print("You Lost!")



else:
    print("Not Valid input.\nTry again.")    
