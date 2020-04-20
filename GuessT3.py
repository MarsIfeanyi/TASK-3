#Program to guess number between 1 and 9.......
#The user will be prompted to enter a guess and if guess is wrong the prompt appears again till the user guesses right and the program will exit
import random
target_num, pick_num = random.randint(1, 10), 0
while target_num != pick_num:
	pick_num = int(input("Chief guess a number between 1 and 10 until you get it right : "))
print('Correct Guess!')