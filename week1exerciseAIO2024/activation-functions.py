import math
def is_number(k):#check if it is a number
    try:
        float(k)
    except ValueError:
        return False
    return True
def sigmoid(n):
    return 1/(1 + math.exp(-n))
def relu(n):
    if n > 0:
        return n
    else:
        return 0
def elu(n):
    if n > 0 :
        return n
    else:
        return 0.01 * (math.exp(n) - 1)
def check_exist(b): # check if the function is exist
    if b == 'sigmoid' or b == 'relu' or b == 'elu':
        return True
    return False

n = input()
function = input()
if is_number(n):
    if check_exist(function):
        if function == 'relu':
            print(f'f({n}) is {relu(float(n))}')
        elif function == 'sigmoid':
            print(f'f({n}) is {sigmoid(float(n))}')
        elif function == 'elu':
            print(f'f({n}) is {elu(float(n))}')
    else:
        print(f'{b} is not supported')
else:
    print('x must be a number')
is_number(n)