import random
Number = int(random.randint(1,30))
guess_count = 0
while guess_count <= 4:
    Guess = int(input("Your Guess : "))
    if Guess > Number:
        print("Lower")
        guess_count += 1
    elif Guess < Number:
        print("Higher")
        guess_count += 1
    elif Guess == Number:
        print("Bingo!")
        break;
    elif guess_count == 3:
        print(f'You LOST Number was {Number}')
        break;