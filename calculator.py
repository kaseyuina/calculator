import math
import sys

equation_list = []
operators = "+*-/^()"
temp = ""

print()
print("Please type in the equation which you would like to calculate.")
print("(Available operators are: ")
print("Addition: +, Subtraction: -, Multiplication: *, Division: /, Exponentiation: ^)")
print("You may also use parentheses.")
# equation = (input(": "))

#Unit test case 1
# equation = "(1+1.25-23)/2*4^3"
# equation = "(1 + 1.25 - 23) / 2 * 4 ^ 3 "
# equation = "1 + x + 5"

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
