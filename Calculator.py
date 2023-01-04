def add(i,j):
    print(f'the sum of {i} and {j} is{i+j}')

def sub(i, j):
    if i>=j :
         print(f'The difference between {i} and {j} is {i-j}')
    else:
        print(f'The difference between {j} and {i} is {j-i}')

def mul(i,j):
    print(f'The product of {i} and {j} is {i*j}')

def div(i,j):
    if i>=j:
        print(f'The division of {i} by {j} gives {i/j}')
    else:
        print(f'The divisiom of {j} by {i} gives {j/i}')    

while True:
    num= int(input('Enter the first number: '))
    num1= int(input('Enter the second number: '))
    print('select the Operation to be perfomd [+,-,*,/]')
    string1=input('Enter the operation: ')
    if string1 =='+':
        add(num,num1)
    elif string1=='-':
        sub(num,num1)
    elif string1=='*':
        mul(num,num1)
    elif string1=='/':
        div(num,num1)   
    print('------------------------------------------------------------------------')         


