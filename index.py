# My Calculator


operand = input("Enter Your Operand * / + -")
num1 = float(input("Enter Your First Number: "))
num2 = float(input("Enter Your Second Number: "))

if operand == "*" :
    result = num1 * num2

if operand == "/" :
    result = num1 / num2

if operand == "-" :
    result = num1 - num2

if operand == "+" :
    result = num1 + num2


print("The Answer Is:", result)