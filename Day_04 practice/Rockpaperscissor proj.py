import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

user_inp=int(input("What do you choose? Type 0 for rock, 1 for paper, 2 for scissors: "))
if(user_inp==0):
    print(rock)
elif(user_inp==1):
    print(paper)
elif(user_inp==2):
    print(scissors)
else:
    print("Invalid input")

print("Computer chose:")
comp_choice=random.randint(0,2)
if(comp_choice==0):
    print(rock)
elif(comp_choice==1):
    print(paper)
else:
    print(scissors)

# logic for rock paper scissor
if user_inp==0 and comp_choice==2:
    print("You win!")
elif user_inp==0 and comp_choice==1:
    print("You lose!")
elif user_inp==1 and comp_choice==0:
    print("You win!")
elif user_inp==1 and comp_choice==2:
    print("You lose!")
elif user_inp==2 and comp_choice==0:
    print("You lose!")
elif user_inp==2 and comp_choice==1:
    print("You win!")
elif user_inp==comp_choice:
    print("Its a draw!")
