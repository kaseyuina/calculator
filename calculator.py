import sys

equation_list = []
operators = "+*-/()"
temp = ""

print()
print("Please type in the equation which you would like to calculate.")
print("(Available operators are: ")
print("Addition: +, Subtraction: -, Multiplication: *, Division: /)")
print("You may also use parentheses.")
equation = (input(": "))

#Unit test case 1
# equation = "(1+1.25-23)/2*4"
# equation = "(1 + 1.25 - 23) / 2 * 4 "
# equation = "1 + x + 5"

#Unit test case 2
# equation = "2.5+34"
# equation = "54-13.4"
# equation = "5.123*23"
# equation = "15/3"
# equation = "15/3.333"
# equation = "15/0"
# equation = "5+6-1"
# equation = "5+3*6"
# equation = "9*(1+3)"
# equation = "10/(1-1)"
# equation = "(1+((2+3)*(4*5)))"
 
print()
# print("equation is: " + equation)

#Storing equation to the list
for x, i in enumerate(equation):
    #Validation of the character
    if not i.isnumeric() == True:
        if not i == ".":
            if not i == " ":
                if operators.find(i) < 0:
                    print("The equation contains invalid character(s).")
                    print()
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
    if x + 1 == len(equation) and not operators.find(i) >= 0:
        equation_list.append(temp)

# print(equation_list)

operator_precedence = {
    '(' : 0,
    ')' : 0,
    '+' : 1,
    '-' : 1,
    '*' : 2,
    '/' : 2
}
 
def infix_to_postfix(infix):
    stack = []
    postfix = [] 
         
    for char in infix:
        if char not in operator_precedence:
            postfix.append(char)
        else:
            if len(stack) == 0:
                stack.append(char)
            else:
                if char == "(":
                    stack.append(char)
                elif char == ")":
                    while stack[len(stack) - 1] != "(":
                        postfix.append(stack.pop())
                    stack.pop()
                elif operator_precedence[char] > operator_precedence[stack[len(stack) - 1]]:
                    stack.append(char)
                else:
                    while len(stack) != 0:
                        if stack[len(stack) - 1] == '(':
                            break
                        postfix.append(stack.pop())
                    stack.append(char)
     
    while len(stack) != 0:
        postfix.append(stack.pop())
 
    return postfix


# print(infix_to_postfix(equation_list))

def RPN(states):
    operator = {
        '+': (lambda x, y: float(x) + float(y)),
        '-': (lambda x, y: float(x) - float(y)),
        '*': (lambda x, y: float(x) * float(y)),
        '/': (lambda x, y: float(x) / float(y))
    }
    stack = []
    for z in states:
        if z not in operator.keys():
            stack.append(z)
            continue
        y = stack.pop()
        x = stack.pop()
        if float(y) == 0 and z == "/":
            print("Division by 0 not allowed.")
            print()
            sys.exit()
        stack.append(operator[z](x, y))
    return stack[0]

print("The answer is: " + str(RPN(infix_to_postfix(equation_list))))
print()