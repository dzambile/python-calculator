#Calculator
#start with defining functions for calculator operations

#Defining a function to sum values
def Sum(num1,num2): #defining sum function - using 2 empty variables
    return num1 + num2 # returns the calculation

#Defining a function to subtract values
def Sub(num1,num2):
    return num1 - num2

#Defining a function to multiply values
def Mul(num1,num2):
    return num1 * num2

#Defining a function to divide values
def Div(num1,num2):
    if num2 !=0:
        return num1 / num2
    else: 
        print("Error you cant divide by zero")

#User choice options
print("Welcome to my calculator")


#While Loop
while True:
    print("Please choose an option")
    print("1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divide")
    Choice = input("Enter a option number:") # Grabbing user input

    if Choice in ("1","2","3","4"):
        try:
            #print("Please")
            num1 = float(input("Please enter your first value: "))
            num2 = float(input("Please enter your second value: "))
            
        except ValueError:
            print("Invalid choice, please enter an option number(1,2,3,4)")
            continue
        if Choice == '1':
            print(num1," + ", num2 , " = ", Sum(num1,num2))
                  
        elif Choice == '2':
            print(num1," - ", num2 , " = ", Sub(num1,num2))

        elif Choice == '3':
            print(num1," X  ", num2 , " = ", Mul(num1,num2))

        elif Choice == '4':
            print(num1," ÷ ", num2 , " = ", Div(num1,num2))

        NextCal = input("Do you want to make another calculation?(y/n)")

        if NextCal =="n":
            break

