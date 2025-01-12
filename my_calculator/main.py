num1 = float(input("Enter 1st no. : "))
operator = input("Enter your operator : ")
num2 = float(input("Enter 2nd no. : "))

def calculate(num1,num2,operator):
    
    if operator == "+":
        result = (num1 + num2)
    elif operator == "-":
        result = (num1 - num2)
    elif operator == "*":
        result = (num1 * num2)
    elif operator == "/":
        if num2 == 0: # Here, we put an if condition in elif statement for zero division.
            return "Zero division is not allowed" 
        result = num1 / num2
    else:
        return "Invalid Operation"
    return f"Result : {result}"

result_calculated = calculate(num1,num2,operator)
print(result_calculated)

choice = input("Do you want to carry on another operation ?? : ")

while choice.lower() == "yes":
    num1 = float(input("Enter 1st no. : "))
    operator = input("Enter your operator : ")
    num2 = float(input("Enter 2nd no. : "))
    

    result_calculated = calculate(num1,num2,operator)
    print(result_calculated)

    choice = input("Do you want to carry on another operation ?? : ")

while choice.lower() != "yes":
    break