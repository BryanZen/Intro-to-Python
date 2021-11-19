# Decode/evaluate an arithmetic expression written in reverse Polish notation (RPN), or postfix notation

def rpn(data):
    # Take a string that represents an RPN-format expression and return its final value (as a number)

    values = [] # Initially, we have not seen/stored any numbers

    for character in data:
        print("Current character is", character)
        if character == "+": # Addition
            operand_2 = values.pop(-1) # Extract the last item in values
            print("The last element of values becomes operand_2:", operand_2, "and values is now", values)
            operand_1 = values.pop(-1) # Extract the new last item in values
            print("The last element of values becomes operand_1:", operand_1, "and values is now", values)
            sum = operand_1 + operand_2
            print("Add", operand_1, "to", operand_2, "to get", sum)
            values.append(sum) # Places the result at the end of the list
        else: # We assume that character is a number
            values.append(int(character))
        print("values is now", values)

    if len(values) == 1: # We should have exactly one number left when we're done
        return values[0]
    else:
        return -99999 # signal an error

postfix = input("Please enter an RPN/postfix expression: ")
answer = rpn(postfix)
print("This expression evaluates to", answer)
