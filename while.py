number = 23
running = True

while running:
    guess = int(input('Enter an integer: '))

    if guess == number:
        print('Congratulations, you got it!')
        running = False
    elif guess < number:
        print ('No, its higher than that')
    else: 
        print ('No, its lower than that')

else: 
    print('The while loop is over.')

print('Fin')
