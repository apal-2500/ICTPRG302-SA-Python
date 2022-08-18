#A simple calculator to add, subtract, multiply and divide two values together.


#While - a loop to keep the calculator running until the using inputs true to end the program:
end = "false"
while end != "true":
    
#Variables to store the input from the user:
    value1 = int(input(print("Please enter the first value "))); #the storing of the first value input by the user.
    value2 = int(input(print("Please enter the second value "))); #the storing of the second value input by the user.

    opr = str(input("Enter Operation (+, -, *, /) => ")) #the storing of the operation the user wishes to use.

    if opr == "+": #this statement takes the two numbers input by the user and if the addition symbol is chosen will add the values.
        total = value1 + value2 
    elif opr == "-": #this statement takes the two numbers input by the user and if the subtraction symbol is chosen will add the values.
        total = value1 - value2
    elif opr == "*": #this statement takes the two numbers input by the user and if the multiply symbol is chosen will add the values.
        total = value1 * value2
    elif opr == "/": #this statement takes the two numbers input by the user and if the divide symbol is chosen will add the values.
        total = value1 / value2
    else: #this will produce an error message to a user if the wrong operation is chosen.
        total = str("Please enter a valid operation")
    
    #below we will print out the total of the chosen operation
    print (total)
    
    #below we will give the user the option to proceed to a new operation or the exit out.
    end = input(print("Continue true/false  "))
    
    #the end.