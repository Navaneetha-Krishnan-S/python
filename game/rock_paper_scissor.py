import random

print("Welcome to Rock Paper Scissor Game: ")
print("------------------------------------")

rock = ("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

# Paper
paper = ("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

# Scissors
scissor = ("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")
game = [rock,paper,scissor]

while(True):
    
    print("----------------------------------------")
    print( """
            0: Rock
            1: Paper
            2: Scissor
            press 'e' to  Exit
          """)
    
    user_input = input("Enter your Choice: ")
    if user_input == "e":
        print("Thank You for playing the Game!")
        break
    user_choice = int(user_input)
    computer_choice = random.randint(0,2)   
    print("COMPUTER CHOICE: ")
    print(game[computer_choice],"\n")
    print("USER CHOICE")
    print(game[user_choice])
   

    if user_choice >2 or user_choice<0:
        print("Invalid Choice")
    
                
    else:
    
            if user_choice == computer_choice:
                print("TIE")
            elif user_choice == 0 and computer_choice == 1:
                print("YOU LOSE")
            elif user_choice == 1 and computer_choice == 2:
                print("YOU LOSE")
            elif user_choice == 2 and computer_choice == 0 :
                print("YOUT LOSE")
           
            else:
                print("YOU WON")
