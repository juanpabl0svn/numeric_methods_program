from sympy import symbols, diff

def factorial(x):
    value = 1
    for i in range(1,x+1):
        value*=i
    return value


def taylor(f,x0,n):
    P=0
    x = symbols('x')
    for i in range(n+1):
        df = diff(f,x,i).subs({x:x0})
        T = (df*(x-x0)**i)/factorial(i)
        P += T

    return P