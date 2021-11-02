import random


def unique(start: int, stop: int) -> int:
    return random.randint(start, stop)


def create_four_digits() -> list:
    digits = list()

    while len(digits) != 4:
        if not digits:
            digits.append(unique(1, 9))
        elif (num := unique(0, 9)) not in digits:
            digits.append(num)

    return digits


random_number = (create_four_digits())
separator = '-' * 55
print(
    f"Hi there!\n{separator}\n"
    f"I've generated a random 4 digit number for you.\n"
    f"Let's play a bulls and cows game.\n{separator}"
    )


def control_number():
    number = input('Enter your number: ')
    duplicates = []
    for num in number:
        if not number.isnumeric():
            print(f"Sorry, number is not numeric.")
            return quit()
        elif len(number) > 4:
            print(f"Sorry, number is too long.")
            return quit()
        elif len(number) < 4:
            print(f"Sorry, number is too short.")
            return quit()
        elif number[0] == '0':
            print(f"Sorry, number must start with a non zero.")
            return quit()
        elif num  in duplicates:
            print(f"Sorry, the number contains a duplicate.")
            return quit()
        else:
            duplicates.append(num)

    return number


def game(number):
    bulls = 0
    guess = 0
    while bulls != 4:
        bulls = 0
        cows = 0

        for i,n in enumerate(number):
            if int(n) == random_number[i]:
                bulls += 1
                cows += 1

            elif int(n) in random_number:
                cows +=1

        guess += 1

        if bulls == 4:
            print(sing_plu(cows, bulls, guess))
            return f"Correct, you've guessed the right number in {guess} guesses!"
            break
        else:
            print(sing_plu(cows, bulls, guess))
            number = control_number()


def sing_plu(cows, bulls, guess):
    if cows == 1:
        final_cows = 'Cow'
    else:
        final_cows = 'Cows'

    if bulls == 1:
        final_bulls = 'Bull'
    else:
        final_bulls = 'Bulls'
    return f"{cows} {final_cows}, {bulls} {final_bulls}, Guess {guess}\n{separator}"


number = control_number()
print(game(number))