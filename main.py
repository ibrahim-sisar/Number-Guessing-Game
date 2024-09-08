from random import randint
quit_the_game=False
while quit_the_game != True:
    is_wen=False
    the_guessing_number=randint(1,100)
    dic={'Easy':10,'Medium':5,'Hard':3}
    lis=['Easy','Medium','Hard']
    print('''
Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.
    ''')
    print('Please select the difficulty level:')
    print('1. Easy (10 chances)')
    print('2. Medium (5 chances)')
    print('3. Hard (3 chances)\n')

    try:
        choice=int(input('Enter your choice:'))
    except:
        print('Please choose a number')
    print(f"""
Great! You have selected the {lis[choice-1]} difficulty level.
Let's start the game!
    """)
    for i in range(dic[lis[choice-1]]):
        guess=int(input('Enter your guess:'))
        msg=f'Incorrect! The number is '
        if guess == the_guessing_number:
            print(f'Congratulations! You guessed the correct number in {i+1} attempts.')
            is_wen=True
            break
        elif guess < the_guessing_number:
            msg+=f'greater  than {guess}.'
        elif guess > the_guessing_number:
            msg+=f'lass than {guess}.'
            
        else:
            msg='Incorrect! input'
        print(msg)
        i+=1
    if is_wen == False:
        print('Sorry, the transformers are finished.')
    play_again=input('play again (y,n):')
    if play_again == 'n' or play_again =='N':
        quit_the_game=True