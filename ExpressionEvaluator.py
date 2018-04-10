# Stack data structure
class Stack:
    def __init__(self):
         self.items = []

    def isEmpty(self):
         return self.items == []

    def push(self, item):
         self.items.append(item)

    def pop(self):
         return self.items.pop()

    def peek(self):
         return self.items[len(self.items)-1]

    def size(self):
         return len(self.items)
    def printStack(self):
         x = []
         for items in reversed(self.items):
             x.append(items)
         return x

# Checks for valid operation
def isOperator(op):
    add = "+"
    sub = "-"
    if (op == add) or (op == sub):
        return True
    else:
        return False

# Checks if a number is a float
def isFloat(val):
    val = str(val)
    if '.' in val:
        return True
    else:
        return False


 # @param input is an input file of valid expressions. It may contain only one expression on each line
 #        output is a file the answers to the expressions will be written on.
 #
 # The expressionTOArray function reads an input file and stores each line into inputArray.
 # Then reverseseach expression in inputArray and returns the computeExpression function with the list and output file as it's parameters
 #
 # Valid expressions include only '+' and '-' operations and only includes integers and floating point numbers
 # as expressions
 # The syntax for expressions in input file is always <operation> <expression> <expression>
 #
 # @author  Nikhil Mithani

def evaluateExpression(input, output):
    inputArray = []
    inputArraySplit = []
    f = open(input, 'r').readlines()
    for line in f:
        line = line.strip() #strip removes leading and trailing space from string
        line = line.split()
        inputArray.append(line)
    for line in inputArray:
        line.reverse()
    print inputArray
    return computeExpression(inputArray, output)

 # @param arr stores expression in each index. When multiple expressions are given in input file each line of
 #         input file is stored in individual index of arr
 #        output is a file the answered to the expressions will be written to
 #
 # The computeExpression function iterates through arr and pushes numbers on to a stack. When an operation is
 # found it pops the top two element of stack performs operation and pushes the result onto stack
 # After iterating through arr it prints the stack elements onto output file by popping every element of Stack into
 # ansList reversing the list and then writing each elem of ansList onto output file

def computeExpression(arr, output):
    addition = "+"
    subtraction = "-"
    arrLen = len(arr)
    print arrLen
    index = 0
    stack = Stack()
    while index < arrLen:
        input = arr[index]
        inputLen = len(input)
        index2 = 0
        while index2 < inputLen:
            input2 = input[index2]
            if isOperator(input2):
                exp1 = int(stack.pop())
                exp2 = int(stack.pop())
                if input2 == addition:
                    expAns = exp1 + exp2
                else:
                    expAns = exp1 - exp2
                stack.push(expAns)
            else:
                stack.push(input2)
            index2 += 1
        index += 1
    print stack.printStack()
    ansList= []
    while not stack.isEmpty():
        ansList.append(str(stack.pop()))
    ansList.reverse()
    print ansList
    fileOut = open(output, 'w')
    for line in ansList:
        fileOut.write(line +"\n")

# Main method to call expressionTOArray
if __name__== "__main__":
    evaluateExpression('input.txt', 'output.txt')
