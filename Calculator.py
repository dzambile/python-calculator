#start with defining functions for calculator operations

#addition
def add( x, y) :
    return x + y

#subtraction
def subtract ( x, y) :
    return x - y

#multiplication
def multi(x,y):
    return x * y

#division
def divide (x, y) :
    return x / y
  
print("Welcome to my calculator")
#while loop to calculate
while True:
    #Show the user options
    print("Select an operation")
    print("1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divide")
    print("5.Exit")
    #grabbing user input
    Choice = input("Enter your choice ( 1,2,3,4,5)")

    if Choice in ("1", "2", "3", "4", "5"):
        #option 5 will end program
        if Choice == "5":
            print("Exiting the calculator. Goodbye!")
            break

        #loop to get first value and validate it
        while True:
         try:
            x = float(input("Please enter your first value: "))
            break
         except ValueError:
            print("Invalid choice, please enter a valid number")

        #loop to get second value and validate it
        error=False
        while True:
            try:
                y = float(input("Please enter your second value: "))
                if Choice == "4" and y ==0:
                    print("Error: Division by zero is not allowed.")
                    error=True
                else:
                       #if & elif to print calculations
                    if  Choice == "1":
                        print( x, " + ", y ," = ", add(x, y))

                    elif Choice == "2":
                        print( x, " - ", y ," = ", subtract(x, y))

                    elif Choice == "3":
                        print( x, " x ", y ," = ", multi(x, y))

                    elif Choice == "4":
                        print( x, " ÷ ", y ," = ", divide(x, y))
                    break
            except ValueError:
                print("Invalid choice, please enter a valid number")

     

        #ask user if they want to do another calculation
        NextCal = input("Do you want to make another calculation?(y/n)")
        #if no end program
        if NextCal =="n":
            print("Exiting the calculator. Goodbye!")
            break
        #error handling (else to if choice(1,2,3,4,5))
    else :
        print("Invalid choice. Please enter a valid choice ")
