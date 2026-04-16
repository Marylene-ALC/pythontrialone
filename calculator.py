num1 = int(input("Enter your First number:"))
num2 = int(input("Enter your Second number:"))
operation = input("select(*,+,-,/):")

if operation == "+":
    print(f"Sum = {num1 + num2}")
elif operation == "-":
    print(f"Answer = {num1-num2}")
elif operation == "*":
    print(f"Answer = {num1*num2}")
elif operation == "/" :   
    if num2 != 0:
        print(f"Answer = {num1 / num2}")
    else:
        print("Error: Cannot divide by zero!")
else:
    print("What is your operation?")
    

    
