import numpy as np
import sympy as sp
# import pandas as pd

def Falsa(f,a,b,tol):
    if (f(a)*f(b)>0):
        print('la función no cumple el teorema')
    else:
        data=[]
        c=(b*f(a)-a*f(b))/(f(a)-f(b))
        while(np.abs(f(c))>tol):
            c=(b*f(a)-a*f(b))/(f(a)-f(b))
            data.append([a,b,c,np.abs(f(c)),np.abs(b-a)])
            if (f(a)*f(c)<0):
                b=c
            else:
                a=c
    return c

# def Newton(f,xo,tol):
#     fp=sp.diff(f,x)
#     newT=x-f/fp
#     newT=sp.lambdify(x,newT)
#     x1=newT(xo)
#     nmax=50
#     i=1
#     while(np.abs(x1-xo)>tol and nmax>i):
#         xo=x1
#         x1=newT(xo)
#         i+=1
#     print('La raiz de la funcio es: ',x1,'Las interaciones son: ',i)
#     return x1

def biseccion(f,a,b,tol = 1E-10):
    if (f(a)*f(b)>0):
        raise 'la función no cumple el teorema'
    data=[]
    while(np.abs(b-a)>tol):
        c=(a+b)/2
        data.append([a,b,c,f(a),f(c),np.sign(f(a)*f(c)),np.abs(b-a)])
        if (f(a)*f(c)<0):
            b=c
        else:
            a=c
    return data,c

def Secante(f, xo, x1, tol):
    while(np.abs(x1-xo)>tol):
        x2=x1-(f(x1)*(x1-xo))/(f(x1)-f(xo))
        xo=x1
        x1=x2
    return x2

# print(Biseccion(lambda x: x,30,41,.001))
