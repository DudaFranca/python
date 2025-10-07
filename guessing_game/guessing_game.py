import random

number_secret = random.randint(1, 100)
count = 0

while True:
    try:
        number_user = int(input('Please enter a number between 1 and 100: '))

        if number_user <= 100 and number_user >= 1:
            if number_user > number_secret:
                print('Too high')
                count += 1
            elif number_user < number_secret:
                print('Too low')
                count += 1
            else:
                count += 1
                print(f'You guessed right! You made {count} attempts left')
                question = input('Do you want to play again? (y/n): ')
                if question == 'y':
                    number_secret = random.randint(1, 100)
                    count = 0
                else:
                    break
    except ValueError:
        print('Please enter a number.')