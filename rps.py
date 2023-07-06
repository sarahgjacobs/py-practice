import random

user_score = 0
computer_score = 0


options = ['scissors', 'rock', 'paper']

while True:
    user_input = input("Choose Rock, Paper, or Scissors or Q to quit:  ").lower()
    if user_input == 'q':
        break

    if user_input not in options:
        continue

    random_num = random.randint(0, 2)
    # scissors: 1, rock:2, paper:3

    computer_pick = options[random_num]

    print("Computer chose " + computer_pick)

    if user_input == "rock" and computer_pick == "scissors":
        print("You win!")
        user_score += 1
        continue
    if user_input == "paper" and computer_pick == "rock":
        print("You win!")
        user_score += 1
        continue
    if user_input == "scissors" and computer_pick == "paper":
        print("You win!")
        user_score += 1
        continue
    else:
        print("You lose ):")
        computer_score += 1


print("Your score is " + user_score)
print("The computer's score is " + computer_score)