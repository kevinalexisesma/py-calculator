# The numbers to which the arithmetic operation is performed are obtained
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
# You are asked what operation you want to perform.
operation = input("Enter the operation you want to perform: "
                  +"\n 1. if it is sum"
                  +"\n 2. if it is subtraction"
                  +"\n 3. if it is division"
                  +"\n 4. if it is multiplication.\n\n")
# The typed operation is performed
if operation == "1":
    sum = num1 + num2
    print(f"\n The sum is: {sum}")
elif operation == "2":
    subtraction = num1 - num2
    print(f"\n The subtraction is: {subtraction}")
elif operation == "3":
    if num2==0 : 
        print(f"\n The second number entered cannot be zero: {num2}")
    else:    
        division = num1 / num2
        print(f"\n The division is: {division:.2f}")
elif operation == "4":
    multiplication = num1 * num2
    print(f"\n The multiplication is: {multiplication}")
else:
    print(f"\nHe made the wrong operation.")