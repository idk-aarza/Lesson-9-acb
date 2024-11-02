print("select your ride:")
print('1. Bike')
print("2. car")
#take input of no. 1 or 2
#select your ride
choice=int(input('Enter your choice:'))

#use entering option 1
if(choice==1): #condition 1 outer if statement
    print('What type of bike?')
    print('1.Scooty\n')
    
#Condition for selecting the type of bike
choice2= int(input("Enter your choice2 :"))
if choice2==1:#inner if statement
    print("you have selected scooty")
else: 
    print('You have selected scooter')

#user entering option 2
if(choice ==2): # outer elif statement
    print("what type of car")
    print("1.sedan")
    print("2.XUV")
    
choice3=int(input('enter your choice3:'))
if choice3==1:#inner if statement
#condition for selecting the type of car
    print('you have selected sedan')
    print('You have selected XUV')
else:
    print("Wrong choice")

    