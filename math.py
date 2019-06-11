import decimal
import cmath

userInput = input('Type A to use the four function calculator, B to use the tip calculator, or C to use the quadradic formula.')
userChoice = userInput.lower()
if userChoice == 'a':
    #This statement will test out if x is an integer value. It will run the loop until the user puts in a correct integer value
    while True:
        try:
            x = int(input("Pick a value for x: "))
        except ValueError:
            print("Sorry, I didn't understand that. You need to enter an integer. Don't type the word out!")
            #better try again... Return to the start of the loop
            continue
        else:
            #number was sucessfully passed!
            #we're ready to exit the loop.
            break
    while True:
        try:
            y = int(input("Pick a value for y: "))
        except ValueError:
            print("Sorry, I didn't understand that. You need to enter an integer. Don't type the word out!")
            #better try again... Return to the start of the loop
            continue
        else:
            #number was sucessfully passed!
            #we're ready to exit the loop.
            break
    math_operator = input("Would you like to add, multiply, divide, or subtract these numbers?")
    
    #We convert the math operator to lowercase to avoid issues with some letters being capitalized by the user
    choice = math_operator.lower()

    if choice == 'multiply':
        multiply_answer = int(x)*int(y)
        print('The value of x multiplied by y is ' + str(multiply_answer))
    elif choice == 'divide':
        divde_answer = int(x)/int(y)
        print('The value of x divided by y is ' + str(divde_answer))
    elif choice == 'add':
        add_answer = int(x) + int(y)
        print('The value of x plus y is ' + str(add_answer))
    elif choice == 'subtract':
        subtract_answer = int(x) - int(y)
        print('The value of x minus y is ' + str(subtract_answer))
    else:
        print('You did not select add, multiply, subtract, or divide. You must type these words without spelling errors.')

if userChoice == 'b':
    total_bill = decimal.Decimal(input('Total Bill: '))
    tip = total_bill * decimal.Decimal(0.18)
    final_bill = total_bill + tip
    print('You should tip ' + str(round(tip,2)) + ' for your bill of ' + str(total_bill) + " for a total bill of " + str(round(final_bill,2)))

if userChoice == 'c':
    while True:
        try:
            a = int(input("Pick a value for A: "))
        except ValueError:
            print("Sorry, I didn't understand that. You need to enter an integer. Don't type the word out!")
            #better try again... Return to the start of the loop
            continue
        else:
            #number was sucessfully passed!
            #we're ready to exit the loop.
            break
    while True:
        try:
            b = int(input("Pick a value for B: "))
        except ValueError:
            print("Sorry, I didn't understand that. You need to enter an integer. Don't type the word out!")
            #better try again... Return to the start of the loop
            continue
        else:
            #number was sucessfully passed!
            #we're ready to exit the loop.
            break
    while True:
        try:
            c = int(input("Pick a value for C: "))
        except ValueError:
            print("Sorry, I didn't understand that. You need to enter an integer. Don't type the word out!")
            #better try again... Return to the start of the loop
            continue
        else:
            #number was sucessfully passed!
            #we're ready to exit the loop.
            break
    #calculate the disciminate
    d = (b**2) - (4*a*c)
    
    solution_1 = (-b-cmath.sqrt(d))/(2*a)
    solution_2 = (-b+cmath.sqrt(d))/(2*a)
    print('The two roots are '+str(solution_1)+" and "+str(solution_2))