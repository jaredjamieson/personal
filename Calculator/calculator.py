from linked_stack import LinkedStack


def calculate():
    """ User input filename, print result of each expression """
    mainlist = []                                                          # Create empty main list
    filename = 'expressions.txt'
    #filename = input(str('Enter a file name: '))
    filein = open(filename, 'r')

    for line in filein:                                                    # Read each line one at a time
        templist = []                                                      # Create empty temp list
        line = line.strip()                                                # Removes \n and split by spaces
        line = line.split(' ')

        mainlist.append(line)                                              # Append line to mainlist                                      
    
    #mainlist                                                              # Original text file seperated into elements
    conversion = convert_postfix(mainlist)                                 # Convert mainlist into postfix
    print(solve_postfix(conversion))                                       # Prints outputs of postfix                     
    
    
def convert_postfix(infix):
    """ Returns infix expression converted to postfix format """
    
    s = LinkedStack()                                                     # Create linked stack object
    postfix = []                                                          # Create main list
    
    for line in infix:
        templine = []                                                     # Create temporary line list
        for char in line:
            if char.isdigit() == True:                                    # If append digits to temp line
                templine.append(char)
            elif char == '(':                                             # Push () to linked stack
                s.push(char)
            elif char == ')':
                while (s.top() != '('):                                   # Keep pushing until reach (
                    templine += s.pop()
                s.pop()
            elif char == '+' or char == '-' or char == '*' or char == '/':# Do symbols in order of precedence while not empty
                while not s.is_empty() and s.top() != '(' and precedence(char) <= precedence(s.top()):
                    templine += s.pop()
                s.push(char)
        while not s.is_empty():
            templine += s.pop()
        postfix.append(templine)                                           # Append templine to main list
    print(postfix)
    return postfix                                                         # Return mainlist as postfix


def precedence(char):
    """ Returns order of operands """
    if char == '+' or char == '-':
        return 1
    elif char == '*' or char == '/':                                       # Set precedence of * and / over + and -
        return 2
    
    
def solve_postfix(conversion):
    """ Returns solved postfix expression """
    s = LinkedStack()                                                      # Create linked stack object
    output = []                                                            # Create output list
    
    for line in conversion:
        for element in line:                                               # For each element of embedded list
            if element.isdigit() == True:
                s.push(element)                                            # If digit, push
            else:
                operator = element                                         # Else, pop top two nums and operator
                op2 = s.pop()
                op1 = s.pop()
                op2 = int(op2)
                op1 = int(op1)
                if operator == '+':
                    result = op2 + op1
                elif operator == '-':
                    result = op1 - op2
                elif operator == '*':
                    result = op2 * op1
                else:
                    result = op1 // op2

                s.push(result)                                              # Push result of top two pop and operator
        output.append(s.pop())                                              # Append the pop to output
    
    return output                                                           # Return all lists solved to calculate()
     
     
def main():
    calculate()
    
main()