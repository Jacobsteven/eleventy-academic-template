string-test.py

print("Do you want to play rock / paper / scissors?\nType 'y' for yes")
answer = input()

if first_player >=3 or second_player >= 3:
    print("Choose a number between 0 and 2")
if first_player == second_player:
    print("Tie")

print("Enter 0 for Rock, Enter 1 for Paper, Enter 2 for Scissors")

while answer.lower() == "y"
print("Player 1, enter your number: ")
player_one = int(input())

print("Player 2, enter your number: ")
player_two = int(input())

for i in range(0, 3):
if player_one == player_two:
    print("Tie!")
elif player_one == 0 and player_two == 1:
    print("Player two wins.")
elif player_one == 0 and player_two == 2:
    print("Player one wins.")
else:
    print("Still working on it") 

print("Do you want to stop playing?\nPress 'q' to quit")
quit = input()

if quit.lower() == 'q':
    break
else:
    continue
