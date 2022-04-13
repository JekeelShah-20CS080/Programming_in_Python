##
# Jekeel Shah 20CS080
# Practical 8
# #

# Creating a stack
def create_stack():
    stack = []
    return stack

def check_empty(stack):
    return len(stack) == 0

# Push operation
def push(stack, item):
    stack.append(item)
    print('Pushed element',item,'into the stack!')

# Pop operation
def pop(stack):
    if (check_empty(stack)):
        return "Stack is empty! :("
    return stack.pop()

stack = create_stack()
print('Enter number of elements to be pushed into the stack: ',end=' ' )
count = int(input())
print()

for  i  in range(count):
        print('Enter data for element',i+1,': ',end=' ')
        data = int(input())
        push(stack,str(data))
        print()

print()
print("Popped element: " + pop(stack))
print()
print("Stack after Pop operation : " + str(stack))
print()
print('Prepared by Jekeel Shah 20CS080')
print('Thank you! :)')
