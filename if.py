number = 23
guess = int(input('Enter an integer: '))

if guess == number:
    print('Congrats you got it!')
    print('(But we got no prizes)')

elif guess < number:
    print('Nope, you fail. It be higher')

else:
    print('Nope, you fail. It be lower')

print('Done')
