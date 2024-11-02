enrol=input('Do you want to enrol in school Y or N')
age=int(input('Enter your age'))
if enrol == 'Y':
    print('You can enrol in the school')
else:
    if age <= 10:
        print("You cant enrol")
    elif age <=20:
        print('You can enrol')
    else:
        print('you cant enrol')