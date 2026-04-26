import random
lucky_number = random.randint(1,100)
print("try to guess a number from 1 to 100")
guess = 0
command = input("choose mode easy/hard :")
if command.lower() == "easy" :
    guess_count = 10
    print('you have 10 guesses')
elif command.lower() == "hard":
    guess_count = 5
    print("you have 5 guesses")
else:
    print("invalid mode, return to easy mode")
    guess_count = 10
while guess != guess_count:
    user_guesses = int(input("type number: "))
    if user_guesses > lucky_number:
        print(f"too high,{guess_count - guess} left ")
    elif user_guesses < lucky_number:
        print(f" too low, {guess_count - guess} left")
    else:
        print("congratulation, you are tuff")
        break
    guess += 1
    if guess == guess_count:
        print("you lost, better luck next time. ")
        break
