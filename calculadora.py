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
    suma = num1 + num2
    print("\n The sum is: ", suma)
else:
    print("\nHe made the wrong operation.")