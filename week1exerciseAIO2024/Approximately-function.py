def factorial(n):#to find the factorial of n
    if n == 0 or n == 1 :
        return 1
    else:
        return n * factorial(n-1)
def sin(x,n):
    s = 0
    for i in range(n):
        s += ((-1)**i) * (x**(2*i + 1) / factorial(2*i + 1))
    return s
def cos(x,n):
    s = 0
    for i in range(n):
        s += ((-1)**i) * (x**(2*i) / factorial(2*i))
    return s
def sinh(x,n):
    s = 0
    for i in range(n):
        s += (x**(2*i + 1) / factorial(2*i + 1))
    return s
def cosh(x,n):
    s = 0
    for i in range(n):
        s += (x**(2*i) / factorial(2*i))
    return s
print(round(cosh(3.14,10),2))