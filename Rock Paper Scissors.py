import random
user_choice = int(input("Enter a number between(0-2).Enter 0 for Rock 1 for Paper 2 for Scissor: "))
comp_choice = random.randint(0,2)

print("You Choice: ",user_choice)
print("Computer Choice: ",comp_choice)

if user_choice < 0 or user_choice >= 3 :
    print("You canno't enter these numbers")
elif user_choice == comp_choice :
    print("Wow the game is Raw!")
elif user_choice > comp_choice :
    print("Wow You Win!")
elif user_choice < comp_choice :
    print("Oh You Lost!")
elif user_choice==0 and comp_choice ==2 :
    print("Oh You Lost!")
elif user_choice==2 and comp_choice ==  0:
    print("Wow You nailed it!")

