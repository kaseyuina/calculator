import math
import sys

equation_list = []
operators = "+*-/()"
temp = ""

print()
print("Please type in the equation which you would like to calculate.")
print("(Available operators are: ")
print("Addition: +, Subtraction: -, Multiplication: *, Division: /)")
print("You may also use parentheses.")
# equation = (input(": "))
print()

#Unit test case 1
equation = "(1+1.25-23)/2*4"
# equation = "(1 + 1.25 - 23) / 2 * 4 "
# equation = "1 + x + 5"

#Unit test case 2
# equation = "5*4"
# equation = "15/3"
# equation = ""


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


print(infix_to_postfix(equation_list))

def RPN(states):
    operator = {
        '+': (lambda x, y: float(x) + float(y)),
        '-': (lambda x, y: float(x) - float(y)),
        '*': (lambda x, y: float(x) * float(y)),
        '/': (lambda x, y: float(x) / float(y))
    }
    stack = []
    # print('RPN: %s' % states)
    for index, z  in enumerate(states):
        # if index > 0:
            # print(stack)
        if z not in operator.keys():
            stack.append(z)
            continue
        y = stack.pop()
        x = stack.pop()
        stack.append(operator[z](x, y))
        # print('%s %s %s =' % (x, z, y))
    # print(stack[0])
    return stack[0]

# print(RPN(infix_to_postfix(equation_list)))

'''
def test():
    print("OK" if RPN("37+621-*+") == 16 else "NG")

if __name__ == '__main__':
    import sys
    RPN(sys.argv[1])
    test()
'''







'''
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
'''