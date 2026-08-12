import random as r


# Main function for number game

def number_guess():
    print('I am thinking of a number between 1 aaaand 15..')
    random_number = r.randint(1,16)
    counts = 0
    for counts in range(9):
        while True:
            try:
                user_guess = int(input('Guess\n>'))
                break
            except ValueError:
                print('Please only enter a number between 1 and 15')
        if user_guess == random_number:
            print('You got it right!')
            break
        elif user_guess > random_number:
            print('Too high!')
            continue
        elif user_guess <= random_number:
            print('Too low!') 
    if counts == 9:
        print('Too many attempts xd')

# Main function for menu 

def menu():
    print('Hello stranger, please enter a name!')
    user_name = input('>')
    print(f"Please enter '1' to start the game {user_name.strip()} ")
    menu = {
        1: 'Start the game', 
        2: 'Exit'
        }
    while True:
        for k, v in menu.items():
            print(f'{k}: {v}') 
        while True:
            try:
                user_choice = int(input('>'))
                break
            except ValueError:
                print('Please only enter one of the options!')
        if user_choice == 1:
            number_guess()
        elif user_choice == 2:
            exit()
        else:
            print('Please only enter one of the options')
menu()