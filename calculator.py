import math
import sys

equation_list = []
operators = "+*-/()"
temp = ""

print()
print("Please type in the equation which you would like to calculate.")
print("(Available operators are: ")
print("Addition: +, Subtraction: -, Multiplication: *, Division: /")
print("You may also use parentheses.")
# equation = (input(": "))

#Unit test case 1
# equation = "(1+1.25-23)/2*4"
# equation = "(1 + 1.25 - 23) / 2 * 4 "
# equation = "1 + x + 5"

#Unit test case 2
equation = "5*4"
# equation = "15/3"
# equation = ""


print()
print("equation is: " + equation)

#Storing equation to the list
for x, i in enumerate(equation):
    #Validation of the character
    if not i.isnumeric() == True:
        if not i == ".":
            if not i == " ":
                if operators.find(i) < 0:
                    print("The equation contains invalid character(s).")
                    sys.exit()
    #Storing in the list
    if operators.find(i) >= 0:
        if not temp == "":
            equation_list.append(temp)
        equation_list.append(i)
        temp = ""
    else:
        #Ignore a space
        if not i == " ":
            temp = temp + i
    #Operation for the last letter
    if x + 1 == len(equation):
        equation_list.append(temp)

print(equation_list)

def calc(num1, num2, operator):
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        if num2 == 0:
            print("Can't divide with 0")
            sys.exit()
        else:
            return num1 / num2


for i in range(len(equation_list)):
    print(equation_list)
    if equation_list[i] == "*" or equation_list[i] == "/":
        # print(calc(float(equation_list[i-1]), float(equation_list[i+1]), equation_list[i]))
        equation_list[i-1] = calc(float(equation_list[i-1]), float(equation_list[i+1]), equation_list[i])
        equation_list.pop(i)
        equation_list.pop(i)
        i -= 1

# for i in range(len(equation_list)):
#     if equation_list[i] == "+" or equation_list[i] == "-":
#         print(calc(float(equation_list[i-1]), float(equation_list[i+1]), equation_list[i]))

print(equation_list)
